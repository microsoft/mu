# Contributing to Project Mu

Welcome, and thank you for your interest in contributing to Project Mu!

There are many ways in which you can contribute, beyond writing code. The goal of this document is to provide a
high-level overview of how you can get involved.

If this is your first time working with Project Mu, please keep in mind that many project details are maintained in
the [Project Mu Documentation](https://microsoft.github.io/mu/).

## Asking Questions

Have a question? Rather than opening an issue, please post your question under the `Q&A` category in the `Discussions`
section of the relevant Project Mu GitHub repo.

## Reporting Issues

Every Project Mu repo has an `Issues` section. Bug reports, feature requests, and documentation requests can all be
submitted in the issues section.

## Security Vulnerabilities

Please review the repos `Security Policy` but in general every Project Mu repo has `Private vulnerability reporting`
enabled.  Please use the security tab to report a potential issue.

### Identify Where to Report

Project Mu is distributed across multiple repositories. Use features such as issues and discussions in the repository
most relevant to the topic.

Although we prefer items to be filed in the most relevant repo, if you're unsure which repo is most relevant, the item
can be filed in the [Project Mu Documentation Repo](https://github.com/microsoft/mu) and we will review the request and
move it to the relevant repo if necessary.

### Look For an Existing Issue

Before you create a new issue, please do a search in the issues section of the relevant repo to see if the issue or
feature request has already been filed.

If you find your issue already exists, make relevant comments and add your
[reaction](https://github.com/blog/2119-add-reactions-to-pull-requests-issues-and-comments). Use a reaction in place
of a "+1" comment:

* 👍 - upvote
* 👎 - downvote

If you cannot find an existing issue that describes your bug or feature, create a new issue using the guidelines below.

### Follow Your Issue

Please continue to follow your request after it is submitted to assist with any additional information that might be
requested.

### Pull Request Best Practices

Pull requests for UEFI code can become large and difficult to review due to the large number of build and
configuration files. To aid maintainers in reviewing your code, we suggest adhering to the following guidelines:

1. Do keep code reviews single purpose; don't add more than one feature at a time.
2. Do fix bugs independently of adding features.
3. Do provide documentation and unit tests.
4. Do introduce code in digestible amounts.
   * If the contribution logically be broken up into separate pull requests that independently build and function
     successfully, do use multiple pull requests.

#### Pull Request Description Checkboxes

Project Mu pull requests autopopulate a PR description from a template in most repositories. You should:

1. **Replace** this text with an actual descrption:

   ```txt
   <_Include a description of the change and why this change was made._>
   ```

2. **Remove** this line of instructions so the PR description shows cleanly in release notes:

   `"For details on how to complete these options and their meaning refer to [CONTRIBUTING.md](https://github.com/microsoft/mu/blob/HEAD/CONTRIBUTING.md)."`

3. For each checkbox in the PR description, **place an "x"** in between `[` and `]` if true. Example: `[x]`.
   _(you can also check items in the GitHub UI)_

   * **[] Impacts functionality?**
     * **Functionality** - Does the change ultimately impact how firmware functions?
     * Examples: Add a new library, publish a new PPI, update an algorithm, ...
   * **[] Impacts security?**
     * **Security** - Does the change have a direct security impact on an application,
       flow, or firmware?
     * Examples: Crypto algorithm change, buffer overflow fix, parameter
       validation improvement, ...
   * **[] Breaking change?**
     * **Breaking change** - Will anyone consuming this change experience a break
       in build or boot behavior?
     * Examples: Add a new library class, move a module to a different repo, call
       a function in a new library class in a pre-existing module, ...
   * [] **Includes tests?**
     * **Tests** - Does the change include any explicit test code?
     * Examples: Unit tests, integration tests, robot tests, ...
   * [] **Includes documentation?**
     * **Documentation** - Does the change contain explicit documentation additions
       outside direct code modifications (and comments)?
     * Examples: Update readme file, add feature readme file, link to documentation
      on an a separate Web page, ...

4. **Replace** this text as instructed:

   ```txt
   <_Describe the test(s) that were run to verify the changes._>
   ```

5. **Replace** this text as instructed:

   ```txt
   <_Describe how these changes should be integrated. Use N/A if nothing is required._>
   ```

#### Code Categories

To keep code digestible, you may consider breaking large pull requests into three categories of commits within the pull
request.

1. **Interfaces**: .h, .inf, .dec, documentation
2. **Implementation**: .c, unit tests, unit test build file; unit tests should build and run at this point
3. **Integration/Build**: .dec, .dsc, .fdf, (.yml) configuration files, integration tests; code added to platform and
   affects downstream consumers

By breaking the pull request into these three categories, the pull request reviewers can digest each piece
independently.

If your commits are still very large after adhering to these categories, consider further breaking the pull request
down by library/driver; break each component into its own commit.

#### Implementation Limits

Implementation is ultimately composed of functions as logical units of code.

To help maintainers review the code and improve long-term maintainability, limit functions to 60 lines of code. If your
function exceeds 60 lines of code, it likely has also exceeded a single responsibility and should be broken up.

Files are easier to review and maintain if they contain functions that serves similar purpose. Limit files to around
1,000 lines of code (excluding comments). If your file exceeds 1,000 lines of code, it may have functions that should
be split into separate files.

---

By following these guidelines, your pull requests will be reviewed faster, and you'll avoid being asked to refactor the
code to follow the guidelines.

Feel free to create a draft pull request and ask for suggestions on how to split the pull request if you are unsure.

## Thank You

Thank you for your interest in Project Mu and taking the time to contribute!
