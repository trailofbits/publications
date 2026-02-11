---
title: "Insecure Things to Avoid in Python"
date: 2018
authors:
  - Dominik Czarnota
conference:
  - PyCon PL 2018
  - Noc Informatyka 1.1
resources:
  - label: Slides
    url: https://docs.google.com/presentation/d/1LTIuStnvlKvkyRdpFmXrJ6-fxYE0roU_gHJ-83nk0zU
---

This talk describes various things in Python that, if used incorrectly, can lead to security risks. It shows examples of insecure serialization that can lead to remote code execution attacks, examples of how an attacker can leverage those and ways to fix it (at least for the yaml module). It also shows ways to exploit `eval` calls that were attempted to be sandboxed and describes `pwnlib.safeeval` that can be used to evaluate expressions in a secure fashion. Finally, it describes a Python reversing challenge from the Python Challenges competition hosted at PyCon PL.
