# Code Development Overview

## Tools

First you will need to setup your UEFI development environment.  Project Mu leverages most of the tools from _TianoCore EDK2_.  We have streamlined the process for the tool chains and systems we use but our project's goals are to support various tool chains and development environments.  For the best experience or for those new to UEFI and Project Mu we have provided guidance in our [prerequisites](prerequisites.md) page.

## Code

Next you will need to clone a repository or set of repositories to work on.

For __core__ work (Project Mu Repos) you can clone the desired repo, make your changes, run CI builds, run your tests, and submit a PR.  

For __platform__ work (outside of Project Mu) you will need to clone the platform repository and then follow the platform setup process.  

See details on the [compile](compile.md) page for more information about CI builds and how to compile a package or platform.  

Code should follow best practices.  We are working to add some best practices on the [requirements](requirements.md) page. We also attempt to enforce these best practices thru our CI build process.

## Tests

One area of focus for Project Mu is on testing.  Firmware testing has traditionally been hard and very manual.  We hope to describe techniques and provide resources to make this easier and more automated.  Testing needs to be part of the code development process.  Check out the [testing](test.md) page for more details.  
