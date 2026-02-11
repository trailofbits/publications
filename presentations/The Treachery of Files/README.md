---
title: "The Treachery of Files"
date: 2019-12
authors:
  - Evan Sultanik
conference:
  - BSides Philly 2017
  - Empire Hacking 2019
resources:
  - label: Slides (BSides Philly 2017)
    path: "File Polyglottery BSides Philly 2017.pdf"
  - label: Slides (Empire Hacking 2019)
    path: "The Treachery of Files Empire Hacking 2019.pdf"
  - label: Recording (BSides Philly 2017)
    url: https://www.youtube.com/watch?v=fdKPnsWp9ho
  - label: Recording (Empire Hacking 2019)
    url: https://www.youtube.com/watch?v=LqRbfzhcI5g
  - label: Blog Post
    url: https://blog.trailofbits.com/2019/11/01/two-new-tools-that-tame-the-treachery-of-files/
  - label: PolyFile
    url: https://github.com/trailofbits/polyfile
  - label: PolyTracker
    url: https://github.com/trailofbits/polytracker
---

Parsing is hard, even when a file format is well specified. When the specification is ambiguous, it leads to unintended parser behaviors that make file formats susceptible to security vulnerabilities. This talk explores whether we could automatically generate a safe subset of any file format along with an associated verified parser, provides examples of malicious files, and introduces PolyFile and PolyTracker -- two new tools for reverse engineering files and parsers.
