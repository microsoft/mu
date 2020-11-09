# Steps for a New Integration

## Overview

In Project Mu, any time we snap to a new commit from our upstream project, [Tianocore](https://github.com/tianocore/edk2),
we call that an Integration. This usually happens when Tianocore releases a new stable tag, but it can happen at other
times, as needed.

Below, you will find a checklist of the steps that should be followed by any project maintainers when performing a new
upstream integration. This is for reference by the maintainers and by any of the community interested in the process.

We will do our best to keep this up to date, so it's an excellent reference for what to expect if you're waiting on an
integration.

## 1) Announce

Advertise the upcoming update, where it will start from, how long it will take, and what will happen with the existing
release branch afterwards. This should be done in the [Release Announcements](https://teams.microsoft.com/l/channel/19%3a2fcb1744302e4cd28b5a7e9d46479ca8%40thread.skype/Release%2520Announcements?groupId=6ba27a5b-86b2-4dc2-9d74-a8d8a03c3c3f&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47)
channel in the Project Mu Team.

## 2) Rebase and Test

Much of this process is designed to be run on every Mu repo. When deciding which repos to update first, refer to the CI
dependencies documented in each repo. [See here](https://github.com/microsoft/mu_basecore/blob/ce3097e7de6f44f6788b96f7f2dae7c863d44a89/.pytool/CISettings.py#L155)
for an example.

There are currently exceptions to this rule. The `mu_basecore`, `mu_silicon_arm_tiano`, and `mu_tiano_plus` repos have a
circular dependency that must be worked with care. Refer to the integration guide videos for clarification on how these
three should work. They should be rebased and tested prior to any of the others, starting with `mu_basecore`.

### a) Prep for the Naive Rebase

* Create `rebase/*_naive` branch by starting at the very tip of the current (latest) release branch
  * There may be reasons to choose a commit other than the very tip, but this is the default
* Update the readme with new branch info and update all CI badges to look for the new branch
  * Make sure to update source and destination commits

### b) Perform the Naive Rebase

NOTE: This process will not be followed the same way on "pure Mu" repos such as `mu_plus`.
For each repo, refer to the Readme for any special maintenance instructions.

* Work through the Naive Rebase
  * Make sure to pay attention to first two commits and whether any new packages/files/submodules need to be dropped
  * Make sure to drop any new `.pytool/Plugins` that may have been added to other repos that are only needed in
    `mu_basecore`. Some plugins may have been added by the upstream project, but most plugins should only live in
    `mu_basecore`
* Keep notes of any major conflicts/sightings, how they were resolved, and any follow up steps that may be needed
* Sync the Azure pipelines and other docs, .gitignore with Basecore. Try to keep things consistent where possible
  * Easiest way to do this is just a Beyond Compare with Basecore and look at the `.azurepipelines` and `.pytool`
    directories, as well as the `pip_requirements.txt`, `.gitignore`, `RepoDetails.txt`, and `Readme.rst` files

### c) Clean the Rebase

This is an optional -- though desireable -- step where we have the opportunity to squash small bugfixes, drop
temporary/testing commits, update features with new testing requirements, and any other behavior that helps keep
the history clean and readable.

* Create `rebase/*_1` branch and perform initial cleaning
* Repeat with as many new cleaning branches as necessary
  * Always diff with the `rebase/*_naive` branch to ensure changes are understood
* Create the `rebase/*_staging` branch when complete
* For `mu_basecore`, build and release the BaseTools binary (using the pipeline)
  * Afterwards, update the [ext_dep](https://github.com/microsoft/mu_basecore/blob/release/202008/BaseTools/Bin/basetoolsbin_ext_dep.yaml)
    with the updated binary version
  * [See here](https://github.com/tianocore/edk2-pytool-extensions/blob/master/docs/usability/using_extdep.md) for more
    details

### d) Prepare for Testing

* Tag the branch as `*_Rebase` and push tag to remotes
  * NOTE: From here on out, can only make new commits
* On the 3 circular dependency repos, will need to create a temp commit that updates dependencies to point at
  the corresponding `rebase/*_staging` branch, rather than the final `release/*` branch

### e) Run Testing

* Repeatedly run the PR gate pipelines (recommend using the servers) and resolve build issues as they emerge
  * Each issue should be solved in it's own commit and include an update to the Readme with details and potential
    follow-up actions

### f) Clean Up

* Once passing CI on a given repo, first rebase against the `*_Rebase` tag to remove the temp commit for dependencies
  if it was created
  * Should only apply to the 3 circular dependency repos
* Confirm all CI Build notes were updated in the Readme
* Tag as `*_CIBuild` and push to all remotes
  * NOTE: Again, from here on out we cannot reinvent history after this tag

## 3) Boot a Reference Platform

Once rebase has been completed on all repos...

* On a reference platform, create a new branch for integration testing
* Pivot all Mu submodules to the new `rebase/*_staging` branch
* Build platform and fix issues as discovered
  * Update individual Readme files with notes on changes required
  * Try to keep these notes associated with the correct repo. Example: if the platform requires a new PCD to build
    and this PCD is defined in `UefiCpuPkg`, update the `mu_basecore` Readme with a note about the platform decision
    (and ideally include recommendations)
* Once built, boot platform and fix issues as discovered
  * Update individual Readme files with notes on changes required

## 4) Change Default Branches

Once a reference platform successfully boots to Windows...

* Tag all repos as `*_RefBoot` and push tag to remotes
* Create `release/*` branch in all repos and push branch to remotes
* Follow the steps in the [tutorial](https://msit.microsoftstream.com/video/2621a4ff-0400-9fb2-0956-f1eb0db01e45)
  [videos](https://msit.microsoftstream.com/video/65efa3ff-0400-9fb2-d666-f1eb0db4336f) to move the public and
  internal defaults

## 5) Update Security Repos

* Follow the steps in the [tutorial video](https://msit.microsoftstream.com/video/8f0fa1ff-0400-9fb2-2468-f1eb0a7c3087?list=studio)
  to update all current Security Patch repos

## 6) Announce Completion

* Use the `Release Announcements` channel in the Project Mu Team to announce completion
