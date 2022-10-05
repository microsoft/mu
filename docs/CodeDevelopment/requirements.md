# Requirements for contributing Source Code

## Basics

1. Make sure it follows the package, repo, and codebase rules
2. Make sure it builds
3. Write a unit test for it.  Test positive cases as well as negative cases.
4. Make sure it has docs.  Even a minimal readme.md will get collected and added to the docs.
5. Make sure it has only valid characters encoded (often copy paste from Microsoft Word docs or the internet will lead
   to invalid characters)
6. Any changes made to code that originates from outside Project Mu (e.g. upstream project TianoCore, OpenSSL, etc.)
   should be surrounded with comments/tags indicating that it is a "MU_CHANGE".
    - Most of the contents of `mu_basecore`, `mu_tiano_plus`, `mu_silicon_arm_tiano`, and `mu_silicon_intel_tiano`
      fall under this requirement.
    - Example:

    ```c
    EFI_STATUS
    EFIAPI
    SomeFunction (
            VOID
            )
        {
            EFI_STATUS      Status;
            // MU_CHANGE [BEGIN] - Add new counters for Feature X
            UINTN           CounterA;
            UINTN           CounterB;
            // MU_CHANGE [END]

            Status = EFI_ABORTED;
            ...
        }
    ```

## Repositories

[Repo Philosophy](overview.md#repo-philosophy)

1. Repositories should have a clear owner
2. Repositories should have a clear target

- Cross platform/single platform
- Cross architecture/single architecture
- Cross organization/single organization

3. Repositories should have a consistent license (open source or proprietary)
4. Repositories should have a well defined

- CI process
- Build/Test process
- Release process

5. Repositories should provide documentation for working with the repository
6. Repositories _must_ not violate the intellectual property of others

## Uefi Packages

1. Packages are the sharing granular in Project Mu
2. Packages should be for a feature/feature set
3. Packages should enable all CI features
4. Packages should contain a host-based unit test Dsc
5. Packages should contain a compile test Dsc that includes all INF files
6. Packages should minimize dependencies
7. Package documentation should reside in the same package (Docs folder)

- Documentation should describe dependencies
- Documentation should describe integration steps
- Documentation should describe abstraction points and package usage

## Uefi Components

1. All new modules must be listed in their containing package Dsc in the components section
2. All modules must follow the dependency rules of their containing package
3. All modules within common layers should avoid silicon or architecture dependencies.
    - Use existing libraries and functionality when possible
    - Build out minimal required abstraction to allow other silicon or architectures to leverage common capabilities
4. All modules should consider testability as part of their design.
    - It is highly recommended to write a unit test for each module in the design

## Public Header files

1. Don't include other header files
2. Don't mix public and private information in the same header file
    - Implementation details should never be in a public header file
3. Use "doxygen" style function header comments to clearly specify parameters and return results.
4. Use a guidgen tool to define any guids
5. For libraries:
    - Library class should be listed in Package DEC file
    - A NULL instance must be created that allows compiling and linking with minimal dependencies.

## Library Instance

1. The supported module types in the INFs must be accurate.

    ``` inf
    LIBRARY_CLASS: <Library Class Name>|<Module types supported by this instance>
    ```

2. Use STATIC on each non-public function and non-public global to avoid conflicts with other modules.
3. Use EFIAPI on all public library class functions.

## Source files

Source files should follow the Edk2 coding standards available on [TianoCore.org](https://www.tianocore.org/) website.  

Please include the appropriate copyright messages in the file headers.
Please include the appropiate Spdx License Identifier(s) in the file headers. (<https://spdx.org/licenses/>)

## More info

For general Edk2 and UEFI development additional information can be found at the
[TianoCore.org](https://www.tianocore.org/) website.
