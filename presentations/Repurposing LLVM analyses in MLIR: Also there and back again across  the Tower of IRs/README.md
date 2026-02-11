---
title: "Repurposing LLVM analyses in MLIR: Also there and back again across the Tower of IRs"
date: 2024-04-10
authors:
  - Henrich Lauko
conference:
  - EuroLLVM Developers' Meeting 2024
resources:
  - label: Slides
    path: "slides.pdf"
  - label: Recording
    url: https://youtu.be/pfViYCignjY
---

LLVM IR has a rich history of tools and analyses, but with the rise of MLIR there is a challenge of transitioning these valuable legacy analyses to the new representation. This talk walks through a solution that allows repurposing LLVM analyses in MLIR seamlessly using a "tower of IRs" that connects the LLVM representation to the desired MLIR dialect, enabling analysis outcomes from LLVM IR to be related directly to an MLIR dialect.
