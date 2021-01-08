# Safely integrating with ERC20 tokens

DeFi smart contracts are financial applications that interact with arbitrary ERC20 tokens. Many risks associated with these interactions are not well-known and can lead to severe security issues. The goal of this presentation is to increase awareness of these risks and present guidelines to follow.

Takeaways
* Interacting with external ERC20 tokens come with risks
* The [token integration checklist](https://github.com/crytic/building-secure-contracts/blob/master/development-guidelines/token_integration.md) will help you to evaluate these risks
* [Slither's printers](https://github.com/crytic/slither/wiki/Printer-documentation#human-summary), [slither-check-erc](https://github.com/crytic/slither/wiki/ERC-Conformance), and [slither-prop](https://github.com/crytic/slither/wiki/Property-generation) will help you to review external contracts

Presented at

* [Hello Security 2021](https://www.crowdcast.io/e/hello-security-audit)

Resources

* [Slides](safely_integrating_erc20.pdf)
* [Video](https://www.crowdcast.io/e/hello-security-audit/3)
* [Building secure contracts](https://github.com/crytic/building-secure-contracts)
* [Token integration checklist](https://github.com/crytic/building-secure-contracts/blob/master/development-guidelines/token_integration.md)

Authored by

* Josselin Feist
