# Smart Contract Audit Findings

Format of findings files is CSV containing:

- *type*: category of the finding
- *severity*: high - low, estimate of impact of the finding
- *difficulty*: low - high, estimate of how hard finding is to exploit (low is easier, so worse consequences)
- *static*: is the finding plausibly detectable by present or near-term future automated static analysis?
- *dynamic*: is the finding plausibly detectable by present or near-term future automated dynamic analysis, including custom properties?
- *ERC20*: is the finding related to ERC20 token semantics?
