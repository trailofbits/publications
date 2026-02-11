---
title: "PEP 740 and PyPI: Bootstrapping Provenance for the Python Ecosystem"
date: 2024-10-22
authors:
  - William Woodruff
conference:
  - SOSS Fusion 2024
resources:
  - label: Slides
    path: "slides.pdf"
---

PyPI is the official package index for the Python programming language, and one
of the largest OSS package indices, serving over 1.2 billion downloads of over
500,000 unique packages each day to millions of Python developers and hundreds
of millions of downstream users. As the cornerstone of a massive and diverse
language ecosystem, changes to PyPI's security posture (and security features
offered) represent a significant operational challenge, one shared by indices of
similar size and criticality (such as NPM, RubyGems, and Crates). This talk is
about one such change in PyPI's security posture: the creation and (ongoing)
implementation of PEP 740, or "Index support for digital attestations." This
talk will go through the details of PEP 740, how it relates to (and integrates
with) standards like Sigstore, in-toto, and SLSA, and how PyPI (and Python
packaging more broadly) is using PEP 740 to "bootstrap" strong, maintainer
digital provenance for Python packages on top of PyPI's pre-existing support for
Trusted Publishing, without the traditional downsides of key and identity
management, complex signing ceremonies, and so forth.
