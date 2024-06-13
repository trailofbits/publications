Implementing X.509 path validation for Python
=============================================

The Python ecosystem has historically relied on OpenSSL (and its myriad forks) to provide an implementation of X.509 path validation, a little-known but essential component of every secure HTTPS connection made on the modern Internet. This has brought technical debt, developer frustration (due to OpenSSL's poorly documented implementation quirks), and a mottled security history.

This talk introduces an alternative, developed over the past year: a new implementation of X.509 path validation, written from the ground-up in a memory-safe language with standards conformance as a priority, newly integrated into PyCA Cryptography, Python's most popular cryptographic library. We'll cover the work's implementation details, strategies applied for reducing complexity, technical decisions and tradeoffs made in its Rust components, as well as the work's impact on the millions of Python developers that depend on PyCA Cryptography and PyCA pyOpenSSL. Particular attention will be dedicated to the work's critical security scope and accompanying testing philosophy, including developed strategies for reaching perfect test coverage and avoiding vulnerability classes that have historically afflicted X.509 path validation implementations.

The audience is expected to have an intermediate familiarity with general Python development, including a high-level familiarity with SSL/TLS and HTTPS (but not X.509 or X.509 path validation). Audience members will leave the talk with a more complete understanding of the modern Internet's security model, as well as how the Python ecosystem is maturing to accomodate modern cryptographic best practices in networked settings.

Presented at:

* [PyCon US](https://us.pycon.org/2024/schedule/presentation/49/), 2024

Authored by:

* William Woodruff
