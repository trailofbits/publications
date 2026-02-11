---
title: "Using Graph-Based Machine Learning Algorithms for Software Analysis"
date: 2023-08
authors:
  - Michael Brown
conference:
  - ITEA Cybersecurity Workshop 2023
resources:
  - label: Slides
    path: "Using Graph-Based Machine Learning Algorithms for Software Analysis.pptx.pdf"
---

Software analysis is a well-established research area focused on automatically determining facts about a program's properties and behaviors and using them to improve the program. Software analysis techniques are used in many domains, most notably to achieve performance and security enhancements (compilers), identify bugs and security vulnerabilities (code scanners), simplify programming through abstraction (DSL interpreters), and reverse engineer software. The limitations of software analysis for these purposes are well understood – in general it is impossible to collect a complete set of program facts about a particular piece of software, especially for complex software used in the DoD. As a result, many software analysis tools employ heuristics or rely on humans in the loop to make meaningful advances in the space.

The recent technological leaps forward in Machine Learning (ML) have created a unique opportunity to make advances in software analysis that were previously not possible because ML-based solutions are not bounded by the same computational constraints as traditional software analysis techniques. Further, these techniques excel at approximating and replicating human problem solving. As a result, there has been a dearth of new research on ML-based software analysis, however recently proposed techniques have fallen flat because they failed to exploit the natural shape and form of software: directed graphs.

Over the last three years, my team and I have researched and developed techniques to address several key challenges that researchers face when creating effective, graph-based ML software analysis tools. Specifically, we have developed techniques to aid researchers in generating realistic training data sets, converting software to a representation that graph-based ML algorithms can consume, and formulating real-world software analysis problems as graph recognition problems. Using these techniques, we have created two tools that outperform state of the art traditional software analysis tools: VulChecker and CORBIN. Vulchecker is a static application security testing (SAST) tool that excels at identifying fuzzy security vulnerabilities in source code. CORBIN is a system for lifting advanced mathematical constructs (formulas, lookup tables, PID controllers, etc.) from legacy binary software that powers cyber-physical systems like power generation and onboard vehicular control systems.

In this technical track session, I will first discuss the inherent challenges in using ML to create software analysis tools and how exploiting the graph-based nature of software can bring about success. Second, I will present two successful graph-based ML software analysis tools created under the DARPA AIMEE and ReMath programs: VulChecker and CORBIN. Finally, I will present a set of guiding principles and guardrails for applying ML to software based on the lessons learned from building these tools.
