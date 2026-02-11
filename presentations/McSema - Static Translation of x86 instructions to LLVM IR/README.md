---
title: "Static Translation of X86 Instruction Semantics to LLVM with McSema"
date: 2014-06-28
authors:
  - Andrew Ruef
  - Artem Dinaburg
conference:
  - REcon 2014
resources:
  - label: Slides
    path: "McSema.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=nW9bE5tUVYg
  - label: Source Code
    url: https://github.com/trailofbits/mcsema
  - label: Blog Post
    url: https://blog.trailofbits.com/2014/06/23/a-preview-of-mcsema/
---

We have developed McSema, a new framework for analyzing and transforming machine-code programs. McSema translates x86 instructions into LLVM bitcode, with a translation strategy that allows for analysis by standard compiler algorithms. The talk demonstrates McSema by adding control flow integrity to existing Windows DLLs. McSema is open source, permissively licensed, and available for use and modification.
