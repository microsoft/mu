# How to setup a new Repo for a Platform that will use Project MU

This document will describe the base guidelines for setting up a Project MU repo.

1. You will need to install the [prerequisites tools](../CodeDevelopment/prerequisites.md)
2. Determine how to layout your project and the content
     * Look at [layout](../WhatAndWhy/layout.md) to understand our recommended repository layout.
     * You can also look at [ms-iot iMX8](https://github.com/ms-iot/MU_PLATFORM_NXP) for a real platform
       implementation.
     * Check out our docs in our Project Mu Teams channel as we have presentations on OVMF and Intel
       OpenKBL platforms.

## Nomenclature

I will use the term *workspace root* to reference the base folder for your code tree.

Ordinarily, we use the *Platform Repository* as the outer-most layer. This means that the outermost git repository is
 where we store Platform specific files and libraries. In this case, our *Platform Repo* is also our *workspace root*.
 If you choose to have a different repository layout, it will be important to note what your *workspace root* is, as
 it should still be the base folder of your code tree.

Submodules are full git repos on their own. What we do with these repos is add them as sub-repos to the
*workspace root*. Git will create a `.gitmodules` file that contains links to the repo and default branches. There are
git submodule commands that you can use to work with your submodules, such as:

```bash
git submodule add <url> <path>  # url to submodule, path to submodule installation
git submodule update --init --recursive  # Recursively initializes and updates all submodules.
git submodule foreach git status  # git submodule foreach can be used to run a command in each submodule.
                                  # git status is just an example.
```

For more information available [here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

## Create Git Repo

Make new directory.

```cmd
mkdir NewPlatformRepo
cd NewPlatformRepo
git init
```

This will serve as our Platform Repository as well as our Workspace Root.

For more information on creating a Git repo, here are
[command line instructions](https://kbroman.org/github_tutorial/pages/init.html) and here are
[web instructions](https://help.github.com/en/articles/create-a-repo).

## Add pertinent submodules

Project MU is separated into submodules. For each submodule that you need for your project, run the "git submodule add"
command to add it to your base Repository. The path after the URL is the path we typically use to group the submodules.
You can change it if you'd like, just remember your environment will diverge from the one in these instructions.

### [MU_BASECORE](https://github.com/Microsoft/mu_basecore.git)

This is the core section of TianoCore. Contains the guts of UEFI, forked from TianoCore, as well as the BaseTools
needed to build. You will need this to continue.

```cmd
git submodule add https://github.com/Microsoft/mu_basecore.git MU_BASECORE
```

### [MU_PLUS](https://github.com/Microsoft/mu_plus.git)

Additional, optional libraries and tools we've added to make MU great!

```cmd
git submodule add https://github.com/Microsoft/mu_plus.git Common/MU
```

### [MU_TIANO_PLUS](https://github.com/Microsoft/mu_tiano_plus.git)

Additional, optional libraries and tools forked from TianoCore.

```cmd
git submodule add https://github.com/Microsoft/mu_tiano_plus.git Common/TIANO
```

### [MU_OEM_SAMPLE](https://github.com/Microsoft/mu_oem_sample.git)

This module is a sample implementation of a FrontPage and several BDS support libraries. This module is intended to
be forked and customized.

```cmd
git submodule add https://github.com/Microsoft/mu_oem_sample.git Common/MU_OEM_SAMPLE
```

### [MU_SILICON_ARM_TIANO](https://github.com/Microsoft/mu_silicon_arm_tiano.git)

Silicon code from TianoCore has been broken out into individual submodules. This is the ARM specific submodule.

```cmd
git submodule add https://github.com/Microsoft/mu_silicon_arm_tiano.git Silicon/ARM/TIANO
```

### [MU_SILICON_INTEL_TIANO](https://github.com/Microsoft/mu_silicon_intel_tiano.git)

Silicon code from TianoCore has been broken out into individual submodules. This is the Intel specific submodule.

```cmd
git submodule add https://github.com/Microsoft/mu_silicon_intel_tiano.git Silicon/INTEL/TIANO
```

You can run `git submodule --update --init` to make sure all the submodules are set up.

## Adding your platform contents

``` pre
New_Platform_Repo/
├── Common/
│   └── ...                    # MU_PLUS, MU_OEM_SAMPLE, MU_TIANO_PLUS are generally created by the "git submodule ..."
├── MU_BASECORE/
├── PlatformGroup/
│   └── PlatformName/
│       └── PlatformBuild.py   # Python script to provide information to the build process.
│       └── Platform.dsc       # List of UEFI libraries and drivers to compile, as well as platform settings.
│       └── Platform.fdf       # List of UEFI Drivers to put into Firmware Volumes.
├── Silicon/
│   └── SiProvider/            # You should create a separate git repo for Silicon code for development with partners.
│       └── REF_CODE/          # Enablement code for your architecture
├── .gitattributes
├── .gitignore
└── .gitmodules
```

You will need to create PlatformBuild.py, Platform.dsc, and Platform.fdf. These files will go inside the platform
folder, which will be `New_Platform_Repo/PlatformGroup/PlatformName`. The
[ms-iot iMX8](https://github.com/ms-iot/MU_PLATFORM_NXP) repo can help you get started as a layout reference and
can demonstrate the PlatformBuild file. More information about PlatformBuild can be found
[here](../CodeDevelopment/compile/).
