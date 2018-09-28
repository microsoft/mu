# Block Diagram

![Block Diagram](../img/dependency-layering.png)

# File Layout

To best preserve and delineate these concepts of componentization and unidirectional dependency, we have chosen to lay out our repository files in a structure that reinforces the same mentality.

The underlying logic of this layout is to clearly distinguish each layer from the rest. As such, the Basecore -- which is considered foundational -- is broken out on its own, followed by the Common repos, followed by the Silicon, followed by the Platform. As mentioned elsewhere, Project Mu makes liberal use of multiple repositories due to the mixture of requirements in the firmware ecosystem. Some repos are split for technical reasons, some for organizational, and some for legal. One of the goals of Project Mu is to make this seemingly complicated layout easier to work with.

**_Add graphics and more details..._**
