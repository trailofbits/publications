# Contract upgrade risks and remediations

A popular trend in smart contract design is to promote the development of upgradable contracts. Existing techniques to upgrade contracts have flaws, increase the complexity of the contract significantly, and ultimately introduce bugs. We will detail our analysis of existing smart contract upgrade strategies, describe the weaknesses we have observed in practice, and provide recommendations for contracts that require upgrades.

Takeaways
* Upgradability is useful for developers as it allows for features to be added and bugs to be fixed after the fact. However, it also adds complexity and increases the likelihood of deployment mistakes.
* Use the simplest upgrade system that suits your needs. Compared to data separation, the delegatecall proxy pattern is very fragile and adds even more complexity.
* Instead of these upgradability patterns, consider contract migration. Migration is more involved, but it allows for recovery from many more scenarios.

Josselin Feist is a security engineer at Trail of Bits.

Presented at

* [Empire Hacking](https://blog.trailofbits.com/2018/11/19/return-of-the-blockchain-security-empire-hacking/)

Resources

* [Slides](contract_upgrades.pdf)
* [Video](https://www.youtube.com/watch?v=mebA5Qz9zeQ)
* [Contract upgrade anti-patterns](https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/)
* [How contract migration works](https://blog.trailofbits.com/2018/10/29/how-contract-migration-works/)

Authored by

* Josselin Feist
