# Project Mu
This repository documents Project Mu.  

Start here: https://microsoft.github.io/mu/ 

[![Build status](https://dev.azure.com/projectmu/mu/_apis/build/status/Publish%20Mu)](https://dev.azure.com/projectmu/mu/_build/latest?definitionId=3)

## Overview
Project Mu is a modular adaptation of TianoCore's edk2 tuned for building modern devices using a scalable, maintainable, and reusable pattern. Mu is built around the idea that shipping and maintaining a UEFI product is an ongoing collaboration between numerous partners. For too long the industry has built products using a "forking" model combined with copy/paste/rename and with each new product the maintenance burden grows to such a level that updates are near impossible due to cost and risk.

Project Mu also tries to address the complex business relationships and legal challenges facing partners today. To build most products it often requires both closed-source, proprietary assets as well as open source and industry standard code. The distributed build system and multi-repository design allow product teams to keep code separate and connected to their original source while respecting legal and business boundaries.

Project Mu originated from building modern Windows PCs but its patterns and design allow it to be scaled down or up for whatever the final product's intent. IoT, Server, PC, or any other form factor should be able to leverage the content.

## Primary Goals
### 1. Share our active code tree to both solicit feedback and entice partners to collaborate
Project Mu is an active project. This is not a side project, mirror, clone, or example. This is the same code used today on many of Microsoft's 1st party devices and it will be kept current because it must be to continue to enable shipping products.

### 2. Promote, evangelize, and support an industry shift to a more collaborative environment so we all can build and maintain products with lower costs and higher quality
Today's open source projects although extremely valuable are very resource intensive to interact with. This friction leads to major industry players avoiding public interaction thus diminishing the overall community’s value. The modern era of open source projects has incorporated new tools and procedures to lower this friction and it is our goal to leverage those tools. GitHub provides issue tracking, Pull Requests, Gated builds, tracked/required web-based code reviews, and CI/CD (Continuous builds and testing). It is our belief that by leveraging and extending this automation and workflow we can lower the friction and foster a safe place for all contributors to work.

