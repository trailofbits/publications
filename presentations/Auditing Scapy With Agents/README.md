---
title: "Auditing Scapy With Agents"
date: 2026-09-16
authors:
  - Clinton Thomas
conference:
  - ScapyCon 2026
resources:
  - label: Slides
    path: "slides.pdf"
---

How eleven agent runs became 129 reports and fixes the maintainers were willing to read.

As part of Patch the Planet, an OpenAI-funded initiative run by Trail of Bits to improve the security of widely used open-source software, we audited Scapy with LLM agents over five days (Aug 24–28, 2026). Rather than repeat OSS-Fuzz's coverage, the agents targeted `scapy/contrib/**`, stream reassembly, and the automatons that reply to traffic on their own. Eleven search runs across 670 agent sessions reported 471 crashes and bugs, which deduplicated to 265 distinct bugs. Of those, 129 went to the maintainers (92 private reports, 37 pull requests); as of Sep 14, 2026, 80 patches had been merged (85% of patches) and 89% of reported issues were resolved.

The talk covers the scaffolding that made each finding prove itself before a person looked at it:

1. **Start with their scope**: the project's own definition of a security bug is the first filter. Anything outside it is recorded but not reported.
2. **Prove it with a script**: every finding ships with a reproduction that shows the failure, a negative control without the trigger, that the error escapes to the caller, and the exact environment. The same script runs against the patched tree.
3. **Adversarial review**: fresh agents with no prior context are told to disprove each finding, and every claim cites a file and line.
4. **Write it all down, review it after**: reviewing across all findings turned 26 separate short-packet bugs into a single guard in `sessions.py`.
5. **Exhaustive testing**: regression tests must fail when the fix is removed, all patches are tested together in the project's own CI, and a person runs every reproduction. Each patch also reports its performance cost, which steered agents away from lazy fixes; 15 of 41 fixes made normal traffic faster.
6. **Ask the maintainers what good looks like**: maintainer feedback became written rules that every later fix was held to.

The talk closes with what the process cannot do: define good code for a project, stop locally tidy patches from adding up to noise, or decide scope. Those remain the maintainers' calls.
