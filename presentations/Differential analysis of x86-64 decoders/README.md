---
title: "Differential Analysis of x86-64 Instruction Decoders"
date: 2021-05
authors:
  - William Woodruff
  - Niki Carroll
  - Sebastiaan Peters
conference:
  - LangSec Workshop at IEEE S&P 2021
resources:
  - label: Slides
    path: "langsec-2021-slides.pdf"
  - label: Paper
    url: https://easychair.org/publications/preprint/1LHr
  - label: Mishegos
    url: https://github.com/trailofbits/mishegos
---

This presentation describes the application of differential fuzzing to x86-64 instruction decoders for bug discovery. It introduces Mishegos, a novel differential fuzzer that discovers decoding discrepancies between instruction decoders. The talk covers the architecture of Mishegos, the security implications of decoding errors in sandboxes, JITs, antivirus tools, and binary translators, and a novel fuzzing strategy for variable-length instruction architectures. Mishegos produces hundreds of millions of decoder tests per hour and has been used to discover hundreds of errors in popular x86-64 decoders.
