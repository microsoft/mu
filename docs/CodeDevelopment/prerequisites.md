# Prerequisites for building Code

Generally there are a set of tools required on the platform.  Project Mu tries to minimize the number of global tools but there are a few.  There could be more depending on the repository/product/platform you are building but this should get you started.  If the repo requires other tools those should be documented within the repo.  
The tools also vary by Operating System and Compiler choice.  Project Mu will document what is currently supported but the expectation is that between Project Mu and TianoCore Edk2 you could use any of those tool sets.

## Windows

### Python

1. Download latest Python from https://www.python.org/downloads
    ``` cmd
    https://www.python.org/ftp/python/3.7.1/python-3.7.1-amd64.exe
    ```
2. It is recommended you use the following options when installing python:
    1. include pip support
    2. include test support

### Git

1. Download latest Git For Windows from https://git-scm.com/download/win 
    ``` cmd
    https://github.com/git-for-windows/git/releases/download/v2.19.1.windows.1/Git-2.19.1-64-bit.exe
    ```
2. It is recommended you use the following options:
    1. Checkout as is, commit as is.
    2. Native Channel support (this will help in corp environments)

### Visual Studio 2017

1. Download latest version of VS build Tools to c:\TEMP
    ``` cmd
    https://aka.ms/vs/15/release/vs_buildtools.exe
    ```
2. Install from cmd line with required features (this set will change overtime).
    ``` cmd
    C:\TEMP\vs_buildtools.exe --quiet --wait --norestart --nocache --installPath C:\BuildTools --add Microsoft.VisualStudio.Component.VC.CoreBuildTools --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 --add Microsoft.VisualStudio.Component.Windows10SDK.17134 --add Microsoft.VisualStudio.Component.VC.Tools.ARM --add Microsoft.VisualStudio.Component.VC.Tools.ARM64
    ```
See component list here for more options. https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2017 

### Get the Project Mu Build tools using Pip

Usually this can be done by looking for the __requirements.txt__ file.  Each repo generally has one to describe the required modules.  

This can be installed by doing:

 ```cmd
pip install --upgrade -r requirements.txt
```

!!! note "Virtual Environments"
    In more active development environments or on PCs where you might want to have different versions of these tools to support older/newer platforms it is recommended to leverage python virtual environments to avoid any global dependencies.  

Project Mu currently has 3 pip modules:

#### mu_python_library

UEFI, Edk2, Acpi, and TPM common library functions.

``` cmd
python -m pip install --upgrade mu_python_library
```

#### mu_environment

Self Describing Environment (SDE) code which is used to organize and coordinate UEFI builds.  This is the Project Mu Build system, plugin manager, edk2 build wrapper, logging, etc.  

``` cmd
python -m pip install --upgrade mu_environment
```

#### mu_build

CI and package test scripts.  Supports compiling as well as running other build test plugins.

``` cmd
python -m pip install --upgrade mu_build
```

## Windows Subsystem For Linux (WSL)

_Coming soon_