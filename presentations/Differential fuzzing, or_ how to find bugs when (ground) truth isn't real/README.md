Differential fuzzing, or: how to find bugs when (ground) truth isn't real
=========================================================================

Fuzzing is a well-understood bug finding technique, with known constraints: it requires a notion
of “ground truth” for program misbehavior, such as memory access violations, exceptions,
misuse of synchronization primitives, and so on. But many programs are written in high-level,
managed languages that either lack these sentinels or use them to report all errors, masking
“interesting” bugs. How can we find “interesting” bugs in these contexts? With differential
fuzzing!

Presented at:

* [OSIRIS Lab](https://www.osiris.cyber.nyu.edu/), March 2020

Authored by:

* William Woodruff
