---
title: "Trusted Publishing: Lessons from PyPI"
date: 2023-10-26
authors:
  - William Woodruff
conference:
  - PackagingCon 2023
resources:
  - label: Slides
    path: "Trusted Publishing: Lessons from PyPI.pdf"
---

This talk provides a developer-minded introduction to trusted publishing, an OpenID Connect-based authentication scheme that PyPI has successfully deployed to reduce the need for and risk associated with manually configured API tokens. Thousands of packages have already enrolled in trusted publishing, improving the overall security posture of the Python ecosystem. The talk covers the high-level scheme and its security properties, then dives into the implementation details on PyPI including challenges with OIDC, threat model considerations, and knock-on benefits such as integration with Sigstore.
