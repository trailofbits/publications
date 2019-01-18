# Property testing with Echidna and Manticore for secure smart contracts

Property-based testing is an incredibly simple and powerful tool for bug discovery, but despite its efficacy, it’s almost unheard of in the smart contract development community. This talk will introduce the concept of property-based testing, discuss strategies for picking good properties and testing them thoroughly, then go into how to apply these ideas to smart contracts specifically. We’ll discuss the use of both Manticore and Echidna for testing, and look at real bugs these tools can find in production code.

Takeaways

* Unit Testing is not always sufficient: it tests one individual case at a time, and typically focuses on known cases and failure modes. Property Testing aims to cover unknown cases by specifying generic code invariants.
* Echidna is a tool for property testing smart contracts, which is extremely fast and can discover new transaction sequences that violate code properties.
* When property-based testing with such tools, you’re sure to hit some conditions that a user might have typically missed in their individual unit tests.

Presented at

* [Empire Hacking](https://blog.trailofbits.com/2018/11/19/return-of-the-blockchain-security-empire-hacking/)

Resources

* [Slides](Property-based%20testing%20of%20smart%20contracts.pdf)
* [Video](https://youtu.be/CCs_mmbxm7Q)

Authored by

* JP Smith
