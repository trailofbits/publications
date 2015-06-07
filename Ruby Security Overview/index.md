---
layout: slides
title:  Ruby Security Workshop
author: Hal Brodigan
email:  hal@trailofbits.com
venue:  SummerCon 2013
date:   2013-06-06
---

{::options parse_block_html="true" /}

<div class="slide">
# {{ page.title }} 2013

<img src="images/ruby.png" class="hcenter" />
</div>

<div class="slide">
# Disclaimer

![I have only done this once before](images/disclaimer.jpg)
</div>

<div class="slide">
# Outline

1. Rails Vulnerabilities
2. Root Problems
3. Possible Solutions
</div>

<div class="slide">
# Rails Vulnerabilities, A Look Back

* CVE-2012-5664
* CVE-2013-0155
* CVE-2013-0156
* CVE-2013-0333
</div>

<div class="slide">
# CVE-2012-5664

{% highlight ruby %}
Post.find_by_id(params[:id])
{% endhighlight %}

{% highlight ruby %}
params[:id] = {:select => '; INSERT INTO admins ...'}
{% endhighlight %}
</div>

<div class="slide">
# params

* [ActionDispatch::Middleware::ParamsParser]
* Sych. `params` is a [HashWithIndifferentAccess].
* Every params key is coerced into a String.
* **Ruby idiom:** method options are always Symbol Hashes.

{% highlight ruby %}
Post.find_by_id('select' => 'SQL ...') # NOPE
{% endhighlight %}
</div>

<div class="slide">
# What about session?

{% highlight ruby %}
User.find_by_id(session[:user_id])
{% endhighlight %}

* authlogic (CVE-2012-6497)
* `sessions` comes from the cookie
* Unfortunately, the cookie is signed with a secret token
  * `config/initializers/secret_token.rb`
</div>

<div class="slide">
# Not Exploitable

![total self loathing despair](images/we_found_nothing.jpg)
</div>

<div class="slide">
# But it got people looking
</div>

<div class="slide">
# CVE-2013-0155

{% highlight ruby %}
unless params[:token].nil?
  user = User.find_by_token(params[:token])
  user.reset_password!
end 
{% endhighlight %}

* Truthiness and Nulliness.
* `[nil]`, `[""]` and `[[]]` are all not nil and not empty.
</div>

<div class="slide">
# CVE-2013-0156

* M-m-m-multiple vulnerabilities!
* [ActionDispatch::ParamsParser] supports parsing JSON, YAML and XML encoded
  request params.
* [ActiveSupport::XmlMini] allows for specifying types of elements
  * `type="symbol"` and `type="yaml"`
</div>

<div class="slide">
# CVE-2013-0333

* Fact: JSON is a subset of YAML.
* Fact: does not mean you should parse JSON with YAML.
* Fact: Rails 2.3.x and 3.0.x did just that.
</div>

<div class="slide">
# [ActiveSupport::JSON::Backends::Yaml]

* `convert_json_to_yaml` scans through the JSON, converting JSON syntax into
  YAML equivalents.
* Decodes the converted JSON using `YAML.load`.
* Does not decode escaped hex/unicode Strings **before** converting the JSON.
* Does not validate the input is well formed JSON.
</div>

<div class="slide">
# YAML Exploitation

![Evil](images/evil.jpg)
</div>

<div class="slide">
# YAML Syntax

* Commonly used as a more readable version of JSON:

{% highlight yaml %}
---
foo:
  - bar
  - baz
{% endhighlight %}

* But also allows serializing/deserializing arbitrary Objects:

{% highlight yaml %}
--- !ruby/object
x: 1
y: 2
{% endhighlight %}
</div>

<div class="slide">
# But wait there is more!

* Override the class for String. Will call `AwesomeString.new(value)`.

{% highlight yaml %}
--- !ruby/string:AwesomeString "foo bar baz"
{% endhighlight %}

* Override the class of Hashes. Will create a new `AwesomeHash` object and call
  `#[]=` to populate it.

{% highlight yaml %}
--- !ruby/hash:AwesomeHash
key: "hello\\nworld"
{% endhighlight %}
</div>

<div class="slide">
# What To Look For

* Are there classes that extend String but treated differently.
  (ex: [Arel::Nodes::SqlLiteral])
* Classes that define `#[]=` that pass the `key` or `value` to `eval` or
  `system`.
</div>

<div class="slide">
# Protip

* Find all Hash-like classes:

{% highlight ruby %}
ObjectSpace.each_boject(Class).select { |klass|
  klass.instance_methods.include?(:[]=)
}
{% endhighlight %}
</div>

<div class="slide">
# Exercises!

* Your mission if you choose to accept it:
  * Exploit a series of trivial Sinatra web-apps that accept YAML input.
  * Each app requires an increasingly nuanced method of exploitation.
  * Update the `exploit.rb` file until you can successfully execute
    `puts 'hello'`.
</div>

<div class="slide">
</div>

<div class="slide">
# Parsing

