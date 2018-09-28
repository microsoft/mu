# Project Organization

This documentation is hosted in the main repository for Project Mu, which is used as a central collection point for community interaction and documentation. The build system and firmware code for the project is hosted in a number of other repositories, grouped/divided by function, partner, license, and dependencies. Several of these repositories are brought together by the build system to create a FW project, but we'll get into those details later. ;)

For now, an overview of the repositories and what code you'll find there...

## [Mu Basecore](https://github.com/Microsoft/mu_basecore)

This repository is considered foundational and fundamental to Project Mu. The guiding philosophy is that this code should be one or more of the following:

* Part of the build system
* Common to any silicon architecture
* Part of the "API layer" that contains protocol and library definitions including
  * Industry Standards
  * UEFI Specifications
  * ACPI Specifications
  * Part of the "PI" layer that contains driver dispatch logic, event/signaling logic, or memory management logic
  * This can also include central technologies like variable services

## [Mu Common Plus](https://github.com/Microsoft/mu_plus)

The packages found in this repository are contributed entirely by Project Mu. They should be common to all silicon architectures and only depend on Mu Basecore. These packages provide features and functionality that are entirely optional, but may be recommended for PC platform FW.

## [Mu Tiano Plus](https://github.com/Microsoft/mu_tiano_plus)

This repository contains only modules that were originally sourced from TianoCore. They are not essential for any particular platform, but are likely useful to many platforms. The versions contained in this repo are modified and/or improved to work with the rest of Project Mu.

## Layout / Block diagram

![Block Diagram](../img/dependency-layering.png)
