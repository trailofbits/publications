---
title: "It's coming from inside the house: kernel space fault injection with KRF"
date: 2019-08
authors:
  - William Woodruff
conference:
  - Linux Security Summit 2019
  - CSAW C2 2019
resources:
  - label: Slides
    path: "Kernel space fault injection with KRF.pdf"
---

Fault injection (FI) has become an increasingly popular software testing method, with major players like Netflix, Microsoft, and Google using automated failures to test the end-to-end resiliency of their distributed services. This talk presents a lower-level, vulnerability-first approach: by randomly inducing errors in the system calls made by targeted programs, fault injection can be used to discover incorrect and potentially dangerous assumptions. The talk covers specific classes of dangerous assumptions and their potential for exploitation, all motivated by KRF, a kernelspace fault injector open-sourced by Trail of Bits.
