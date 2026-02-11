---
title: "The Osquery Extensions Skunkworks Project"
date: 2018-06-01
authors:
  - Mike Myers
conference:
  - QueryCon 2018
resources:
  - label: Slides
    path: "The osquery Extensions Skunkworks Project.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=g46rjoP18EE
  - label: Trail of Bits osquery Extensions
    url: https://github.com/trailofbits/osquery-extensions
---

Unconventional Uses for Osquery.

Facebook created osquery with certain guiding principles: don't pry into users' data, don't change the state of the system, don't create network traffic to third parties. It was originally intended as a read-only information gatherer. For those that didn't want to play by these rules, there's the extension interface. We've begun experimenting with extensions that don't align with mainline osquery: integrating with third-party services, writable tables, host-based firewall administration, malware vaccination, and more. We shared some of our lessons-learned on the challenges of using osquery as a control interface.

Resources

* [Announcing the Trail of Bits extension repostiory](https://blog.trailofbits.com/2017/12/14/announcing-the-trail-of-bits-osquery-extension-repository/)
* [Manage Santa within osquery](https://blog.trailofbits.com/2018/05/29/manage-santa-within-osquery/)
* [Manage your fleet's firewalls with osquery](https://blog.trailofbits.com/2018/05/30/manage-your-fleets-firewalls-with-osquery/)
