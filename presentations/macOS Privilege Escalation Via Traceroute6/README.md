---
title: "macOS Privilege Escalation via Traceroute6"
date: 2025-10-15
authors:
  - Paweł Płatek
conference:
  - Objective by the Sea v8.0
resources:
  - label: Slides
    path: "macos-privilege-escalation-via-traceroute6.pdf"
  - label: Recording
    url: https://www.youtube.com/watch?v=fhkH0Cad96g
---

How hard is it to get a root shell on a modern macOS system? Is old-school SUID binary exploitation still viable? This talk presents a user-to-root local privilege escalation exploit against macOS, chaining four vulnerabilities in mDNSResponder, traceroute6, and libinfo: local DNS traffic interception, incorrect privilege dropping, ASLR bypass, and an integer overflow. The talk dives into macOS' local DNS architecture, explores libmalloc from an exploit development perspective highlighting differences between Intel and Apple Silicon architectures, and assesses and bypasses the Pointer Authentication Codes (PAC) mitigation to obtain root.
