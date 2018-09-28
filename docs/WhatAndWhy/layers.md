## Conceptual Layers

A modern, full-featured, product-ready UEFI firmware codebase combines code from a multitude of sources:

* TianoCore EDK2 UEFI standard-based code  
* Value-add code from TianoCore
* Silicon vendor hardware initialization code
* Silicon vendor value-add code
* Independent BIOS Vendor code
* ODM/OEM customization code
* OS firmware support code
* Legacy BIOS compatibility code
* Board-specific code
* etc.

Some of the above components come from closed-source projects (silicon vendors, IBVs, OEMs), others are open source.  Each component is supported at its own schedule with new features and bugfixes, creating a problem of stale code if not synced up regularly. Compound the version and source problem with the sheer size: a common UEFI codebase is typically well above 1 million LOC and only goes up from there.  

## What is a dependency

To understand the layering you must first understand the terminology.  There are two types of code assets.  

  1. A definition of something.  Generally, this is defined in an accessible header file.  This is the API provided by some asset.  This API can be "depended" upon to provide some capability.
  2. An implementation of something.

<center>![Dependency](../img/dependency.png)</center>

Example of a dependency: DxeCore in the Basecore layer includes a TimerLib interface.  TimerLib interface is defined in the same Basecore layer as DxeCore, so in this case a Basecore module is depending on a Basecore interface. This is allowed.

Another example: Silicon-layer module implements a TimerLib interface defined in Basecore.  Here, a Silicon layer module depends on a Basecore interface. This is allowed.

## Architecture

Project Mu is an attempt to create a rigid layering scheme that defines the hierarchy of dependencies.  Architectural goal kept in mind when designing this layering scheme is a controlled, limited scope, and allowed dependecies for each module within a given layer.  It is important to know, when implementing a module, what the module is allowed to depend on. When creating an interface, it is important to identify the correct layer for it such that all the consuming modules are located in the layers below.

Motivation and goals of the layering scheme:

* Easy component integration
* Code reuse
* Only carry relevant code
