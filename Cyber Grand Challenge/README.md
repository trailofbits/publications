# The DARPA Cyber Grand Challenge

## Empire Hacking Abstract

We built an autonomous robot to fight and destroy insecure software as part of a DARPA competition. It uses symbolic execution, fuzzing, binary translation, dynamic instrumentation, and more to identify and fix vulnerabilities without any human guidance. We will describe the high-level architecture of our system, how well it works, and difficulties we overcame during the development process.

## Infiltrate Abstract

DARPA’s Cyber Grand Challenge is a contest to automate vulnerability discovery and patching. Trail of Bits participated in the qualifying event held this past June (2015), and, well, didn’t qualify. While other teams are heads down preparing for the CGC final event (to be held on August 4th in Las Vegas), I can talk about what our team did right and what our team did wrong.

In this presentation, I’ll tell the story of our Cyber Grand Challenge adventure, explain how to automatically find and patch bugs in binary code, and discuss what’s next for our bug finding system.

The story will describe how our small team of internationally distributed engineers made an automated bug finding system that placed 2nd in vulnerability discovery. I will cover both the fun parts and the necessary-but-boring-parts of automated bug finding. Fun parts include combining existing fuzzing and symbolic execution tools into one coherent system, and making fuzzing fast by identifying and eliminating performance bottlenecks. The necessary-but-boring-parts include automated testing, deployment, and configuration management, otherwise known as devops.

Second, I’ll talk about how to patch bugs by translating binaries to LLVM bitcode, patching the bitcode, and re-emitting working patched binaries. I will cover different patching strategies and the requirements for each approach. I will also discuss instrumentation techniques, transformation operations, and analysis passes that are enabled by LLVM translation.

Finally, I will talk about how researchers should fundamentally change the way bug finding tools are developed. Currently each tools is its own discrete island. However, there are quantifiable benefits to be gained by applying the Unix philosophy of discrete, communicating tools to the problem of bug finding.

Resources
* [Video from ShakaCon](https://www.youtube.com/watch?v=pOuO5m1ljRI), July 2016
* [Slides from Infiltrate](/Cyber%20Grand%20Challenge/Dinaburg_INFILTRATE_2016.pdf), April 2016
* [Slides from Empire Hacking](/Cyber%20Grand%20Challenge/cgcempirehacking_wide.pdf), August 2015
* [mcsema](https://github.com/trailofbits/mcsema)

Presented at
* [ShakaCon](https://www.shakacon.org/making-a-scalable-automated-hacking-system-by-artem-dinaburg/), July 2016
* [NCC Group Open Forum Chicago](http://www.meetup.com/NCCGroupChicago/events/229972651/), June 2016
* [High Confidence Software and Systems (HCSS)](http://cps-vo.org/node/25057), May 2016
* [Infiltrate](http://infiltratecon.com/archives.html), April 2016
* [Empire Hacking](http://www.meetup.com/Empire-Hacking/events/223128682/), August 2015

More info
* [Dear DARPA: Challenge Accepted](http://blog.trailofbits.com/2014/06/03/dear-darpa-challenge-accepted/)
* [How We Fared in the Cyber Grand Challenge](https://blog.trailofbits.com/2015/07/15/how-we-fared-in-the-cyber-grand-challenge/)
* [Hacking for Charity: Automated Bug-finding in LibOTR](http://blog.trailofbits.com/2016/01/13/hacking-for-charity-automated-bug-finding-in-libotr/)

Team
* Artem Dinaburg
* Peter Goodman
* Felipe Manzano
* Car Bauer
* Ryan Stortz
* Andrew Ruef
