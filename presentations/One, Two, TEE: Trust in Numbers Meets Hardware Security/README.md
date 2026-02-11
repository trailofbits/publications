---
title: "One, Two, TEE: Trust in Numbers Meets Hardware Security"
date: 2025-09-30
authors:
  - Paul Bottinelli
conference:
  - DeCompute 2025
resources:
  - label: Slides
    path: "OneTwoTEE_Decompute2025_Paul_Bottinelli.pdf"
---

MPC and Trusted Execution Environments (TEEs) represent two powerful paradigms for privacy-preserving computation, each with distinct trust models and security guarantees. While MPC distributes trust across multiple parties, TEEs centralize trust in hardware-based secure enclaves. In a perfect world, MPC's cryptographic guarantees should eliminate the need for additional hardware trust assumptions.

In practice, however, real-world deployments face implementation vulnerabilities, side-channel attacks, and operational challenges that TEEs can help mitigate. Yet this combination isn't automatically secure; TEE implementations vary in their security, known vulnerabilities exist, and incorrect attestation or verification can undermine the entire system's security guarantees.

This talk will explore the intersection of these technologies, examining how to effectively combine MPC protocols with TEE deployments. Drawing from real-world experience, the speaker will discuss best practices for securely layering these technologies and highlight common pitfalls that can completely undermine security.
