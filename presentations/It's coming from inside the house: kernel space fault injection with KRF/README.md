It's coming from inside the house: kernel space fault injection with KRF
========================================================================

Fault injection (FI) has become an increasingly popular software testing method, with major
players like Netflix, Microsoft, and Google using automated failures to test the end-to-end
resiliency of their (geographically, functionally) distributed services.

In this talk, William Woodruff presents a lower-level, vulnerability-first approach: by randomly
inducing errors in the system calls made by (targeted) programs, fault injection can be used to
discover incorrect and potentially dangerous assumptions. This talk will cover specific classes of
dangerous assumptions and their potential for exploitation, all motivated by KRF, a kernelspace
fault injector open-sourced by Trail of Bits.

Presented at:

* [Linux Security Summit](https://events.linuxfoundation.org/events/linux-security-summit-north-america-2019/), August 2019

Authored by:

* William Woodruff
