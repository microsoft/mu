# How to contribute

There are three common ways to contribute.

1. Participate in discussions using GitHub issues.
1. Contribute documentation by opening a GitHub Pull Request.
1. Contribute code by opening a GitHub Pull Request

## Issue Tracker Usage

https://github.com/Microsoft/mu/issues

### General feedback and discussions

Please start a discussion on the issue tracker.

### Bugs and feature requests

For non-security related bugs please log a new issue on the [Project Mu repo issue tracker](https://github.com/Microsoft/mu/issues). The best way to get your bug fixed is to be as detailed as you can be about the problem. Providing a code snippet or sample driver that exposes the issue with steps to reproduce the problem is ideal.  

### Reporting security issues and bugs

Security issues and bugs should be reported privately, via email, to the Microsoft Security Response Center (MSRC)  secure@microsoft.com. You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Further information, including the MSRC PGP key, can be found in the [Security TechCenter](https://technet.microsoft.com/en-us/security/ff852094.aspx).

## Contributions of Documentation and/or Code

### Pull Requests

If you don't know what a pull request is read this article: https://help.github.com/articles/about-pull-requests . Make sure the repository can build and all tests pass. Familiarize yourself with the project workflow and our coding conventions.

### General workflow

1. Fork Repository in GitHub
2. Make code changes.  [More Details](../DeveloperDocs/code_requirements.md)
3. Build it, test it, document it
    * Do a package build to confirm it compiles and passes code analysis tests
    * Build it into a platform which you can test the functionality
    * Build a unit test.  Project Mu (and UEFI) needs more automated/regression testing.
    * Document it.  Add to an existing or create a new markdown file. [More Details](../DeveloperDocs/doc_requirements.md)
4. Submit a Pull Request back to the development branch you would like to target.
5. You will be asked to digitally sign a CLA
6. The server will run some builds and tests and report status
7. Community and reviewers will provide feedback in the Pull Request
8. Make changes / adjust based on feedback and discussion
9. Keep your PR branch in-sync with the branch you are targeting and resolve any merge conflicts
10. Once the the PR status is all passing it can be squashed and merged (just press the button in the PR).  If the PR is ready the maintainers may complete it for you.  

That is it.  Thanks for contributing.  

### Contributor License Agreement (CLA)

This project welcomes contributions and suggestions.  Most (code and documentation) contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.