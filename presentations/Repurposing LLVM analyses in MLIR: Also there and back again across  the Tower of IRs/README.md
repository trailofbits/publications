Repurposing LLVM analyses in MLIR: Also there and back again across  the Tower of IRs
=====================================================================================

LLVM IR boasts a rich history of tools and analyses, but with the emerging rise
of MLIR, there is a challenge of transitioning these valuable legacy analyses to
the new representation. Ideally, we would not have to touch them at all and
repurpose them in MLIR seamlessly. Imagine being able to relate your analysis
outcomes from LLVM IR directly to your MLIR dialect – pretty cool, right? In
this talk, I will walk you through a solution that allows us to achieve
precisely that using what we call a "tower of IRs," connecting LLVM
representation to the desired MLIR dialect.

Resources:
* [Slides](slides.pdf)
* [Video](https://youtu.be/pfViYCignjY?si=766DwSXOQbKzkZYU)

Presented at:

* [EuroLLVM Developers' Meeting, 2024](https://llvm.swoogo.com/2024eurollvm/session/2087007/quick-talks)

Authored by:

* Henrich Lauko
