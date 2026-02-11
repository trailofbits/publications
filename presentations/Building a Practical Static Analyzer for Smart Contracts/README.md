---
title: "Building a Practical Static Analyzer for Smart Contracts"
date: 2021-10-27
authors:
  - Josselin Feist
conference:
  - Dagstuhl Seminar on Rigorous Methods for Smart Contracts 2021
resources:
  - label: Slides
    path: "2021-10-27-dagstuhl-slither.pdf"
  - label: Slither
    url: https://github.com/crytic/slither/
---

This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts. It works by converting Solidity smart contracts into an intermediate representation called SlithIR, allowing to apply commonly used program analysis techniques, such as taint tracking. The framework has four main use cases: (1) the automated detection of vulnerabilities, since it provides a set of security issue detectors ready to be used, (2) the improvement of the user's understanding of the contracts, (3) the assistance to code review, and (4) the automated detection of code optimizations. In this talk, we see an overview of Slither, detail the design of its intermediate representation, and discuss its industrial and academic impacts.

Takeaways

* Slither is fast and precise and will find vulnerabilities and optimizations in smart contracts.
* SlithIR, the security-oriented intermediate representation, is the key component for advanced analyses.
* Researchers can leverage its Python API to build custom static analyses.
