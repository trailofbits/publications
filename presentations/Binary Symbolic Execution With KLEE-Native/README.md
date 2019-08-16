# Binary Symbolic Execution with KLEE-Native

KLEE is an emulator for LLVM bitcode. Its primary use is in software testing and verification tool chains. It is an excellent tool if your goal is to produce test inputs for a target that have extremely high code coverage. It leverages symbolic execution and a custom runtime to intelligently find bugs. Unfortunately it is somewhat difficult to obtain bitcode in the real world. This talk shows how we used Remill to lift binaries into LLVM and symbolically execute the result. We also extended KLEE's syscall implementations, forking model, and heap memory model. The end result is a version of KLEE that uses eager concretization to symbolically execute binaries, reproduces CVESs, clearly models heap memory, accurately classifies heap bugs, emulates syscalls, and executes libc functions in a performant way , and in a way that productively handles symbolic data.

The presentation displays some of the higher level techniques we used to make KLEE-Native, our fork of KLEE, possible. It also shows a CVE that was accurately reproduced; the CVE was used in a ChromeOS exploit chain.

Presented at

* [August 13 Empire Hacking 2019](https://www.meetup.com/Empire-Hacking/events/262296773/)

Authored by

* Sai Vegasena
