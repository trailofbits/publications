# Insecure Things to Avoid in Python

This talk describes various things in Python that, if used incorrectly, can lead to security risks. It shows examples of insecure serialization that can lead to remote code execution attacks, examples how an attacker can leverage those and ways to fix it (at least for yaml module). It also shows ways to exploit `eval` calls that were attempted to be sandboxed and describes `pwnlib.safeeval` that can be used to evaluate expressions (and more) in a secure fashion. In the end, it describes a Python reversing challenge from Python Challenges competition hosted on PyCon PL conference.

Resources:
* [Slides](https://docs.google.com/presentation/d/1LTIuStnvlKvkyRdpFmXrJ6-fxYE0roU_gHJ-83nk0zU)

Presented at

* [PyCon PL 2018](https://pl.pycon.org/2018/agenda/#:~:text=Some%20insecure%20things%20to%20avoid%20in%20Python): an earlier but more technically deep version
* [Noc Informatyka 1.1 (2018)](https://nocinformatyka.pl/poprzednie-edycje/#:~:text=Dominik,Python): an earlier version

Authored by

* Dominik 'disconnect3d' Czarnota
