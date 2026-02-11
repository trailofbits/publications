---
title: "Toward Automated Grammar Extraction via Semantic Labeling of Parser Implementations"
date: 2020-05-21
authors:
  - Carson Harmon
  - Brad Larsen
  - Evan Sultanik
conference:
  - LangSec 2020
resources:
  - label: Slides
    path: "PolyMerge_LangSec2020.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=N2QYMUPKQRE
  - label: Blog Post
    url: https://blog.trailofbits.com/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/
  - label: PolyFile
    url: https://github.com/trailofbits/polyfile
  - label: PolyTracker
    url: https://github.com/trailofbits/polytracker
---

This talk introduces a new approach for labeling the semantic purpose of functions in a parser. An input file with a known syntax tree is passed to an instrumented copy of the target parser for universal taint tracking. A novel algorithm merges that syntax tree ground truth with observed taint and control-flow information, producing a mapping from file format types to the set of functions most specialized in operating on that type. The resulting mapping has applications in mutational fuzzing, reverse engineering, differential analysis, and automated grammar extraction.
