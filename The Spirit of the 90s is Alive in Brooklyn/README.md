## The Spirit of the 90s is Alive in Brooklyn

Using the tools and techniques of today to solve problems that only existed in the 90s and are still alive in DEFCON CTF. We explain and demo tools built on Binary Ninja’s BNIL to find 90s era bugs such as format string vulnerabilities, stack buffer overflows, and command injection.

Presented at

* [SummerCon 2017](http://www.summercon.org/presentations.html#90s-alive-in-brooklyn)

Resources

* [Slides](https://docs.google.com/presentation/d/1YSEfpEuBPp7g-kVHlbEjkXHJi1jbNt7-D8JoUFYlDJM/embed?start=false&loop=true&delayms=3000&slide=id.g1f7fb3a661_0_0)

[Binary Ninja Plugins](https://github.com/trailofbits/binjascripts/tree/master/abstractanalysis)

* uninitialized_variable_finder.py - Find uses of uninitialized variables
* uninitialized_variable_finder.py - Abstract interpretation using lattices to analyse the possible sign of a variable at any point in a program
* binja_memcpy.py - Demonstrates Binary Ninja's headless API for python by finding memcpy's and cooresponding src/dst information. It can be easily modified to find argument information for other function calls.
* walk_via_dfs.py - A plugin template to walk the Binary Ninja CFG using the depth-first search algorithm (aka path sensitive, one path traversed at a time)

Authors

* Sophia D'Antoine
* Ryan Stortz
