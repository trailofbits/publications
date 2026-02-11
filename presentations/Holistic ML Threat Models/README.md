---
title: "Holistic ML Threat Models"
date: 2024
authors:
  - Adelin Travers
conference:
  - AI Village at BSidesSF 2024
  - Graph the Planet 2024
  - Tokyo AI Event 2024
resources:
  - label: Slides (BSidesSF)
    path: "BSidesSF - AI Village - Holistic ML threat models.pdf"
  - label: Slides (Graph the Planet)
    path: "Graph the planet - Holistic ML threat models.pdf"
  - label: Slides (Tokyo AI, Japanese)
    path: "Tokyo AI event_ 総合的な機械学習の脅威モデリング.pdf"
---

A common but misguided threat modeling approach for systems incorporating ML models is to augment a typical system threat model with analysis of ML model-level attacks such as prompt injections. This effectively disconnects the ML model, the underlying system, and safety/privacy requirements, ultimately setting the process up to fail by missing critical risks. This talk presents Trail of Bits' approach to holistic ML threat modeling and how it enables robust and practical control recommendations throughout the ML lifecycle that account for the full complexity of the ML tech stack.
