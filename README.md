# 8Q
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![DOI](https://zenodo.org/badge/275711975.svg)](https://zenodo.org/badge/latestdoi/275711975)
Computer with built-in General Purpose 8 Qubit Optical Quantum Processor

# Contributors
[Thank you to all the contributors who make this possible](./CONTRIBUTORS.md)

# Status
The 8Q processor is currently in development
![Quantum Processor Schematic](./docs/source/imgs/qpu.png)

## Features
![Feature List](./docs/source/imgs/8q.png)

* Quad-Core Cortex-A53
* Mali-T720 MP2 GPU
* 1x DDR4 Ram Slot (Max 64GB)
* 32/64 Bit Compatible
* Linux Capable

## Files

#### Hardware Design Files

| Type                | Directory   | Filename         | Description                |
| ------------------- | ----------- | ---------------- | -------------------------- |
| Project File        | 8Q/         | 8Q.pro           | Main KiCAD Project File    |
| PCB Design File     | 8Q/         | 8Q.kicad_PCB     | Main KiCAD PCB File        |
| Board Schematic     | 8Q/         | cpu.sch          | Main CPU Schematic         |
| Board Schematic     | 8Q/         | cpu_power.sch    | CPU Power Schematic        |
| Board Schematic     | 8Q/         | RAM.sch          | CPU RAM Schemati           |
| QCore Schematic     | 8Q/         | qpu.sch          | Main QPU Schematic         |
| QCore Schematic     | 8Q/         | qpower.sch       | QPU Power Schematic        |
| QCore Schematic     | 8Q/         | preprocessor.sch | QPU Control Unit Schematic |
| Manufacturing Files | 8Q/gerber   | none             | none (gerber files)        |
| Manufacturing Files | 8Q/assembly | none             | none (assembly files)      |

#### Documentation Files

| Type              | Directory         | Filename         | Description                                |
| ----------------- | ----------------- | ---------------- | ------------------------------------------ |
| Makefile          | docs/             | Makefile         | Used to build documentation                |
| Folder            | docs/build/       | *                | Build files for docs                       |
| Folder            | docs/source/      | *                | Documentation source files                 |
| Folder            | docs/source/imgs/ | *                | Image files                                |
| ReStructured Text | docs/source/      | architecture.rst | Instruction Set Architecture Documentation |
| ReStructured Text | docs/source/      | board.rst        | Board Hardware Information                 |
| Python            | docs/source/      | conf.py          | Docs Generator Configs                     |
| ReStructured Text | docs/source/      | index.rst        | Documentation Home Page                    |
| ReStructured Text | docs/source       | programming.rst  | Programming Documentation                  |

#### Firmware/Software Sources

None: src/

#### Development Tools

None: tools/
