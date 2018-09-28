# Layout

## Dependency Block Diagram

![Block Diagram](../img/dependency-layering.png)

## File Layout

To best preserve and delineate these concepts of componentization and unidirectional dependency, we have chosen to lay out our repository files in a structure that reinforces the same mentality.

The underlying logic of this layout is to clearly distinguish each layer from the rest. As such, the Basecore -- which is considered foundational -- is broken out on its own, followed by the Common repos, followed by the Silicon, followed by the Platform. As mentioned elsewhere, Project Mu makes liberal use of multiple repositories due to the mixture of requirements in the firmware ecosystem. Some repos are split for technical reasons, some for organizational, and some for legal. One of the goals of Project Mu is to make this seemingly complicated layout easier to work with.

### Min Platform Example

A simple tree might look like this...

```
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
├── .gitmodules
└── bootstrap_repo.py
```

Note that this file structure is likely located in a Git repository, and every "ALL CAPS" directory in this example is a Git submodule/nested repository.

### Surface Laptop Example

For a real-world example, this is a tree that could build the Surface Laptop product, including both open- and closed-source repositories:

```
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
├── .gitmodules
└── bootstrap_repo.py
```

Once again, the "ALL CAPS" directories are submodules.
