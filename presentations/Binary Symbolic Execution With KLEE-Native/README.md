---
title: "Binary Symbolic Execution with KLEE-Native"
date: 2019-08-13
authors:
  - Sai Vegasena
conference:
  - Empire Hacking, August 2019
resources:
  - label: Slides
    path: "KLEE-Native EH Presentation.pdf"
---

KLEE is an emulator for LLVM bitcode primarily used in software testing and verification. This talk shows how Remill was used to lift binaries into LLVM and symbolically execute the result. Extensions to KLEE's syscall implementations, forking model, and heap memory model are discussed. The resulting KLEE-Native fork uses eager concretization to symbolically execute binaries, reproduce CVEs, model heap memory, classify heap bugs, emulate syscalls, and execute libc functions performantly with symbolic data.
