---
title: "Building a Rusty path validation library for PyCA Cryptography"
date: 2024
authors:
  - William Woodruff
conference:
  - PyCon US 2024
resources:
  - label: Slides
    path: "slides.pdf"
---

The Python ecosystem has historically relied on OpenSSL for X.509 path validation, an essential component of every secure HTTPS connection. This talk introduces a new implementation written from scratch in Rust with standards conformance as a priority, newly integrated into PyCA Cryptography. It covers implementation details, strategies for reducing complexity, technical decisions and tradeoffs in the Rust components, and the impact on millions of Python developers. Particular attention is given to the work's critical security scope and testing philosophy, including strategies for reaching perfect test coverage.
