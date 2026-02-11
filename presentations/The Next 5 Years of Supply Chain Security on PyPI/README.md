---
title: "The Next 5 Years of Supply Chain Security on PyPI"
date: 2024-11-12
authors:
  - William Woodruff
conference:
  - SigstoreCon 2024
resources:
  - label: Slides
    path: "slides.pdf"
---

Over the last 5 years, PyPI has adopted a large number of technologies and
standards aimed at improving the integrity of the Python packaging ecosystem:
scoped API tokens, security events, strong MFA, Trusted Publishing, and (most
recently) PEP 740 for cryptographic package attestations.

This talk hypothesizes
and breaks down the next 5 years of changes, ranging from immediately practical
efforts to "big picture" ideas. Some ideas considered include (but are not
limited to):

* Index-wide binary transparency in the style of Go's sumdb, along with
  considerations for identity (i.e. package identity) monitoring by upstreams;
* "Counter" attestations in the vein of PEP 740, enabling auditors and
  interested community members to cryptographically register their trust in a
  PyPI package;
* Scalable witnessing and monitoring for PEP 740 attestations, including rollup
  techniques for reducing the burden of integration for pure-Python package
  installers like `pip`;
* TOFU-style identity locking via lockfiles, including (potentially) Python's
  PEP 751;
* Using TUF to distribute complex identity policies.
