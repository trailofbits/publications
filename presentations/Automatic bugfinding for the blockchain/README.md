---
title: "Automatic bugfinding for the blockchain"
date: 2017
authors:
  - Josselin Feist
  - Felipe Manzano
conference:
  - Ekoparty 2017
resources:
  - label: Slides
    path: "abfftb.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=r0cvQhBBw1w
---

Blockchain technology and, in particular, its application in the execution of smart contracts is a recent and growing topic of research. The most prevalent platform for the development and execution of smart contracts is the Ethereum blockchain, on which several projects have already been founded, with funding of up to multiple millions of dollars.

Smart contracts enforce user trust by using a consensus-based protocol. However, several recent large hacks have demonstrated that smart contracts are not without vulnerabilities. Unfortunately, the most widely used language (Solidity) is still young and, even a subtle error in the code can lead to millions lost. Auditing and testing smart of contracts has gained popularity within the security community, yet, available toolchains are still in their infancy and developers often ignore even the most basic security recommendations.

This presentation aims to, first, present the technical aspects of the Ethereum Virtual Machine (EVM) and provide an overview of the most common bugs. Subsequently, we will discuss the design and implementation of our EVM capable dynamic symbolic execution engine -- Manticore -- which enables human-assisted analysis and the automatic detection of vulnerabilities.
