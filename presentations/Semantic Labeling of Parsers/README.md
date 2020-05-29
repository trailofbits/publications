# Toward Automated Grammar Extraction via Semantic Labeling of Parser Implementations

This is the conference talk associated with [an academic paper](../../papers/semantic_labeling_langsec2020.pdf) introducing a new approach for labeling the semantic purpose of the functions in a parser. An input file with a known syntax tree is passed to a copy of the target parser that has been instrumented for universal taint tracking. This paper introduces a novel algorithm for merging that syntax tree ground truth with the observed taint and control-flow information from the parser's execution. This produces a mapping from types in the file format to the set of functions most specialized in operating on that type. The resulting mapping has applications in mutational fuzzing, reverse engineering, differential analysis, as well as automated grammar extraction. We demonstrate that even a single execution of an instrumented parser with a single input file can lead to a mapping that a human would identify as intuitively correct. We hope that this approach will lead to both safer subsets of file formats, as well as safer parsers.

Resources

* [Recording of the talk](https://www.youtube.com/watch?v=N2QYMUPKQRE).
* [Blog post](https://blog.trailofbits.com/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/) describing the project and tooling.

Presented at

* [LangSec 2020](http://spw20.langsec.org/)

Authored by

* Carson Harmon
* Brad Larsen
* Evan Sultanik
