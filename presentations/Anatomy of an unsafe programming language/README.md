# Anatomy of an unsafe smart contract programming language

This talk dissects Solidity: the most popular smart contract programming language. Various examples of its unsafe behavior are discussed, demonstrating that even an experienced, competent programmer can easily shoot themselves in the foot. These serve as a cautionary tale of how not to create a programming language and toolchain, particularly one that shall be trusted with hundreds of millions of dollars in cryptocurrency. The talk is concluded with a retrospective of how some of these issues could have been avoided, and what we can do to make smart contract development more secure moving forward.

Takeaways

* Solidity harbors many unsafe features that allow even experienced, competent programmers to easily shoot themselves in the foot.
* Solidity is changing quickly, which is both bad and good. Developers must keep pace with new compiler releases and beware the implications of contract upgradability.
* There is an effort to introduce an intermediate representation to the compiler. Early indications suggest that it suffers from many of the same design decisions that have plagued Solidity.

An updated version of this talk was titled *Fantastic Bugs and How to Squash Them; or, the Crimes of Solidity* and included a menagerie of common mistakes, as well as the deeply insidious idiosyncrasies that can trip up even the most seasoned developer. It concludes with a brief survey of open-source tools you can use to help you write secure smart contracts.

Evan Sultanik is a security engineer from Trail of Bits.

Presented at

* [Philadelphia Ethereum Blockchain Meetup, July 2019](https://www.meetup.com/Philadelphia-Ethereum-Meetup/events/262608448/)
* [Empire Hacking, December 2018](https://blog.trailofbits.com/2018/11/19/return-of-the-blockchain-security-empire-hacking/)

Resources

* [2019 Slides](Fantastic%20Bugs%20and%20How%20to%20Squash%20Them.pdf)
* [2018 Slides](Anatomy%20of%20an%20Unsafe%20Smart%20Contract%20Programming%20Language%20(Sultanik%20EH%202018-12-12).pdf)
* [2018 Video](https://www.youtube.com/watch?v=JaUIxMJAOsA)

Authored by

* Evan Sultanik
