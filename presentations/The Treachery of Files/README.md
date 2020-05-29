# The Treachery of Files

Parsing is hard, even when a file format is well specified. But when the specification is ambiguous, it leads to unintended and strange parser and interpreter behaviors that make file formats susceptible to security vulnerabilities. What if we could automatically generate a “safe” subset of any file format, along with an associated, verified parser? This talk explores that question, provides examples of malicious files, examines some troublesome parsers, and introduces two new tools for reverse engineering files and parsers. PolyFile is a tool for exploring the contents and structure of files to detect funky file tricks like steganography, polyglots, and chimeras. PolyTracker can instrument parsers to perform efficient universal taint tracking, to associate which bytes of the input file are operated on by which functions. Used in conjunction, these tools will permit us to specify safer subsets of file formats.

Resources

* [Blog post on the tooling](https://blog.trailofbits.com/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/)
* [PoC||GTFO](https://sultanik.com/pocorgtfo/), the journal in which most of the funky file format tricks were published
* https://github.com/trailofbits/polyfile
* https://github.com/trailofbits/polytracker

Presented at

* [BSides Philly 2017](https://www.youtube.com/watch?v=fdKPnsWp9ho): an earlier but more technically deep version
* [Empire Hacking, December 2019](https://www.youtube.com/watch?v=LqRbfzhcI5g): a newer version with much more breadth

Authored by

* Evan Sultanik
