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

Code signing is coming to the Python packaging ecosystem in the form of Sigstore. Individual package maintainers and users will be able to sign for and verify the authenticity of their Python packages without the historical and technical baggage of PGP. This talk introduces Sigstore and its security model to Python developers, provides a technical overview of ongoing efforts to integrate Sigstore into Python packaging, and covers the cryptographic fundamentals of codesigning without long-term key material. Attendees also get a behind-the-scenes look at the standardization process and foundational efforts required to introduce a new codesigning format to one of the world's largest packaging ecosystems.
