# How to Build/Compile

The repository/product/project should describe any unique steps required.  Project Mu currently supports two methods of building.  Those will be described here to encourage pattern/code reuse and limit the required repository specific documentation.  

## Compile Testing aka __Mu_Build__

Mu_Build is a framework for running a battery of tests against a single Mu repository (and its dependencies).  A plugin model is used for adding additional tests.  Today one such plugin is a basic compile test.  The repository maintainer may add additional tests such as linters, etc.

It is often desirable to compile test code and at times there might not be a product to test with.  This is also how the Pull Requests gates are implemented and enforced.

!!! Note
    This also runs the other static code tests so it does more than compile.  

    Assumption is that the repository to compile has been cloned to your filesystem and is in the state ready to compile.

1. Open cmd prompt at workspace root
2. __Suggestion:__ Activate your python virtual environment
3. Install or update Python dependencies using pip
4. Run Mu_Build to:
    * Clone code dependencies
    * Download binary dependencies
    * Statically test code
    * Compile test code
    ```cmd
    mu_build -c <Mu Repo Build Config File> -p <1st Mu Pkg Build Config File> <2nd Mu Pkg Build Config File...>
    ```
5. Open __TestResults.xml__ for results
6. Open log files to debug any errors

## Project Build aka __PlatformBuild__

??? info
    There is currently no example in Project Mu. An example platform is in the works!

When you actually want to compile for a platform that will create a firmware binary which can be flashed and execute on a platform this process is necessary.  

1. open cmd prompt at workspace root
2. __Suggestion:__ Activate your python virtual environment
3. Install or update Python dependencies using pip
4. Locate the __PlatformBuild.py__ file (generally in the platform build dir)
5. Run __PlatformBuild.py__

### Other features

__PlatformBuild.py__ leverages a common _UefiBuild_ python component.  This component provides a common set of features.  The UefiBuild component documentation is published from the mu_pip_environment repository but here are a few of the common features developers find useful.

* Control the target of the build.  Pass `Target=RELEASE`
* Build a single module: `BuildModule=MdePkg/ModuleToBuild.inf`
* Build with reporting:
  * Single report type `BUILDREPORTING=TRUE BUILDREPORT_TYPES="PCD"`
  * Change report file `BUILDREPORT_FILE=filename.txt` default is __BUILD_REPORT.TXT__
  * All report types. `BUILDREPORTING=TRUE BUILDREPORT_TYPES="PCD DEPEX FLASH BUILD_FLAGS LIBRARY"`
* Clean build: `--clean`
* Clean only (no compile): `--cleanonly`
* Skip some of the build steps:
  * Skip the Edk2 build step: `--skipbuild`
  * Skip pre or post build steps: `--skipprebuild` or `--skippostbuild`
* Change a Build variable that is used in Edk2 build process:
  * `BLD_*_DEBUG_OUTPUT_LEVEL=0x80000004` will be passed to DSC/FDF as __DEBUG_OUTPUT_LEVEL__.  These variable names and behavior are platform defined.  
  * `BLD_*_<var name>` is used for builds of any target type unless there is a more specific version for the given target type.
  * `BLD_DEBUG_<var name>` is used for debug builds only
  * `BLD_RELEASE_<var name>` is used for release builds only
* Using a config file.  To simplify calling of __PlatformBuild.py__ if there is a __BuildConfig.conf__ in the root of your UEFI workspace those parameters will be used as well.  The command line overrides anything from the conf file.  

### Example BuildConfig.conf

```yml
# Turn on full build reports
BUILDREPORTING=TRUE
BUILDREPORT_TYPES="PCD DEPEX FLASH BUILD_FLAGS LIBRARY"
```