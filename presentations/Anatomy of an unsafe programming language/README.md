---
title: "Anatomy of an unsafe programming language"
date: 2018-12-12
authors:
  - Evan Sultanik
conference:
  - Empire Hacking, December 2018
  - Philadelphia Ethereum Blockchain Meetup, July 2019
resources:
  - label: 2018 Slides
    path: "Anatomy of an Unsafe Smart Contract Programming Language (Sultanik EH 2018-12-12).pdf"
  - label: 2019 Slides
    path: "Fantastic Bugs and How to Squash Them.pdf"
  - label: 2018 Recording
    url: https://www.youtube.com/watch?v=JaUIxMJAOsA
---

This talk dissects Solidity: the most popular smart contract programming language. Various examples of its unsafe behavior are discussed, demonstrating that even an experienced, competent programmer can easily shoot themselves in the foot. These serve as a cautionary tale of how not to create a programming language and toolchain, particularly one that shall be trusted with hundreds of millions of dollars in cryptocurrency. The talk is concluded with a retrospective of how some of these issues could have been avoided, and what we can do to make smart contract development more secure moving forward.

Takeaways

* Solidity harbors many unsafe features that allow even experienced, competent programmers to easily shoot themselves in the foot.
* Solidity is changing quickly, which is both bad and good. Developers must keep pace with new compiler releases and beware the implications of contract upgradability.
* There is an effort to introduce an intermediate representation to the compiler. Early indications suggest that it suffers from many of the same design decisions that have plagued Solidity.

An updated version of this talk was titled *Fantastic Bugs and How to Squash Them; or, the Crimes of Solidity* and included a menagerie of common mistakes, as well as the deeply insidious idiosyncrasies that can trip up even the most seasoned developer. It concludes with a brief survey of open-source tools you can use to help you write secure smart contracts.

Evan Sultanik is a security engineer from Trail of Bits.
