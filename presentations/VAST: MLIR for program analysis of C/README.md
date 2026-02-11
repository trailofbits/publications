---
title: "VAST: MLIR for program analysis of C/C++"
date: 2022-11
authors:
  - Henrich Lauko
conference:
  - LLVM Developers' Meeting 2022
resources:
  - label: Slides
    path: "slides.pdf"
  - label: Recording
    url: https://youtu.be/YFqWa4pxXzM?si=5GZjmm7-AsM8DkhN
---

Program analysis has specific requirements for compiler toolchains that are
usually unsatisfied. Ideally, an analysis tool would pick the best-fit
representation that preserves interesting semantic features. Such a
representation would know the precise relationships between low-level constructs
in IR and the analyzed source code. LLVM IR is rarely the best fit
representation for program analysis. In this talk, we will look at how we can
improve the situation using an MLIR infrastructure called VAST. VAST is an MLIR
library for multi-level C/C++ representation. With VAST, an analysis does not
need to commit to a single best fit. Instead, an analysis can have simultaneous
visibility into multiple progressions of the code, from very high-level down to
very low-level.
