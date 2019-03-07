# Slither: A Static Analysis Framework for Smart Contracts
This talk presents Slither, a static analysis framework designed to provide rich information about Ethereum smart contracts. It works by converting Solidity smart contracts into an intermediate representation called SlithIR, allowing to apply commonly used program analysis techniques, such as taint tracking. The framework has four main use cases: (1) the automated detection of vulnerabilities, since it provides a set of security issue detectors ready to be used, (2) the improvement of the user’s understanding of the contracts, (3) the assistance to code review, and (4) the automated detection of code optimizations. In this talk, we see an overview of Slither, detail the design of its intermediate representation and evaluate its capacities on real-world contracts.

Takeaways

* Slither is fast and precise and will find vulnerabilities and optimizations in smart contracts.
* Slither's printers will help to review contracts.
* It has an easy-to-use Python API that allows building custom static analyses.

Presented at
* [EthCC 2019](https://ethcc.io)

Ressources

- [Slides](2019-03-07-Slither_EthCC.pdf)
- [Slither](https://github.com/trailofbits/slither/)

Authored by

* Josselin Feist
