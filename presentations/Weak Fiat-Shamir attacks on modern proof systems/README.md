Weak Fiat-Shamir attacks on modern proof systems
================================================

Over the past decade, proof systems, and especially zero-knowledge proofs, have seen an explosion of interest from academic researchers and practitioners. The resulting modern proof systems are being widely deployed in blockchain and cryptocurrency settings. Though built using novel technical ideas, many modern proof systems share a key ingredient with classic schemes: the Fiat-Shamir (F-S) transform. F-S is a generic way to compile an interactive proof system with a public-coin verifier to a non-interactive one by hashing the prover’s messages to generate verifier’s challenges. Prior work has shown that it is surprisingly easy to implement F-S incorrectly, and that incorrect F-S breaks classic proof systems like Schnorr. However, little is known about the risk of incorrectly implementing F-S for the modern proof systems being used in practice today; since more proof systems that use F-S are being deployed than ever before, it is crucial to understand whether vulnerable code exists and how it could be exploited. In this talk, we will present a broad survey of the state of the Fiat-Shamir transform in implementations of modern proof systems. Our talk’s contributions are fourfold. First, we will describe an extensive survey we conducted on implementations of the F-S transform in modern proof systems which identified dozens of incorrect implementations. For one such implementation, Incognito Chain’s Bulletproofs, the incorrect implementation could have led to untraceable theft of millions of dollars of funds. Second, we introduce novel attacks on incorrect F-S for four modern proof systems of interest: Bulletproofs, Plonk, Wesolowski’s VDF, and Spartan. We demonstrate attacks on adaptive knowledge soundness for all four protocols: for example, using the F-S transform described in the Wesolowski’s VDF paper, an attacker could claim to have performed orders of magnitude more squarings than it actually did. Third, we look at the applications in which these proof systems are used and try to understand whether these attacks are exploitable in relevant application contexts. Here the picture is more mixed: we show that the vulnerabilities are clearly exploitable in some applications, such as transactions using Plonk or Bulletproofs, but in other cases external constraints seem to prevent “lifting” soundness attacks to overlying protocols. Finally, we develop a set of clear recommendations to academic researchers and practitioners to try to ensure future implementations of proof systems use F-S correctly. This talk is based on a paper that was published at IEEE S&P ‘23, where it received a Distinguished Paper Award.

Presented at:

* [Real World Crypto](https://rwc.iacr.org/2024/program.php), 2024

Authored by:

* Jim Miller
* Opal Wright
* Quang Dao
* Paul Grubbs

[Presentation YouTube link](https://www.youtube.com/watch?v=HsqmaLszRm4)
