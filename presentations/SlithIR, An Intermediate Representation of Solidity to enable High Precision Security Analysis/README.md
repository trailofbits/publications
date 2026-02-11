---
title: "SlithIR, An Intermediate Representation of Solidity to enable High Precision Security Analysis"
date: 2019-04-17
authors:
  - Josselin Feist
conference:
  - RunEVM 2019
resources:
  - label: Slides
    path: "2019-04-17-SlithIR_RunEVM.pdf"
  - label: Slither
    url: https://github.com/crytic/slither/
---

This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts. It works by converting Solidity smart contracts into an intermediate representation called SlithIR, allowing to apply commonly used program analysis techniques, such as taint tracking. The framework has four main use cases: (1) the automated detection of vulnerabilities, since it provides a set of security issue detectors ready to be used, (2) the improvement of the user's understanding of the contracts, (3) the assistance to code review, and (4) the automated detection of code optimizations. In this talk, we see an overview of Slither, and detail the design of its intermediate representation.

Takeaways

* Slither is fast and precise and will find vulnerabilities and optimizations in smart contracts.
* Slither's printers will help to review contracts.
* It has an easy-to-use Python API that allows building custom static analyses.
* SlithIR, the security-oriented intermediate representation, is the key component for advanced analyses.
