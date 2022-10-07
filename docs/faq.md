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

### What is a good philosophy for organizing my code?

Programming has had a lot written about abstractions to help make code more readable or to simplify complex disjoint
features under a common API. The same volume of literature does not exist for organizing large sets of features
for firmware.  

[Repo Philosophy](overview.md#repo-philosophy)

So how should firmware be organized? By feature? By silicon, or by author? It is difficult to document what makes
good organization.  Some simple observations are below:

1. Understand the consumer of your code
    If your code is designed to be an intermediate, then design it to be as robust as possible. If your code
    is configuring a piece of hardware, leave the "policy" decision as an input to your code, and allow external
    configuration of the policy via library or pcd.
2. Abstract silicon specific code.  
    e.g. Most platforms use SPI flash, but the mechanics of reading/writing/configuring a SPI controller are specific
    to the hardware. Move SPI controller functionality out of your feature.
3. Organizing code for reuse and configurability.
    Are you writing something to satisfy a program requirement? What portions of the code would be useful for
    reuse? Maybe those should move into a library or outside of the current package you are designing?
4. Be mindful of dependencies
    If you are writing a feature for reuse, be mindful of what dependencies you create.  Its bad practice to have
    a generic function include horizontal dependencies. e.g. If FatPkg had dependencies on ArmPkg, or OvmfPkg had
    dependencies on IntelFsp2Pkg those would be considered bad designs.

Did a bad decision get made in your code design? Refactoring may cause some temporary pain, but will be beneficial
in the long run.

Did a bad decision get made in your existing repos? The benefit of Project Mu using the [edk2-pytools-library](https://github.com/tianocore/edk2-pytool-library)
is that reorganization of repositories will have minimal effect on a project
