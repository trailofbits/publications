---
title: "Seriously, stop using RSA"
date: 2019-07-07
authors:
  - Ben Perez
conference:
  - Summercon 2019
  - Empire Hacking
resources:
  - label: Slides
    path: "Seriously, stop using RSA.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=lElHzac8DDI
  - label: Blog Post
    url: https://blog.trailofbits.com/2019/07/08/fuck-rsa/
---

RSA is an intrinsically fragile cryptosystem containing countless foot-guns which the average software engineer cannot be expected to avoid. Weak parameters can be difficult, if not impossible, to check, and its poor performance compels developers to take risky shortcuts. Even worse, padding oracle attacks remain rampant 20 years after they were discovered. This talk argues that while it may be theoretically possible to implement RSA correctly, decades of devastating attacks have proven that such a feat may be unachievable in practice.
