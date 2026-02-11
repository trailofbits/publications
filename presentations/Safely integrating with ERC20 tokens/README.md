---
title: "Safely integrating with ERC20 tokens"
date: 2021
authors:
  - Josselin Feist
conference:
  - Hello Security 2021
resources:
  - label: Slides
    path: "safely_integrating_erc20.pdf"
  - label: Recording
    url: https://www.crowdcast.io/e/hello-security-audit/3
  - label: Building Secure Contracts
    url: https://github.com/crytic/building-secure-contracts
  - label: Token Integration Checklist
    url: https://github.com/crytic/building-secure-contracts/blob/master/development-guidelines/token_integration.md
---

DeFi smart contracts are financial applications that interact with arbitrary ERC20 tokens. Many risks associated with these interactions are not well-known and can lead to severe security issues. This presentation increases awareness of these risks and presents guidelines to follow, including the token integration checklist, Slither's printers, slither-check-erc, and slither-prop for reviewing external contracts.
