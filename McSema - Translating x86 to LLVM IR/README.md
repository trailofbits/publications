# Static Translation of X86 Instruction Semantics to LLVM with McSema

We have developed McSema, a new framework for analyzing and transforming machine-code programs. McSema translates x86 instructions into LLVM bitcode, with a translation strategy that allows for analysis by standard compiler algorithms. We will demonstrate McSema by adding control flow integrity to existing Windows DLLs. McSema is open source, permissively licensed, and is now available for use and modification.

Resources
* [Slides](/McSema%20-%20Translating%20x86%20to%20LLVM%20IR/McSema.pdf)
* [Video](https://www.youtube.com/watch?v=nW9bE5tUVYg)
* [Source Code](https://github.com/trailofbits/mcsema)

Presented at
* [REcon 2014](https://recon.cx/2014/schedule/events/19.html)

More info
* [A Preview of McSema](https://blog.trailofbits.com/2014/06/23/a-preview-of-mcsema/)
* [Close Encounters with Symbolic Execution (Part 1)](https://blog.trailofbits.com/2014/11/25/close-encounters-with-symbolic-execution/)
* [Close Encounters with Symbolic Execution (Part 2)](https://blog.trailofbits.com/2014/12/04/close-encounters-with-symbolic-execution-part-2/)
