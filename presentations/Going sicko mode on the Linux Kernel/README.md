---
title: "Going Sicko Mode on the Linux Kernel"
date: 2019-02
authors:
  - William Woodruff
conference:
  - Empire Hacking
resources:
  - label: Slides
    path: "Going sicko mode on the linux kernel.pdf"
  - label: KRF
    url: https://github.com/trailofbits/krf
---

This talk discusses the concept of faults as an abstract bug class, as well as the usage of fault injection for both software resiliency and vulnerability research purposes. It introduces KRF, a kernel-space randomized fault injector developed at Trail of Bits, as a practical example of injecting faulty syscalls into user-space programs to discover how they handle unexpected failures.
