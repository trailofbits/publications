---
title: "Slither: A Static Analysis Framework for Smart Contracts"
date: 2019-03-07
authors:
  - Josselin Feist
conference:
  - EthCC 2019
resources:
  - label: Slides
    path: "2019-03-07-Slither_EthCC.pdf"
  - label: Slither
    url: https://github.com/trailofbits/slither/
---

This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts. It works by converting Solidity smart contracts into an intermediate representation called SlithIR, enabling commonly used program analysis techniques such as taint tracking. Slither has four main use cases: automated detection of vulnerabilities, improving the user's understanding of contracts, assisting code review, and automated detection of code optimizations.
