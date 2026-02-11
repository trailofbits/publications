---
title: "Contract Upgrade Risks and Recommendations"
date: 2018-11
authors:
  - Josselin Feist
conference:
  - Empire Hacking
resources:
  - label: Slides
    path: "contract_upgrades.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=mebA5Qz9zeQ
  - label: Blog - Contract Upgrade Anti-Patterns
    url: https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/
  - label: Blog - How Contract Migration Works
    url: https://blog.trailofbits.com/2018/10/29/how-contract-migration-works/
---

A popular trend in smart contract design is to promote the development of upgradable contracts. Existing techniques to upgrade contracts have flaws, increase complexity significantly, and ultimately introduce bugs. This presentation details the analysis of existing smart contract upgrade strategies, describes weaknesses observed in practice, and provides recommendations for contracts that require upgrades. Key takeaways include favoring the simplest upgrade system for your needs, avoiding the fragile delegatecall proxy pattern when possible, and considering contract migration as an alternative to upgradability patterns.
