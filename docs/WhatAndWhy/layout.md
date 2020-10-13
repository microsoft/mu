# Dependencies and Layout

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

Some of the above components come from closed-source projects (silicon vendors, IBVs, OEMs), others are open source.
Each component is supported at its own schedule with new features and bug fixes, creating a problem of stale code if
not synced up regularly. Compound the version and source problem with the sheer size: a common UEFI codebase is
typically well above 1 million LOC and only goes up from there.  

## What is a dependency

To understand the layering you must first understand the terminology.  There are two types of code assets.

  1. A definition of something.  Generally, this is defined in an accessible header file.  This is the API provided by
     some asset.  This API can be "depended" upon to provide some capability.
  2. An implementation of something.

``` mermaid
  flowchart BT
    id1["Implementation/Module <br> (Inf/C)"]
    id2["Definition/Declaration <br>(Public Header file)"]
    id1 -.-> id2
```

Example of a build time/link dependency: DxeCore in the Basecore layer depends on the TimerLib interface.  TimerLib
interface is defined in the same Basecore layer as DxeCore, so in this case a Basecore module is depending on
a Basecore interface. This is allowed. :heavy_check_mark:

``` mermaid
flowchart BT
  id1["DxeCore Module"]
  id2["TimerLib Interface"]
  id1 -.-> id2
  
```

To extend this example even more into construction details.  Often the logic of a library will be implemented in the
silicon layer.  This means the code may vary based on which silicon is used in the product but because the interface
is defined in the basecore layer this is allowed and working as designed.  The core module can be optimized
and targeted for a specific silicon implementation.  :heavy_check_mark:

``` mermaid
flowchart BT
  subgraph bc [Basecore]
    id1["DxeCore"]
    id2["TimerLib"]
    id1 -.-> id2
  end
  subgraph sl [Silicon layer]
    id3["Silicon TimerLib"]
  end
  id3 -->id2
```

An example of an unacceptable/unsustainable dependency is if the core module starts to use the silicon layer
directly. For example if a feature was introduced that used a silicon special widget in the DxeCore then
this would fail our dependency checks.  :x:

``` mermaid
flowchart BT
  subgraph bc [Basecore]
    id1["DxeCore"]
  end
  subgraph sl [Silicon layer]
    id3["Silicon Special Widget Lib<br>Implementations"]
    id4["Silicon SpecialWidgetLib"]
    id3 -->id4
  end
  id1 -. NOT ALLOWED .-> id4
```

## Architecture

Project Mu is an attempt to create a rigid layering scheme that defines the hierarchy of dependencies.  Architectural
goal kept in mind when designing this layering scheme is a controlled, limited scope, and allowed dependencies for each
module within a given layer.  It is important to know, when implementing a module, what the module is allowed to depend
on. When creating an interface, it is important to identify the correct layer for it such that all the consuming
modules are located in the layers below.

Motivation and goals of the layering scheme:

* Easy component integration
* Code reuse
* Only carry relevant code

## Dependency Block Diagram

![Block Diagram](../img/dependency_layering.png)

## File Layout

To best preserve and delineate these concepts of componentization and unidirectional dependency, we have chosen to lay
out our repository files in a structure that reinforces the same mentality.

The underlying logic of this layout is to clearly distinguish each layer from the rest. As such, the Basecore -- which
is considered foundational -- is broken out on its own, followed by the Common repos, followed by the Silicon,
followed by the Platform. As mentioned elsewhere, Project Mu makes liberal use of multiple repositories due to the
mixture of requirements in the firmware ecosystem. Some repos are split for technical reasons, some for
organizational, and some for legal. One of the goals of Project Mu is to make this seemingly complicated layout easier
to work with.

### Min Platform Example

A simple tree might look like this...

``` pre
project_mu/
├── Build/
├── Common/
│   └── ...                     # Common code optional, but probably not required
├── Conf/
├── MU_BASECORE/
├── Platform/
│   └── Sample/
│       └── MyMinPlatform       # Platform-specific build files and code
├── Silicon/
│   └── SiProvider/
│       └── REF_CODE/           # Enablement code for your architecture
├── .gitattributes
├── .gitignore
└── .gitmodules
```

Note that this file structure is likely located in a Git repository, and every "ALL CAPS" directory in this example is
a Git submodule/nested repository.

### Surface Laptop Example

For a real-world example, this is a tree that could build the Surface Laptop product, including both open- and
closed-source repositories:

``` pre
project_mu/
├── Build/
├── Common/
│   ├── MSCORE_INTERNAL/        # Proprietary code and code not yet approved for public distribution
│   ├── MU/
│   ├── MU_TIANO/
│   └── SURFACE/                # Shared code to enable common features like FrontPage
├── Conf/
├── MU_BASECORE/
├── Platform/
│   ├── Surface/
│   │   ├── SurfKbl/
│   │   │   └── Laptop/         # Surface Laptop-Specific Platform Code
│   │   └── ...
│   └── Others/
│       └── ...
├── Silicon/
│   ├── Intel/
│   │   ├── KBL/                # Intel KBL Reference Code
│   │   ├── MU/                 # Project Mu Intel Common Code
│   │   ├── MU_TIANO/           # Project Mu Intel Code from TianoCore
│   │   └── SURF_KBL/           # Surface Customizations/Overrides for KBL Ref Code
│   └── SURFACE/                # Shared code to enable common HW like ECs
├── .gitattributes
├── .gitignore
└── .gitmodules
```

Once again, the "ALL CAPS" directories are submodules.
