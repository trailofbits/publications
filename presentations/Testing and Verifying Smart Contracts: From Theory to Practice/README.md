---
title: "Testing and Verifying Smart Contracts: From Theory to Practice"
date: 2021
authors:
  - Josselin Feist
conference:
  - Formal Methods for Computer Security 2021
resources:
  - label: Slides
    path: "testing_and_verifying_smart_contracts.pdf"
  - label: Slither
    url: https://github.com/crytic/slither
  - label: Echidna
    url: https://github.com/crytic/echidna
  - label: Manticore
    url: https://github.com/trailofbits/manticore
---

Smart contracts enforce user trust by using a consensus-based protocol. Due to their reasonably small code size, contracts are a good target for the application of formal methods, and their business-oriented logic allows leveraging property-based techniques. This presentation discusses the state of smart contract program analysis techniques and tools, demonstrates their usage through real-world bugs found by semi-automated tools, and highlights current challenges and research opportunities.
