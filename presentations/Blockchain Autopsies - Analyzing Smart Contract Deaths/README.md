# Blockchain Autopsies - Analyzing Ethereum Smart Contract Deaths

In the blockchain, contracts may be lost but are never forgotten. Over 1,500,000 Ethereum smart contracts have been created on the blockchain but under 7,000 unique contracts have value today. An even smaller fraction of those have source code to analyze. Old contracts have been purged from the world computer's working memory but they can be reconstructed and analyzed. When a contract's purpose is fulfilled, the owner typically triggers a self-destruct switch that removes code and state. These steps are similar to what an attacker would do after hijacking a contract. Is it likely the self-destruct was intentional or performed by a trusted third party? Or was it a hack or fraud? By investigating the transactions leading up to the termination of a binary-only contract, we can determine if there was an attack. After identifying an attacker, we can find patterns that lead to a possible motive by carefully examining their other transactions.

This presentation will introduce Ethereum smart contracts, explain how to reverse engineer binary-only contracts, describe common classes of vulnerabilities, and then show how to investigate attacks on contracts by demonstrating new tools that re-process blockchain ledger data, recreate contracts with state, and analyze suspect transactions using traces and heuristics.

Presented at

* [Black Hat USA 2018](https://www.blackhat.com/us-18/briefings.html#blockchain-autopsies-analyzing-ethereum-smart-contract-deaths)
* [Devcon 4](https://guidebook.com/guide/117233/event/21956130/)

Authored by

* Jay Little
