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

End-to-end signing and verification is one of the hardest technical and social
challenges in open source packaging: it rests at the fault lines of error- and
misuse-prone cryptography, long-term secret management, and identity/trust
bootstrapping. These challenges have stymied past attempts to do large-scale
end-user signing in the Python ecosystem, including PyPI's former (now disabled)
support for PGP signature uploads.

Over the past year, PyPI has designed, developed, and deployed a new approach to
package signing, one that aims to break the iron triangle of end-user signing:
digital attestations, as standardized in PEP 740.

This talk will cover the architectural details of attestations, how attestations
were implemented on PyPI and on the client (uploading side), their security
properties (including transparency) and advantages, as well as how PyPI was able
to enable signing by default for a large swath of the ecosystem without
requiring maintainers to change anything about their packaging processes. The
talk will also cover the future of attestations, including pieces of the puzzle
that are currently missing (like large-scale verification of attestations by
parties other than PyPI itself).

The audience is expected to have an intermediate familiarity with Python
packaging, including PyPI. No specific familiarity with cryptography is
required. Audience members will leave the talk with an improved understanding of
the challenges latent in end-user signing, how PEP 740's design and PyPI's
implementation overcome those challenges, and how they can both produce and
consume attestations today.
