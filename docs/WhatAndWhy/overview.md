# Overview

## Project Organization

This documentation is hosted in the main repository for Project Mu, which is used as a central collection point for
community interaction and documentation. The build system and firmware code for the project is hosted in a number
of other repositories, grouped/divided by function, partner, license, and dependencies. Several of these repositories
are brought together by the build system to create a FW project, but we'll get into those details later. :grinning:

For now, an overview of the repositories and what code you'll find there...

## [Mu Basecore](https://github.com/Microsoft/mu_basecore)

This repository is considered foundational and fundamental to Project Mu. The guiding philosophy is that this code
should be one or more of the following:

* Part of the build system
* Common to any silicon architecture
* Part of the "API layer" that contains protocol and library definitions including
  * Industry Standards
  * UEFI Specifications
  * ACPI Specifications
* Part of the "PI" layer that contains driver dispatch logic, event/signaling logic, or memory management logic
  * This can also include central technologies like variable services

## [Mu Common Plus](https://github.com/Microsoft/mu_plus)

The packages found in this repository are contributed entirely by Project Mu. They should be common to all silicon
architectures and only depend on Mu Basecore. These packages provide features and functionality that are entirely
optional, but may be recommended for PC platform FW.

## [Mu Tiano Plus](https://github.com/Microsoft/mu_tiano_plus)

This repository contains only modules that were originally sourced from TianoCore. They are not essential for any
particular platform, but are likely useful to many platforms. The versions contained in this repo are modified
and/or improved to work with the rest of Project Mu.

## [Mu Feature Dfci](https://github.com/Microsoft/mu_tiano_plus/mu_feature_dfci)

This repository contains only the DFCI feature.
For more information, take a look at the [DFCI Documentation]https://microsoft.github.io/mu/dyn/mu_feature_dfci/DfciPkg/Docs/Dfci_Feature/)

## Repo Philosophy

Project Mu makes liberal use of multiple repositories due to the mixture of requirements in the UEFI ecosystem. Some
repos are split for technical reasons, some for organizational, and some for legal. Examples of this are:

* A downstream contributor wants to add a generic feature with a silicon-specific implementation. This feature would
  be leveraged by Common code. If all code were in one repository, no barriers would be in place to prevent the
  contributor from directly calling from Common code into the Silicon implementation. By forcing the API/interface to
  be published in a separate repository, we can ensure that the unidirectional dependency relationship is maintained.

* Module A and Module B both provide optional functionality. However, Module A is far more likely to be consume by a
  wide audience than Module B. To achieve "Less is More", Module A may be placed in a different repos to enable
  downstream consumers to carry as little "unused" code as possible, since it's likely they would not need Module B
  in their code tree.

* A downstream consumer is producing a product in conjunction with a vendor/partner. While most of the enabling code
  for the vendor component is open-source, a portion of it is only released under NDA. By having multiple repositories
  comprise a single workspace, the downstream consumer is able to maximize their open-source consumption (which minimizes
  forking) while maintaining the legal requirements of closed-source/proprietary partitioning.
