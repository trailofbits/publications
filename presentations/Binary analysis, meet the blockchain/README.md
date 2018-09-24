# Binary analysis, meet the blockchain

Ethereum is a novel, decentralized computation platform that has quickly risen in popularity since it was introduced in 2014, and currently controls the equivalent of one hundred ten billion dollars. At its foundation is a virtual machine which executes “smart contracts”: programs that ultimately control the majority of the value transfer within the network. As with most other types of programs, correctness is very important for smart contracts. However, somewhat uniquely to Ethereum, incorrectness can have a direct financial cost, as evidenced by a variety of high profile attacks involving the loss of hundreds of millions of dollars. The error-prone nature of developing smart contracts and the increasing amounts of capital processed by them motivates the development of analysis tools to assist in automated error and vulnerability discovery.

In this talk, we describe our work towards smart contract analysis tooling for Ethereum, which focuses on a modern technique called symbolic execution. We provide context around both Ethereum and symbolic execution, and then discuss the unique technical challenges involved with combining the two, touching on topics including blockchains, constraint solvers, and virtual machine internals. Lastly, we present Manticore: an open source symbolic execution tool which we have used to enhance smart contract security audits.

Presented at

* [Northsec 2018](https://northsec.io)
* [High Confidence Software and Systems Conference 2018](https://cps-vo.org/hcss18/mossberg)

Authored by

* Mark Mossberg
