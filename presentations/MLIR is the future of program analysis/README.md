# MLIR is the future of program analysis

The last 15 years of program analysis research with C/C++ code has focused on performance and correctness, mainly using LLVM IR as the sole analysis 
substrate. The next 15 years will not.

While correctness and performance remain essential, new challenges are approaching: end-to-end optimization for heterogeneous compute platforms (AI/ML 
accelerators, GPUs, cryptography processors, etc.), energy efficiency, and importantly, enabling full-stack bug-finding across program representations.

In the next 15 years, analyses will operate on a tower of IRs: the same program will be represented at multiple simultaneous abstraction levels. 
Multiple representations will allow tailoring abstractions for the task at hand, enabling analysis currently out of reach. For example, future analyses 
will leverage high-level IRs to model high-level container datatypes (e.g. C++ vectors, maps) and summarize operations (e.g. string manipulation), all 
while connecting these improvements down to more efficiently analyzable IRs (e.g. LLVM IR) that are closer to the machine.

This future isn't vague or far off, though. In this talk, I will show how existing open-source projects (e.g. VAST, ClangIR) building off of the LLVM 
project's Multi-level Intermediate Representation (MLIR) infrastructure are bringing about the future, today. 

Presented at

 - [Qualcomm Product Security Summit 2023](https://qcbizdev.my.salesforce-sites.com/QCTConference/GenericTSEventHome?eventname=SecuritySummit)

Authored by

 - Peter Goodman
