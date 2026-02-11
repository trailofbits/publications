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

This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts. It works by converting Solidity smart contracts into an intermediate representation called SlithIR, enabling program analysis techniques such as taint tracking. The framework supports automated vulnerability detection, improved contract understanding, code review assistance, and automated code optimization detection. The talk covers an overview of Slither, the design of SlithIR, and its industrial and academic impacts.
