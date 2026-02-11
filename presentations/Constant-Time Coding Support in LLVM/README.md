---
title: "Constant-Time Coding Support in LLVM"
date: 2025-10
authors:
  - Julius Alexandre
conference:
  - US LLVM Developers' Meeting 2025
resources:
  - label: Slides
    path: "Constant-Time Coding Support in LLVM.pdf"
  - label: Recording
    url: https://youtu.be/zLBEXGTdd6o?si=pBBXe9AbOYwjeKED
---

This presentation covers Trail of Bits' work on adding constant-time coding support to the LLVM compiler infrastructure. The effort introduces compiler-level guarantees that cryptographic implementations remain secure against timing side-channel attacks by preventing the compiler from inadvertently breaking carefully crafted constant-time code. The talk discusses the design and implementation of new intrinsics and supporting infrastructure, developed in collaboration with the System Security Group at ETH Zurich.
