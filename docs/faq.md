# FAQ

## Purpose/Goals

### How is this related to TianoCore

As you can probably tell, Project Mu is based on [TianoCore](https://www.tianocore.org). It represents a variant of
TianoCore that was customized within Microsoft for scaling and maintainability. It's not exactly a staging branch for
TianoCore, as there are some changes that may not have application within or meet the explicit goals of that project,
but it is a place where features and changes can be publicly featured and discussed.

### So, is this a fork

Not entirely. It is our goal to continue to treat TianoCore as a true upstream. Our release branches will always be
based on the latest stable TianoCore release, and we will always try to PR viable fixes and features into the TianoCore
project.

### What is it? Where is it going

Project Mu is a product of the Microsoft Core UEFI team and is the basis for the system firmware within a number of
Microsoft products. It will continue to be maintained to reflect the FW practices and features leveraged for the best
experience with Windows and other Microsoft products.

A secondary purpose is to engage with the community, both in TianoCore and the industry at large. We hope that Project
Mu serves as a concrete example for discussing different approaches to managing the challenges faced by the UEFI
ecosystem.

## Content/Structure

### Is this really following "Less is More"

Yes.  The idea is lowering the entanglement of code, lowering the coupling, and allowing the product to pick and
choose the code it needs.  This means when building any given product, you don't need all the Project Mu code.

### Why are there so many repos

Project Mu makes liberal use of multiple repositories due to the mixture of requirements in the UEFI ecosystem. Some
repos are split for technical reasons, some for organizational, and some for legal.

For details, see "Repo Philosophy" in [What and Why](WhatAndWhy/overview.md#repo-philosophy).

## Is there any stronger guidance than "Less is More"?

Since Mu is derived from Edk2, the Edk2 coding standards are a good foundation, as is the existing code in the 
TianoCore repositories. Beyond that, here are a few other musings:

#### Forgotten lessons in firmware
Firmware, no matter what the flavor of it, all has the same end goal: to securely boot some sort of payload. Features
have been added to firmware over multiple years, but not all of the features work directly towards the goal of 
booting a payload.  The Mu repositories attempt to meet the goals of creating a secure environment for firmware.

Some of the additional responsibilities pushed into firmware have become outdated, or can be pared down.  Mu attempts 
to engage in securing the core requirements for securely booting a system.


#### Coding style will change depending on the goal
* Researchers just need code to work. 
* Platform developers may need code to only work for a single platform
* Silicon developers need code to work for a single processor architecture 

Mu is working towards code that works for multiple platforms and multiple processor architectures through good code.
What is good code? Clean code flow, minimal entanglement and follows industry standard best practices. 

Coding is a process and it gets better with the feedback of multiple developers and with being reused across projects. 


#### Public Headers vs Private Headers
There are lots of header files available in the Edk2 source trees.  Header files can be considered in two types: Public and Private.
* Public Header files are files that contain APIs (Function Library declarations, Ppi/Protocol declarations or information related)
* Private Header flies includes files that abstract Compiler Specific/Processor Specific information.

Public header file includes can be used, while private header files should be avoided. Private header files should be handled 
automatically through the public header files and build system. 

Note that the Edk2 build system will create AutoGen.h, which usually includes some of the private header files automatically.

Private Header examples
*Base.h, can use Uefi.h instead
*ProcessorBind.h, handled through AutoGen's PiDxe,h, PiPei.h, etc
*UefiBaseType.h, handled through AutoGen.h's PiDxe.h, PiPei.h, etc
