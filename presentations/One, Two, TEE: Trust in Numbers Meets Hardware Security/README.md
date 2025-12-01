## One, Two, TEE: Trust in Numbers Meets Hardware Security

MPC and Trusted Execution Environments (TEEs) represent two powerful paradigms for privacy-preserving computation, each with distinct trust models and security guarantees. While MPC distributes trust across multiple parties, TEEs centralize trust in hardware-based secure enclaves. In a perfect world, MPC's cryptographic guarantees should eliminate the need for additional hardware trust assumptions. 

In practice, however, real-world deployments face implementation vulnerabilities, side-channel attacks, and operational challenges that TEEs can help mitigate. Yet this combination isn't automatically secure; TEE implementations vary in their security, known vulnerabilities exist, and incorrect attestation or verification can undermine the entire system's security guarantees.

This talk will explore the intersection of these technologies, examining how to effectively combine MPC protocols with TEE deployments. Drawing from real-world experience, the speaker will discuss best practices for securely layering these technologies and highlight common pitfalls that can completely undermine security.

Presented at

* [DeCompute 2025](https://www.decompute.org/defi-day)

Resources

* [Slides](OneTwoTEE_Decompute2025_Paul_Bottinelli.pdf)

Authors

* Paul Bottinelli
