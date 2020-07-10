# Low-level debugging with Pwndbg

This talk describes [Pwndbg](https://github.com/pwndbg/pwndbg), a plugin for GDB written in Python that helps reverse engineering and binary exploitation of ELF binaries. It shows Pwndbg features such as enhanced context display, telescope (automatic dereferencing of potential pointers), navigation helpers (such as "please break at next syscall/ret/jump"), better display of memory maps through `vmmap` command, unicorn emulation feature (to show branches that will be taken), Windbg aliases, search memory command and others.

Resources:
* [Slides](https://docs.google.com/presentation/d/1mDfA_27DtLUkOaTZ8U9kF1aJcOhpixnGD8hDrLyKR6w)
* [Video (in Polish) from Security PWNing Conference 2018](https://www.youtube.com/watch?v=LJbmWpTNtI4)

Presented at

* [Empire Hacking](https://www.empirehacking.nyc/), February 2019
* [Security PWNing Conference 2018](https://www.instytutpwn.pl/konferencja/pwning2018-eng/#:~:text=Low%20level%20debugging,Pwndbg), November 2018

Authored by

* Dominik 'disconnect3d' Czarnota
