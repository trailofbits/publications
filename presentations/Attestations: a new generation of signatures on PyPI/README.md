---
title: "Attestations: a new generation of signatures on PyPI"
date: 2025-05-17
authors:
  - William Woodruff
conference:
  - PyCon US 2025
resources:
  - label: Slides
    path: "slides.pdf"
---

End-to-end signing and verification is one of the hardest technical and social challenges in open source packaging. Over the past year, PyPI has designed, developed, and deployed a new approach to package signing: digital attestations, as standardized in PEP 740. This talk covers the architectural details of attestations, how they were implemented on PyPI and on the client side, their security properties including transparency, and how PyPI enabled signing by default for a large portion of the ecosystem without requiring maintainers to change their packaging processes.
