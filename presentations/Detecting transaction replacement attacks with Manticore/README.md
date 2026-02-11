---
title: "Detecting Transaction Replacement Attacks with Manticore"
date: 2020-06
authors:
  - Sam Moelius
conference:
  - Empire Hacking
resources:
  - label: Slides
    path: "Detecting transaction replacement attacks with Manticore.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=KXq_xQFwleg
---

In a transaction displacement attack, an attacker inserts their transaction ahead of a legitimate one, to steal rewards associated with the legitimate transaction. Transaction displacement attacks can be subtle, and designing a smart contract API that avoids them is not easy. This talk will describe recent work on a displacement attack detector for Manticore, Trail of Bits' symbolic execution tool.

Sam Moelius is a security engineer at Trail of Bits.
