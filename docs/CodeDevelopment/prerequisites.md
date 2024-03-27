# Prerequisites for building Code

Generally there are a set of tools required on the platform.  Project Mu tries to minimize the number of global tools
but there are a few.  There could be more depending on the repository/product/platform you are building but this should
get you started.  If the repo requires other tools those should be documented within the repo.
The tools also vary by Operating System and Compiler choice.  Project Mu will document what is currently supported but
the expectation is that between Project Mu and TianoCore Edk2 you could use any of those tool sets.

## Windows 10 x64

### Python

1. Download latest Python from <https://www.python.org/downloads>

    ``` cmd
    https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe
    ```

2. It is recommended you use the following options when installing python:
    1. include pip support
    2. include test support
    3. include venv virtual environment support

### Git

1. Download latest Git For Windows from <https://git-scm.com/download/win>

    ``` cmd
    https://github.com/git-for-windows/git/releases/download/v2.37.3.windows.1/Git-2.37.3-64-bit.exe
    ```

2. It is recommended you use the following options:
    1. Checkout as is, commit as is.
    2. Native Channel support (this will help in corp environments)
    3. Check the box to "Enable Git Credential Manager"

### Visual Studio 2022 **preferred**

1. Download latest version of VS build Tools to c:\TEMP

    ``` cmd
    https://aka.ms/vs/17/release/vs_buildtools.exe
    ```

2. Install from cmd line with required features (this set will change over time).

    ``` cmd
    C:\TEMP\vs_buildtools.exe --passive --wait --norestart --nocache --installPath C:\BuildTools ^
    --add Microsoft.VisualStudio.Component.VC.CoreBuildTools --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 ^
    --add Microsoft.VisualStudio.Component.Windows11SDK.22621 --add Microsoft.VisualStudio.Component.VC.Tools.ARM ^
    --add Microsoft.VisualStudio.Component.VC.Tools.ARM64
    ```
See component list here for more options. <https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2022>  
The `^` char is the line continuation char of cmd.exe. Simply remove them if you use previous command in PowerShell.

### Visual Studio 2019

1. Download latest version of VS build Tools to c:\TEMP

    ``` cmd
    https://aka.ms/vs/16/release/vs_buildtools.exe
    ```

2. Install from cmd line with required features (this set will change over time).

    ``` cmd
    C:\TEMP\vs_buildtools.exe --quiet --wait --norestart --nocache --installPath C:\BuildTools ^
    --add Microsoft.VisualStudio.Component.VC.CoreBuildTools --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 ^
    --add Microsoft.VisualStudio.Component.Windows10SDK.19041 --add Microsoft.VisualStudio.Component.VC.Tools.ARM ^
    --add Microsoft.VisualStudio.Component.VC.Tools.ARM64
    ```

See component list here for more options. <https://docs.microsoft.com/en-us/visualstudio/install/workload-component-id-vs-build-tools?view=vs-2019>

### Rust

Follow the Rust [install steps](/mu/CodeDevelopment/rust_build#generally-getting-started-with-rust) to install all
required tooling. This generally includes: `rustc`, `cargo`, `cargo-make`, and `cargo-tarpaulin`

### Optional - Windows Driver Kit

Provides Inf2Cat.exe, needed to [prepare Windows firmware update packages for signing](https://docs.microsoft.com/en-us/windows-hardware/drivers/bringup/certifying-and-signing-the-update-package).

1. Download the WDK installer

    ``` cmd
    https://go.microsoft.com/fwlink/?linkid=2085767
    ```

2. Install from cmd line with required features (this set will change over time).

    ``` cmd
    wdksetup.exe /features OptionId.WindowsDriverKitComplete /q
    ```

### Optional - Create an Omnicache

An Omnicache is a Project Mu tool that leverages git features to speed up git update operations.  This helps speed up
git operations if you have multiple workspaces by using the git "--reference" feature.

## Windows Subsystem For Linux (WSL) and Linux

Basic directions here. <https://www.tianocore.org/edk2-pytool-extensions/features/using_linux/>

## All Operating Systems - Python Virtual Environment and PyTools

In all Operating Systems environments the PyTools python modules are needed.

Python virtual environments are strongly suggested especially when doing development in multiple workspaces.  Each
workspace should have its own virtual environment as to not modify the global system state. Since Project Mu uses
Pip modules this allows each workspace to keep the versions in sync with the workspace requirements.

More info on Python Virtual Environments: <https://docs.python.org/3/library/venv.html>

### Workspace Virtual Environment Setup Process

#### A sample directory layout of workspaces and Python Virtual Environments

``` pre
    /Workspace1Root (basic platform)
    |-- src_of_project1
    |-- venv        <-- Virtual environment for Project in workspace root 1
    |
    /Workspace2Root (basic + local pytool dev support)
    | -- src_of_project2
    | -- venv       <-- Virtual environment for Project in workspace root 2 pip requirements
    | -- venv_dev   <-- Virtual environment configured to use local python modules
    | -- edk2-pytool-library    <-- local clone of python modules in library
    | -- edk2-pytool-extensions <-- local clone of python modules in extensions
```

Virtual environments only need to be created once per workspace.  They must be activated in each new cmd shell.

1. Open Cmd Prompt in the directory where you want to store your virtual environment.  A directory adjacent to
   workspace directories is convenient.
2. run python cmd

    ``` cmd
    python -m venv <your virtual env name>
    ```

3. Activate it for your session.

### Activate Virtual Environment

Do this each time you open a new command window to build your workspace.

1. Open Cmd Prompt
2. run activate script - for windows cmd prompt (cmd.exe) do this

    ``` cmd
    <your virtual env name>\Scripts\activate
    ```

3. cd into your workspace directory
4. Update/Install your python pip requirements.  This is generally at the workspace root.

    ``` cmd
    pip install --upgrade -r pip-requirements.txt
    ```

5. Do dev work and run your builds!
