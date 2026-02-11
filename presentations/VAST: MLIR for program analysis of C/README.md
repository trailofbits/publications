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

Program analysis has specific requirements for compiler toolchains that are usually unsatisfied. Ideally, an analysis tool would pick the best-fit representation that preserves interesting semantic features. LLVM IR is rarely the best fit for program analysis. This talk looks at how VAST, an MLIR library for multi-level C/C++ representation, improves the situation by allowing an analysis to have simultaneous visibility into multiple progressions of the code, from very high-level down to very low-level, without committing to a single best fit.
