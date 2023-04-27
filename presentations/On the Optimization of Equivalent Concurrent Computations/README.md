# On the Optimization of Equivalent Concurrent Computations

In this talk, we will explore the use of equality saturation to optimize concurrent computations. A concurrent environment gives rise to new optimization opportunities, like extracting a common concurrent subcomputation. To our knowledge, no existing equality saturation framework allows such an optimization. The challenge with concurrent environments is that they require non-local reasoning since parallel computations are inherently unrelated and disjoint. This talk will present a new approach to optimizing equivalent concurrent computations: extending e-graphs to capture equal concurrent computations in order to replace them with a single computation.

Presented at
- [PLDI EGRAPHS 2022](https://pldi22.sigplan.org/program/program-egraphs-2022/)

Authored by
- Henrich Lauko (presenter)
- Lukáš Korenčik
- Peter Goodman
