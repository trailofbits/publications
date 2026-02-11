---
title: "Ergonomic Codesigning for the Python Ecosystem with Sigstore"
date: 2023
authors:
  - William Woodruff
conference:
  - PyCon 2023
resources:
  - label: Slides
    path: "slides.pdf"
---

Code signing is coming to the Python packaging ecosystem, in the form of
Sigstore: individual package maintainers and users will be able to sign for and
verify the authenticity of their Python packages, respectively, without the
historical and technical baggage of PGP.

This talk will serve two purposes: (1) as a introduction to Sigstore, and its
security model, to Python developers, and (2) as a technical overview of
ongoing efforts to integrate Sigstore into Python packaging.

Attendees will be introduced to the cryptographic fundamentals of codesigning,
how Sigstore accomplishes codesigning without long-term key material (a critical
downside to PGP), as well as the guarantees they can derive from strong
codesigning in the Python packaging ecosystem. They'll also be introduced to the
technical aspects of Sigstore's integration into Python packaging, including a
peek behind the scenes at the standardization process and other foundational
efforts required to introduce a new codesigning format to one of the world's
largest packaging ecosystems.
