---
title: "Finding Hidden Overflows in Go: Fuzzing Beyond the Compiler's Limits"
date: 2026-02-28
authors:
  - Kevin Valerio
conference:
  - SECCON 14 Open Conference
resources:
  - label: Slides
    path: "slides.pdf"
---

This presentation explains how Go's silent integer overflow behavior can hide bugs from fuzzers. It covers go-panikint, Trail of Bits' forked Go toolchain work that injects runtime arithmetic overflow checks during SSA conversion so fuzzing can catch these bugs as panics.
