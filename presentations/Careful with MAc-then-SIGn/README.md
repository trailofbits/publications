---
title: "Careful with MAc-then-SIGn: A Computational Analysis of the EDHOC Lightweight Authenticated Key Exchange Protocol"
date: 2023
authors:
  - Marc Ilunga
conference:
  - Euro S&P 2023
resources:
  - label: Slides
    path: "128_Careful_with_MAC_then_SIGn.pdf"
  - label: Paper
    url: https://eprint.iacr.org/2022/1705
---

EDHOC is a lightweight authenticated key exchange protocol for IoT communication being standardized by the IETF. Its design trims down protocols like TLS 1.3, building on the SIGMA rationale, but deviates by using short, non-unique credential identifiers with trial verification. This presentation covers a formal analysis showing that EDHOC draft version 17 achieves session key security and user authentication even when adversaries can register malicious keys with colliding identifiers, given that the signature scheme provides exclusive ownership. The work confirms cryptographic improvements integrated by the IETF working group based on recommendations from this and related analyses.
