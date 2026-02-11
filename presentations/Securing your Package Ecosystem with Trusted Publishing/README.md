---
title: "Securing your Package Ecosystem with Trusted Publishing"
date: 2023-10-26
authors:
  - William Woodruff
conference:
  - PackagingCon 2023
resources:
  - label: Slides
    path: "Securing your Package Ecosystem with Trusted Publishing.pdf"
---

This talk provides a developer-minded introduction to "trusted publishing," an OpenID Connect-based authentication scheme that PyPI has successfully deployed to reduce the need for and risk associated with manually configured API tokens. It covers the high-level overview of the scheme and its security properties, as well as the implementation details on PyPI, including support for multiple identity providers, threat model considerations, and knock-on benefits such as future integration with code-signing schemes like Sigstore.
