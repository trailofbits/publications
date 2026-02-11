---
title: "MLIR is the future of program analysis"
date: 2023
authors:
  - Peter Goodman
conference:
  - Qualcomm Product Security Summit 2023
resources:
  - label: Slides
    path: "QPSS_2023_-_MLIR_is_the_future_of_program_analysis.pdf"
---

The last 15 years of program analysis research with C/C++ code has focused on performance and correctness, mainly using LLVM IR as the sole analysis substrate. The next 15 years will not. While correctness and performance remain essential, new challenges are approaching: end-to-end optimization for heterogeneous compute platforms (AI/ML accelerators, GPUs, cryptography processors, etc.), energy efficiency, and enabling full-stack bug-finding across program representations. In the next 15 years, analyses will operate on a tower of IRs, with the same program represented at multiple simultaneous abstraction levels. This talk shows how existing open-source projects (e.g., VAST, ClangIR) building off of the LLVM project's Multi-level Intermediate Representation (MLIR) infrastructure are bringing about this future today.