<img class="hcenter" src="images/parsing.gif" alt="Parsing can be hard" />
</div>

<div class="slide">
# Why Are We Even Covering This?

* Remember CVE-2013-0333 ?
* Using a single regular expression does not scale for parsing input.
* Simply tokenizing the input is not enough.
  [ActiveSupport::JSON::Backends::Yaml] even used the very handy
  [StringScanner] class.
* We need **full recognition**.
</div>

<div class="slide">
# Parsers

* [LALR] (Look-Ahead Left-Right) parsers:
  * yacc / bison
  * [racc]
* [PEG] (Parsing Expression Grammar) parsers:
  * [TreeTop]
  * [Citrus]
  * [Parslet]
</div>

<div class="slide">
# Parslet Parsers

* Define parsers by combining pattern matching rules:

{% highlight ruby %}
class EmailParser < Parslet::Parser
  rule(:space) { match('\s').repeat(1) }
  rule(:space?) { space.maybe }
  rule(:dash?) { match['_-'].maybe }

  rule(:at) {
    str('@') |
    (dash? >> (str('at') | str('AT')) >> dash?)
  }
  rule(:dot) {
    str('.') |
    (dash? >> (str('dot') | str('DOT')) >> dash?)
  }

  rule(:word) { match('[a-z0-9]').repeat(1).as(:word) >> space? }
  rule(:separator) { dot.as(:dot) >> space? | space }
  rule(:words) { word >> (separator >> word).repeat }

  rule(:email) {
    (words.as(:username) >> space? >> at >> space? >> words).as(:email)
  }

  root(:email)
end
{% endhighlight %}
</div>

<div class="slide">
# Parslet Parsers: Methods/Operators

