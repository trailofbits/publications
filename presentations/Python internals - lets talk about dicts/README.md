---
title: "Python internals - let's talk about dicts"
date: 2019-09
authors:
  - Dominik Czarnota
conference:
  - PyConPL 2019
  - Pykonik Tech Talks #43
resources:
  - label: Slides
    url: https://docs.google.com/presentation/d/1jVhSF_YnR-z0_1ftsQWjluYZxiaq2xDX3kSouDbccP8
  - label: Recording
    url: https://www.youtube.com/watch?v=KOVgbnGvGTg
---

This talk explores corners of the Python dictionary data structure. It discusses quirks with dictionary key hashing, flaws of overriding dicts and how to do it properly, demonstrates the __missing__ magic method, and shows ways to update a dict without overriding its keys. It also explains issues regarding hashing of mutable values.
