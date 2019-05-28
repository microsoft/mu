# How to setup a new Repo for a Platform that will use Project MU?

This document will describe the base guidelines for setting up a Project MU repo.

You will need:

1) Git
2) Python 3.7
3) A text editor
4) Look at [layout](../WhatAndWhy/layout.html) to understand our recommended repository layout. You can also look at [ms-iot's iMX8](https://github.com/ms-iot/MU_PLATFORM_NXP) for a real platform implementation.

## 1) Create Git Repo

Make new directory.
```cmd
mkdir NewPlatformRepo
cd NewPlatformRepo
git init 
```
For more information on creating a Git repo, here are [command line instructions](https://kbroman.org/github_tutorial/pages/init.html) and here are [web instructions](https://help.github.com/en/articles/create-a-repo).

## 2) Add pertinent submodules

Project MU is separated into submodules. For each submodule that you need for your project, run the "git submodule add" command to add it to your base Repository. The path after the URL is the path we typically use to group the submodules. You can change it if you'd like, just remember your environment will diverge from the one in these instructions.

### [MU_BASECORE](https://github.com/Microsoft/mu_basecore.git)

This is the main repo. Contains the guts of the build system as well as core UEFI code, forked from TianoCore. You will need this to continue.

```cmd
git submodule add https://github.com/Microsoft/mu_basecore.git MU_BASECORE
```

### [MU_PLUS](https://github.com/Microsoft/mu_plus.git)

```cmd
git submodule add https://github.com/Microsoft/mu_plus.git Common/MU
```

### [MU_TIANO_PLUS](https://github.com/Microsoft/mu_tiano_plus.git)

```cmd
git submodule add https://github.com/Microsoft/mu_tiano_plus.git Common/TIANO
```

### [MU_OEM_SAMPLE](https://github.com/Microsoft/mu_oem_sample.git)

```cmd
git submodule add https://github.com/Microsoft/mu_oem_sample.git Common/MU_OEM_SAMPLE
```

### [MU_SILICON_ARM_TIANO](https://github.com/Microsoft/mu_silicon_arm_tiano.git)
Silicon code from TianoCore has been broken out into indivudal submodules. iMX8 is ARM, so we need this submodule.

```cmd
git submodule add https://github.com/Microsoft/mu_silicon_arm_tiano.git Silicon/ARM/TIANO
```

### [MU_SILICON_INTEL_TIANO](https://github.com/Microsoft/mu_silicon_intel_tiano.git)

```cmd
git submodule add https://github.com/Microsoft/mu_silicon_intel_tiano.git Silicon/INTEL/TIANO
```

You can run `git submodule --update --init` to make sure all the submodules are set up.

# 3) Adding your platform contents

Generally, we use the root directory (the one you just made) as the "Platform Directory".

```
New_Platform_Repo/
├── Common/
│   └── ...                     # MU_PLUS, MU_OEM_SAMPLE, MU_TIANO_PLUS will be in here
├── MU_BASECORE/
├── PlatformGroup/
│   └── PlatformName/
│       └── PlatformBuild.py    # Python script to provide information to the build process.
│       └── Platform.dsc        # List of UEFI libraries and drivers to compile, as well as platform settings.
│       └── Platform.fdf        # List of UEFI Drivers to put into Firmware Volumes.
├── Silicon/
│   └── SiProvider/             # You may want to create a separate git repo for Silicon code to enable development with partners.
│       └── REF_CODE/           # Enablement code for your architecture
├── .gitattributes
├── .gitignore
└── .gitmodules
```

You will need to create directories in this repository for your platform. The important Project MU piece is the PlatformBuild file. [ms-iot's iMX8](https://github.com/ms-iot/MU_PLATFORM_NXP) can be used as an example to help you get started!

# 4) Build instructions

Coming soon.