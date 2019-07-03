## Linux Security Event Monitoring with osquery

This talk introduces security event monitoring on Linux, and our lessons learned from attempts to implement it within osquery. Our first experience with osquery event monitoring was rewriting its use of the Audit subsystem. In order to capture events within containers, we next implemented an event publisher based on eBPF. We discovered what works, what doesn’t, and some paths forward.

Presented at

* [QueryCon 2019](https://querycon.io/)

Resources

* [osquery](https://osquery.io)
* [Linux Audit](http://people.redhat.com/sgrubb/audit/)
* [eBPF](http://www.brendangregg.com/ebpf.html)

Author

* Alessandro Gario