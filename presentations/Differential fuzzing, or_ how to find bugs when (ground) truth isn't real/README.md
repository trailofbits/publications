---
title: "Differential Fuzzing, or: How to Find Bugs When (Ground) Truth Isn't Real"
date: 2020-03
authors:
  - William Woodruff
conference:
  - OSIRIS Lab
resources:
  - label: Slides
    path: "Differential fuzzing, or_ how to find bugs when (ground) truth isn't real.pdf"
---

Fuzzing is a well-understood bug finding technique, with known constraints: it requires a notion
of "ground truth" for program misbehavior, such as memory access violations, exceptions,
misuse of synchronization primitives, and so on. But many programs are written in high-level,
managed languages that either lack these sentinels or use them to report all errors, masking
"interesting" bugs. How can we find "interesting" bugs in these contexts? With differential
fuzzing!
