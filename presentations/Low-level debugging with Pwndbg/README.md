---
title: "Low-level debugging with Pwndbg"
date: 2019-02
authors:
  - Dominik Czarnota
conference:
  - Empire Hacking 2019
  - Security PWNing Conference 2018
resources:
  - label: Slides
    url: https://docs.google.com/presentation/d/1mDfA_27DtLUkOaTZ8U9kF1aJcOhpixnGD8hDrLyKR6w
  - label: Recording (Security PWNing Conference, Polish)
    url: https://www.youtube.com/watch?v=LJbmWpTNtI4
---

This talk describes Pwndbg, a plugin for GDB written in Python that helps with reverse engineering and binary exploitation of ELF binaries. It shows Pwndbg features such as enhanced context display, telescope (automatic dereferencing of potential pointers), navigation helpers (such as "break at next syscall/ret/jump"), better display of memory maps through the `vmmap` command, unicorn emulation feature (to show branches that will be taken), Windbg aliases, search memory command, and others.
