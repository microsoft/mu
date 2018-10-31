# How to Build/Compile

The repository/product/project should describe any unique steps required.  Project Mu currently has two supported patterns.  Those will be described here to encourage pattern/code reuse and limit the required repository specific documentation.  

## Compile Testing aka __MuBuild__

It is often desirable to compile test code and at times there might not be a product to test with.  This is also how the Pull Requests gates are implemented and enforced.

!!! Note
    This also runs the other static code tests so it does more than compile.  

    Assumption is that the repository to compile has been cloned to your filesystem and is in the state ready to compile. 

1. Open cmd prompt at workspace root
2. Run bootstrapper to get necessary build components
3. Run MuBuild to:
    * Clone code dependencies
    * Download binary dependencies
    * Statically test code
    * Compile test code
```cmd
MU_BUILD\UefiBuild\MuBuild\MuBuild.py -c <Mu Repo Build Config File> -p <1st Mu Pkg Build Config File> <2nd Mu Pkg Build Config File...>
```
4. Open __TestResults.xml__ for results 
5. Open log files to debug any errors


## Project Build aka __PlatformBuild__

When you actually want to compile for a platform that will create a firmware binary which can be flashed and execute on a platform this process is necessary.  

1. Locate the __PlatformBuild.py__ file
2. Run __PlatformBuild.py__

_TODO_ describe common features and options of PlatformBuild
