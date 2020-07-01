# Python internals - let's talk about dicts

This talk shows some corners of Python dictionary data structure. It discusses quirks with dictionary keys hashing, flaws of overriding dicts and how to do it properly, shows a `__missing__` magic method example and ways to update dict without overriding its keys. It also explains issues regarding hashing of mutable values.


Resources:
* [Slides](https://docs.google.com/presentation/d/1jVhSF_YnR-z0_1ftsQWjluYZxiaq2xDX3kSouDbccP8)
* [Video from Pykonik Tech Talks #43](https://www.youtube.com/watch?v=KOVgbnGvGTg)

Presented at

* [PyConPL 2019](https://pl.pycon.org/2019/en/agenda/#:~:text=Dominik,dicts), September 2019
* [Pykonik Tech Talks #43](https://www.pykonik.org/tech-talks/43/), March 2019


Authored by

* Dominik 'disconnect3d' Czarnota
