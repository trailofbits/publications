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

This talk covers the creation and ongoing implementation of PEP 740, or "Index support for digital attestations," for PyPI. It explains how PEP 740 relates to and integrates with standards like Sigstore, in-toto, and SLSA, and how PyPI is using it to bootstrap strong, maintainer digital provenance for Python packages on top of PyPI's pre-existing support for Trusted Publishing, without the traditional downsides of key and identity management or complex signing ceremonies.
