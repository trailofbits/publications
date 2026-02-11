---
title: "Implementing X.509 path validation for Python"
date: 2024-04-02
authors:
  - William Woodruff
conference:
  - Open Source Cryptography Workshop 2024
resources:
  - label: Slides
    path: "slides.pdf"
---

Over the past year, [PyCA Cryptography](https://github.com/pyca/cryptography)
(the dominant cryptographic library for Python) has been developing an
Rust-based X.509 path validation API capable of replacing the Python
ecosystem's extensive use of OpenSSL via pyOpenSSL. This talk will serve as an
introduction to and retrospective on the work, with particular attention given
to design and testing methodologies (including the novel X.509 testvector
framework and suite developed during the implementation process).

The goal of the session is to familiarize other open source cryptographic
maintainers with the initiative, foster reuse of the components developed
(including the internal, pure-Rust path validation API), as well as spur
discussion about misuse-resistant API design and potential reuse of the
testvector suite in other X.509 path validation implementations.
