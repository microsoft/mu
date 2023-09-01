# Project Mu and Rust

## Overview

Firmware and UEFI firmware in particular has long been written in C. Firmware operates in a unique environment to other
system software. It is written to bootstrap a system often at the host CPU reset vector and as part of a chain of
trust established by a hardware rooted immutable root of trust. Modern PC firmware is extraordinarily complex with
little room for error.

From a functional perspective, firmware must initialize the operating environment of a device. To do so involves
integrating vendor code for dedicated microcontrollers, security engines, individual peripherals, SOC initialization,
and so on. Individual firmware blobs may be located on a number of non-volatile media with very limited capacity. The
firmware must perform its functional tasks successfully or risk difficult to diagnose errors in higher levels of the
software stack that may impede overall device usability and debuggability.

From a security perspective, firmware is an important component in the overall system Trusted Computing Base (TCB).
Fundamental security features taken for granted in later system software such as kernels and hypervisors are often
based on secure establishment in a lower layer of firmware. At the root is a concept of "trust".

While operating systems are attractive targets due to their ubiquity across devices and scale, attackers are
beginning to shift more focus to firmware as an attack surface in response to increasingly effective security measures
being applied in modern operating systems. Securing the early boot process revolves around key inflection points and
protections applied between those points. The earliest point is the device "root of trust", where the system needs to
ensure it begins operating in a trusted state. This is often performed by code in immutable ROMs located in a SOC.
Since size is extremely limited, this logic typically hands off quickly to code of larger size on some mutable storage
such as SPI flash that is first verified by a key stored in the SOC. In general, this handoff process continues
throughout the boot process as hardware capabilities come online enabling larger and more complex code to be loaded
forming what is referred to as a "chain of trust". Eventually some code must execute on the host CPU, that code is
often UEFI based firmware. While significant research has been devoted across the entire boot process, UEFI firmware
on the host CPU presents a unique opportunity to gain more visibility into early code execution details and intercept
the boot process before essential activities take place such as application of important security register locks,
cache/memory/DMA protections, isolated memory regions, etc. The result is code executed in this timeframe must carry
forward proper verification and measurement of future code while also ensuring it does not introduce a vulnerability
in its own execution.

From a performance perspective, firmware code is often expected to execute exceedingly fast. The ultimate goal is for
an end user to not even be aware such code is present. In a consumer device scenario, a user expects to press a power
button and immediately receive confirmation their system is working properly. At the minimum, a logo is often shown to
assure the user something happened and they will be able to interact with the system soon. In a server scenario,
fleet uptime is paramount. Poorly written firmware can lead to long boot times that impact virtual machine
responsiveness and workload scaling or, even worse, Denial of Service if the system fails to boot entirely. In an
embedded scenario, government regulations may require firmware to execute fast enough to show a backup camera within a
fixed amount of time.

All of this is to illustrate that firmware must perform important work in a diverse set of hardware states with code
that is as small as possible and do so quickly and securely. In order to transition implementation spanning millions of
lines of code written in a language developed over 50 years ago requires a unique and compelling alternative.

## Rust and Firmware

As previously stated, modern PC firmware necessitates a powerful language that can support low-level programming with
maximum performance, reliability, and safety. While C has provided the flexibility needed to implement relatively
efficient firmware code, it has failed to prevent recurring problems around memory safety.

Common pitfalls in C such as null pointer dereferences, buffer and stack overflows, and pointer mismanagement continue
to be at the root of high impact firmware vulnerabilities. These issues are especially impactful if they compromise
the system TCB. Rust is compelling for UEFI firmware development because it is designed around strong memory safety
without the usual overhead of a garbage collector. In addition, it enforces stringent type safety and concurrency rules
that prevent the types of issues that often lead to subtle bugs in low-level software development.

Languages aside, UEFI firmware has greatly fallen behind other system software in its adoption of basic memory
vulnerability mitigation techniques. For example, data execution protection, heap and stack guards, stack cookies,
and null pointer dereference detection is not present in the vast majority of UEFI firmware today. More advanced
(but long time) techniques such as Address Space Layout Randomization (ASLR), forward-edge control flow integrity
technologies such as x86 Control Flow Enforcement (CET) Indirect Branch Tracking (IBT) or Arm Branch Target
Identification (BTI) instructions, structured exception handling, and similar technologies are completely absent in
most UEFI firmware today. This of course exacerbates errors commonly made as a result of poor language safety.

Given firmware code also runs in contexts with high privilege level such as System Management Mode (SMM) in x86,
implementation errors can be elevated by attackers to gain further control over the system and subvert other
protections.

However, the Rust ecosystem brings more than just safety. As a modern language firmware development can now participate
in concepts and communities typically closed to firmware developers. For example:

- Higher level multi-paradigm programming concepts such as those borrowed from functional programming in addition to
  productive polymorphism features such as generics and traits.

- Safety guarantees that prevent errors and reduce the need for a myriad of static analysis tools with flexibility to
  still work around restrictions when needed in an organized and well understood way (unsafe code).

- An official package management system with useful tools such as first-class formatters and linters that reduce
  project-specific implementations and focus discussion on functional code changes.

- High quality reusable bundles of code in the form of crates that increase development velocity and engagement with
  other domain experts.

- Useful compilation messages and excellent documentation that can assist during code development.

Rust's interoperability with C code is also useful. This enables a phased adoption pathway where codebases can start
incorporating Rust while still relying upon its extensive pre-existing code. At the same time, Rust has been conscious
of low-level needs and can precisely structure data for C compatibility.

## Rust and Project Mu

At this time, Project Mu has started its Rust journey by including support for Rust code within the build system used
for firmware code. This allows Rust code to naturally be included in the compilation and firmware packaging process.
More details about build support in particular is covered in the
[Project Mu Rust Build](https://github.com/microsoft/mu_basecore/blob/HEAD/Docs/rust_build.md) readme.

Setting up a fully functional pre-Rust firmware development environment can be tedious. The Rust toolchain is another
dependency that must be accounted for now. To ease the setup process, everything needed to get started has been
integrated into a [container](https://github.com/microsoft/mu_devops/pkgs/container/mu_devops%2Fubuntu-22-dev) in the
[Project Mu developer operations repo](https://github.com/microsoft/mu_devops). As Rust code is being rolled out to
Project Mu repos, they are being hooked into the common Rust infrastructure defined in the Mu DevOps repo.

Project Mu plans to participate within the open Rust development community by leveraging and contributing back to
popular crates and publishing new crates that may be useful to other projects. A general design strategy is to solve
common problems in a generic crate that can be shared and then integrate it back into firmware. In particular, UEFI
specific crates such as [r-efi](https://docs.rs/r-efi/latest/r_efi/) have already been helpful during early
development.

[QEMU](https://www.qemu.org/) is an open-source virtual machine emulator. Project Mu implements open-source firmware
for the [QEMU Q35 platform](https://wiki.qemu.org/Features/Q35) in its [Mu Tiano Platforms repository](https://github.com/microsoft/mu_tiano_platforms).
This open virtual platform is used as an easily accessible demonstration vehicle for Project Mu features. In this case,
UEFI (DXE) modules are already included in the platform firmware to demonstrate their functionality (and test it in CI).

Looking forward, we're continuing to expand the coverage of our firmware code written in Rust. We are excited to
continue learning more about Rust in collaboration with the community and our partners.
