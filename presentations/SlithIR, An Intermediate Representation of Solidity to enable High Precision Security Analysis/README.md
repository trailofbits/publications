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

This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts, and details the design of its intermediate representation, SlithIR. Slither converts Solidity smart contracts into SlithIR, enabling commonly used program analysis techniques such as taint tracking. The framework supports automated vulnerability detection, improved contract understanding, code review assistance, and detection of code optimizations.
