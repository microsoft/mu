# How to Build/Compile

!!! info
    **MAJOR UPDATE** --
    The Project Mu Python packages for UEFI support and build tools have migrated to Tianocore and as a result
    things have changed.  These docs are now updated to leverage building with "edk2-pytools".

The repository/product/project should describe the unique steps required to build and test.  The build tools are now
a set of unique single purpose built tools called "stuart".  These tools together support building, updating binary
dependencies, updating git dependencies, and other functions.  Project Mu has two main patterns for building.  Those
will be described here to encourage pattern/code reuse and limit the required repository specific documentation.  More
details for pytools can be found here:

* <https://github.com/tianocore/edk2-pytool-extensions/tree/master/docs>
* <https://github.com/tianocore/edk2-pytool-library/tree/master/docs>

## CI multi-package Building and Testing aka **stuart_ci_build**

stuart_ci_build is a framework for running a battery of tests against a single Mu repository (and its dependencies).
A plugin model is used for adding additional tests.  Today one such plugin is a basic compile test.  Another plugin
compiles host based unit tests and runs them.  A third plugin checks for misspellings.  Check out the repository for
details on the tests.  Additional test plugins are usually found in `.pytool/Plugin`

It is often desirable to compile test code and at times there might not be a product to test with.  This is also how
the Pull Requests gates are implemented and enforced.

### CI Build Process

1. Open cmd prompt at workspace root
2. Activate your python virtual environment
3. Install or update Python dependencies using pip

    ```cmd
    pip install --upgrade -r pip_requirements.txt
    ```

4. Run stuart_setup to download required submodules.

    ```cmd
    stuart_setup -c <PyTool Config File>
    ```

5. Run stuart_ci_setup to download CI only dependencies

    ```cmd
    stuart_ci_setup -c <PyTool Config File>
    ```

6. Run stuart_update to download or update binary dependencies

    ```cmd
    stuart_update -c <PyTool Config File>
    ```

7. Run stuart_ci_build to build and test the packages

    ```cmd
    stuart_ci_build -c <PyTool Config File>
    ```

8. Open **TestResults.xml** in the build output for results (usually in workspace/Build)
9. Open log files to debug any errors

???+ info
    - In Project Mu repos the config file is generally at ```.pytool/CISettings.py```
    - Project Mu runs on Windows 10 using the following tags: VS2017 and VS2019
    - Project Mu runs on Ubuntu 18.04 using the tags: GCC5
    - Each of the stuart commands can take in additional parameters.  To see customized help run
      `<stuart cmd> -c .pytool/CISettings.py -h`
    - Some common optional parameters that *might* allow the stuart operation to optimize for expected usage.
      For example if only building for X64 ARCH then the ARM compilers might not be
      downloaded.  Or if using the VS2019 toolchain then GCC specific assets aren't needed.  If you only want to run CI
      against the MdePkg and MdeModulePkg then you can do that with `-p`.
        - `-a <arch csv>` - list of architectures to run for
        - `-p <packages csv>` - list of packages to run against
        - `-t <targets csv>` - list of targets to run for
        - `TOOL_CHAIN_TAG=<tag>` - set toolchain for operation

## Project Build aka **PlatformBuild** aka **stuart_build**

When you actually want to compile for a platform that will create a firmware binary which can be flashed and execute on
a platform the process is generally as follows.  Again the platform repository should have details but this is
generally the process.

### Platform Build Process

1. Open cmd prompt at workspace root
2. Activate your python virtual environment
3. Install or update Python dependencies using pip

    ```cmd
    pip install --upgrade -r <pip_requirements.txt file>
    ```

4. Run stuart_setup to download required submodules.

    ```cmd
    stuart_setup -c <platform Config File>
    ```

5. Run stuart_update to download or update binary dependencies

    ```cmd
    stuart_update -c <platform Config File>
    ```

6. Run stuart_build to build and test the packages

    ```cmd
    stuart_build -c <platform Config File>
    ```

7. Open the build output for log files to debug any errors (usually in workspace/Build)

???+ info
    - In Project Mu repos the platform config file is generally in the platform package.
    - Toolchains and host OS support is defined by the platform documentation.
    - Each of the stuart commands can take in additional parameters.  To see customized help run
      `<stuart cmd> -c <platform config file> -h`

### Other features

**stuart_build** leverages a common **UefiBuild** python component.  This component provides a common set of features.
The UefiBuild component documentation is published from the edk2-pytool-extensions repository but here are a few of the
common features developers find useful.

* Control the target of the build.  Pass `Target=RELEASE`
* Build a single module: `BuildModule=MdePkg/ModuleToBuild.inf`
* Build with reporting:
  * Single report type `BUILDREPORTING=TRUE BUILDREPORT_TYPES="PCD"`
  * Change report file `BUILDREPORT_FILE=filename.txt` default is **BUILD_REPORT.TXT**
  * All report types. `BUILDREPORTING=TRUE BUILDREPORT_TYPES="PCD DEPEX FLASH BUILD_FLAGS LIBRARY"`
* Clean build: `--clean`
* Clean only (no compile): `--cleanonly`
* Skip some of the build steps:
  * Skip the Edk2 build step: `--skipbuild`
  * Skip pre or post build steps: `--skipprebuild` or `--skippostbuild`
* Change a Build variable that is used in Edk2 build process:
  * `BLD_*_DEBUG_OUTPUT_LEVEL=0x80000004` will be passed to DSC/FDF as **DEBUG_OUTPUT_LEVEL**.  These variable names and
    behavior are platform defined.
  * `BLD_*_<var name>` is used for builds of any target type unless there is a more specific version for the given
    target type.
  * `BLD_DEBUG_<var name>` is used for debug builds only
  * `BLD_RELEASE_<var name>` is used for release builds only
* Using a config file.  To simplify calling of **PlatformBuild.py** if there is a **BuildConfig.conf** in the root of
  your UEFI workspace those parameters will be used as well.  The command line overrides anything from the conf file.

### Example BuildConfig.conf

```yml
# Turn on full build reports
BUILDREPORTING=TRUE
BUILDREPORT_TYPES="PCD DEPEX FLASH BUILD_FLAGS LIBRARY"
```
