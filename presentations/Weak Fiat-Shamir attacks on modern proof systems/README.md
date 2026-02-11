---
title: "Weak Fiat-Shamir Attacks on Modern Proof Systems"
date: 2024-03-25
authors:
  - Jim Miller
  - Opal Wright
  - Quang Dao
  - Paul Grubbs
conference:
  - Real World Crypto 2024
resources:
  - label: Slides
    path: "45m talk (Cornell) - Weak Fiat-Shamir Attacks on Modern Proof Systems with Decree slides.key"
  - label: Recording
    url: https://www.youtube.com/watch?v=HsqmaLszRm4
  - label: Paper
    url: https://eprint.iacr.org/2023/691
---

Over the past decade, proof systems and especially zero-knowledge proofs have seen an explosion of interest. Many modern proof systems share a key ingredient: the Fiat-Shamir transform. This talk presents a broad survey of F-S implementations in modern proof systems, identifying dozens of incorrect implementations. It introduces novel attacks on incorrect F-S for Bulletproofs, Plonk, Wesolowski's VDF, and Spartan, and develops recommendations to ensure future implementations use F-S correctly. Based on a paper that received a Distinguished Paper Award at IEEE S&P '23.
