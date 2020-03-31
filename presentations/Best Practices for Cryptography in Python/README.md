# Best Practices for Cryptography in Python

Languages can’t always be great at everything. Part of what makes Python great also brings challenges for disciplines that need rigorous control of the way your processor executes instructions and the way memory is handled. We’ll walk through situations where Python is a wonderful fit and also ones where it is a terrible fit for cryptographic operations. When it’s good, we’ll carefully examine why that is the case. When it’s not, we’ll discuss the workarounds and mitigations that can allow its use in most cases.

This talk is targeted at any developer who has wondered whether how to best do sensitive cryptography related things (like encrypting a file, deriving a key, creating secrets, and much, much more) in Python.

Presented at:

* [PyCon AU 2019](https://2019.pycon-au.org/)

Author:

* Paul Kehrer
