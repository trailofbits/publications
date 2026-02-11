---
title: "Linux Security Event Monitoring with osquery"
date: 2019
authors:
  - Alessandro Gario
conference:
  - QueryCon 2019
resources:
  - label: Slides
    path: "QueryCon 19 - Linux security event monitoring with osquery.pdf"
---

This talk introduces security event monitoring on Linux and lessons learned from attempts to implement it within osquery. The first experience with osquery event monitoring was rewriting its use of the Audit subsystem. In order to capture events within containers, an event publisher based on eBPF was implemented next. The talk covers what works, what doesn't, and some paths forward.
