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

Blockchain technology and its application in smart contracts are a recent and growing topic of research. Smart contracts enforce user trust by using a consensus-based protocol. Due to their reasonably small code size, contracts are a good target for the application of formal methods. Additionally, their business-oriented logic allows to leverage property-based techniques. However, several recent large incidents have demonstrated that smart contracts are not without vulnerabilities. In this presentation, we will discuss the state of smart contracts program analysis techniques and tools. We will demonstrate their usage through real-world bugs found by (semi)-automated tools. Finally, we will highlight the current challenges and research opportunities.

Takeaways
* Blockchain brings several challenges and research opportunities for program analysis
* Fully and semi automated tools are already being used by developers and auditors
