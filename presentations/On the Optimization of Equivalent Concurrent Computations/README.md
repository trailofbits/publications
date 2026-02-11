---
title: "On the Optimization of Equivalent Concurrent Computations"
date: 2022-06-14
authors:
  - Henrich Lauko
  - Lukáš Korenčik
  - Peter Goodman
conference:
  - PLDI EGRAPHS 2022
resources:
  - label: Slides
    path: "PLDI-EGRAPHS-2022.pdf"
---

This talk explores the use of equality saturation to optimize concurrent computations. A concurrent environment gives rise to new optimization opportunities, like extracting a common concurrent subcomputation. To our knowledge, no existing equality saturation framework allows such an optimization. The challenge with concurrent environments is that they require non-local reasoning since parallel computations are inherently unrelated and disjoint. The talk presents a new approach to optimizing equivalent concurrent computations: extending e-graphs to capture equal concurrent computations in order to replace them with a single computation.
