# 8Q
Computer with built-in General Purpose 8 Qubit Optical Quantum Processor

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

## Directory Setup
Schematic & Gerber Files:
8Q/
  Main Project File:
    8Q.pro
  PCB Design Files:
    8Q.kicad_pcb
  Schematics:
    CPU:
      cpu.sch
      cpu_power.sch
      RAM.sch
    QPU:
      8Q Core - qpu.sch
      qpower.sch
      preprocessor.sch
  Manufacturing Files (none):
    Gerber Files (none):
      gerber/
    Assembly Files (none):
      assembly/

Documentation:
docs/
  Makefile -- Builds documentation
  build/ -- Build folder for documentation (html)
  source/
    imgs/ -- Image folder
  architecture.rst -- Instruction Set Architecture Documentation
  board.rst -- Hardware Information
  conf.py -- Documentation Generator Configs
  index.rst -- Main Page
  programming.rst -- Programming Documentation

Firmware/Software Sources (none):
src/

Development Tools (none):
tools/
  