* `rule(:name) { ... }` defines a parsing rule with the specified `name`.
* `root :name` defines which parsing rule to start at.
* `str(...)` matches a literal string.`
* `repeat` is equivalent of `regex*`.
* `repeat(1)` is equivalent to `regex+`.
* `repeat(1,5)` is equivalent to `regex{1,2}`.
* `match(...)` matches data against the specified regular expression.
* `match['a-z']` is shorthand for `match('[a-z'])`.
* `|` allows any one of multiple rules to be matched.
* `>>` requires multiple rules to be matched in succession.
* `.as(:name)` tags the matched text with the specified name.
</div>

<div class="slide">
# Parslet Parsers: Output

{% highlight ruby %}
EmailParser.new.parse("john dot smith AT gmail dot com")
{% endhighlight %}

{% highlight ruby %}
{:email=>[
  {:username=>[
    {:word=>"john"@0},
    {:dot=>"dot"@5, :word=>"smith"@9}
  ]},
  {:word=>"gmail"@18},
  {:dot=>"dot"@24, :word=>"com"@28}
]}
{% endhighlight %}
</div>

<div class="slide">
# Parslet Transforms

* Transforms or Sanitize the Parslet tree into something more useful:

{% highlight ruby %}
class EmailSanitizer < Parslet::Transform
  rule(:dot => simple(:dot), :word => simple(:word)) { ".#{word}" }
  rule(:word => simple(:word)) { word }

  rule(:username => sequence(:username)) { username.join + "@" }
  rule(:username => simple(:username)) { username.to_s + "@" }

  rule(:email => sequence(:email)) { email.join }
end
{% endhighlight %}
</div>

<div class="slide">
# Parslet Transforms: Methods

* `rule(:name => ...) { action }` defines a pattern matching rule for the
  Parslet tree.
* Parslet automatically walks the intermediary tree for you and performs
  `action` whenever it encounters `pattern`
* `simple(:name)` matches a single String value.
* `sequence(:name)` matches an Array of String values.
* `subtree(:name)` matches a Hash within the Parslet tree.
</div>

<div class="slide">
# Parslet Transforms: Output

{% highlight ruby %}
EmailSanitizer.new.apply(EmailParser.new.parse("john dot smith AT gmail dot com"))
# => "john.smith@gmail.com"
{% endhighlight %}
</div>

<div class="slide">
# Exercises!

* Your mission if you choose to accept it:
  * level1: write a JSON parser using Parslet.
  * level2: write Parslet Transforms to remove `[nil]`, `[""]` and `[[]]`.
  * Boilerplate code and RSpec tests provided.
</div>

<div class="slide">
</div>

<div class="slide">
# Mutation Testing

<img class="hcenter" src="images/mutation_testing.jpg" alt="Mutation Testing" />
</div>

<div class="slide">
# Problem

* How do we know when we have tested every edge-case?
  * Unit vs. Integration?
  * Test coverage metrics?
  * Do more tests really mean higher test coverage?
  * Input Fuzzing?
* How do we verify the correctness of the tests?
</div>

<div class="slide">
# Mutation Testing: A New Approach

* Instead of fuzzing the input, what if we fuzzed the **code**?
  (inception sound effect here)
  1. Parse the code into an AST
  2. Permutate over every mutation of the AST.
  3. Eval mutated AST.
  4. Run tests against mutated code.
  5. Since the code is semantically different, the tests _should_ fail.
     If the tests do not fail, than you have code which can break and the tests
     will not catch it.
</div>

<div class="slide">
# [Mutant]

* The new hotness in mutation testing for Ruby 1.9.
* Loads one or more test files and selects the classes you want to mutate.

      $ mutant -r ./spec/foo_spec.rb -r --rspec-full ::Foo

* When all mutations are "killed" by the tests, you have reached full coverage.
</div>

<div class="slide">
# Exercises!

* Your mission if you choose to accept it:
  * Write [RSpec] tests for some annoying complex authorization code for a
    fictional Secure Document Database.
  * Run the `rake mutant` task after writing tests.
  * When mutant prints all green, you are done.
</div>

<div class="slide">
</div>

<div class="slide">
# Ruby Security Tools, for Ruby

<img class="hcenter" src="images/ruby_security_tools.jpg" alt="When you get a box of lemons, you make lemonade" />
</div>

<div class="slide">
# Ecosystem

* [Egor Homakav]
* [Larry Cashdollar] (yes, that is his actual name)
* [Rails Security]
  * Michael Koziarski
  * Arron "tenderlove" Patterson
* [RedHat OpenShift]
  * Kurt Seifried (also runs oss-sec)
  * Ramon de C Valle (aka rcvalle)
* [RubySec]
  * Max Veytsman
  * Phill MV
  * Myself
  * Bryan Helmkamp
  * Charlie Summervile
  * Tony Arcieri
</div>

<div class="slide">
# Tools

* [brakeman]
* [ruby-advisory-db]
* [bundler-audit]
* [gemcanary]
* [ronin]
</div>

<div class="slide">
# Shameless Plug

* Ronin is kind of big, and kind of awesome:
  * [ronin-support]
  * [ronin]
  * [ronin-gen]
  * [ronin-asm]
  * [ronin-sql]
  * [ronin-web]
  * [ronin-exploits]
  * [ronin-scanners]
  * [ronin-bruteforcers]
  * I think I might have a programming problem
</div>

<div class="slide">
# Exercise!

* Your mission if you choose to accept it:
  * Convert one of your YAML exploits to use the convenience methods
    from [ronin-support].
  * Marvel at how easy it was.
</div>

[HashWithIndifferentAccess]: https://github.com/rails/rails/blob/v3.2.10/activesupport/lib/active_support/hash_with_indifferent_access.rb#L8
[ActionDispatch::Middleware::ParamsParser]: https://github.com/rails/rails/blob/v3.2.10/actionpack/lib/action_dispatch/middleware/params_parser.rb#L6
[ActiveSupport::XmlMini]: https://github.com/rails/rails/blob/v3.2.10/activesupport/lib/active_support/xml_mini.rb#L67
[ActiveSupport::JSON::Backends::Yaml]: https://github.com/rails/rails/blob/v3.0.0/activesupport/lib/active_support/json/backends/yaml.rb
[Arel::Nodes::SqlLiteral]: https://github.com/rails/arel/blob/master/lib/arel/nodes/sql_literal.rb

[LALR]: http://en.wikipedia.org/wiki/LALR_parser
[StringScanner]: http://rubydoc.info/stdlib/strscan/StringScanner
[racc]: https://github.com/tenderlove/racc#readme
[PEG]: http://en.wikipedia.org/wiki/Parsing_expression_grammar
[TreeTop]: http://treetop.rubyforge.org/
[Citrus]: http://mjijackson.com/citrus
[Parslet]: http://kschiess.github.io/parslet/

[Mutant]: https://github.com/mbj/mutant#readme
[RSpec]: https://www.relishapp.com/rspec

[Egor Homakov]: http://homakov.blogspot.com/
[Larry Cashdollar]: http://vapid.dhs.org/
[Rails Security]: http://rubyonrails.org/security
[RedHat OpenShift]: https://www.openshift.com/
[RubySec]: http://rubysec.github.io/

[brakeman]: http://brakemanscanner.org/
[ruby-advisory-db]: https://github.com/rubysec/ruby-advisory-db#readme
[bundler-audit]: https://github.com/postmodern/bundler-audit#readme
[gemcanary]: https://gemcanary.com/

[ronin-support]: https://github.com/ronin-ruby/ronin-support#readme
[ronin]: https://github.com/ronin-ruby/ronin#readme
[ronin-gen]: https://github.com/ronin-ruby/ronin-gen#readme
[ronin-asm]: https://github.com/ronin-ruby/ronin-asm#readme
[ronin-sql]: https://github.com/ronin-ruby/ronin-sql#readme
[ronin-web]: https://github.com/ronin-ruby/ronin-web#readme
[ronin-exploits]: https://github.com/ronin-ruby/ronin-exploits#readme
[ronin-scanners]: https://github.com/ronin-ruby/ronin-scanners#readme
[ronin-bruteforcers]: https://github.com/ronin-ruby/ronin-bruteforcers#readme
