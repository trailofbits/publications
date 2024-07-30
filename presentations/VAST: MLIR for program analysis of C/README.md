VAST: MLIR for program analysis of C/C++
=====================================================================================

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

Resources:
* [Slides](slides.pdf)
* [Video](https://youtu.be/YFqWa4pxXzM?si=5GZjmm7-AsM8DkhN)

Presented at:

* [LLVM Developers' Meeting, 2022](https://llvm.swoogo.com/2022devmtg/session/1093944/vast-mlir-for-program-analysis-of-cc++)

Authored by:

* Henrich Lauko
