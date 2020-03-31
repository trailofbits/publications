# Seriously, stop using RSA

RSA is an intrinsically fragile cryptosystem containing countless foot-guns which the average software engineer cannot be expected to avoid. Weak parameters can be difficult, if not impossible, to check, and its poor performance compels developers to take risky shortcuts. Even worse, padding oracle attacks remain rampant 20 years after they were discovered. While it may be theoretically possible to implement RSA correctly, decades of devastating attacks have proven that such a feat may be unachievable in practice.

Resources

* [Blog post](https://blog.trailofbits.com/2019/07/08/fuck-rsa/)

Presented at

* [Summercon 2019](https://www.youtube.com/watch?v=lElHzac8DDI)
* [Empire Hacking, June 2019]

Authored by

* Ben Perez
