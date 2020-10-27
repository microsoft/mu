# Steps for a New Integration

## Overview

Below, you will find a checklist of the steps that should be followed by any project maintainers when performing a new
upstream integration. This is for reference by the maintainers and by any of the community interested in the process.

We will do our best to keep this up to date, so it's an excellent reference for what to expect if you're waiting on an
integration.

## 1) Announce

Advertise the upcoming update, where it will start from, how long it will take, and what will happen with the existing
release branch afterwards. This should be done in the `Release Announcements` channel in the Project Mu Team.

## 2) Rebase and Test

Much of this process is designed to be run on every Mu repo. When deciding which repos to update first, refer to the CI
dependencies documented in each repo.

There are currently exceptions to this rule. The `mu_basecore`, `mu_silicon_arm_tiano`, and `mu_tiano_plus` repos have a
circular dependency that must be worked with care. Refer to the integration guide videos for clarificaion on how these
three should work. They should be rebased and tested prior to any of the others, starting with `mu_basecore`.

### a) Prep for the Naive Rebase

* Create `rebase/*_naive` branch
* Update the readme with new branch info and update all CI badges to look for the new branch
  * Make sure to update source and destination commits

### b) Perform the Naive Rebase

NOTE: This process will not be followed the same way on "pure Mu" repos such as `mu_plus`.
For each repo, refer to the Readme for any special maintenance instructions.

* Work through the Naive Rebase
  * Make sure to pay attention to first two commits and whether any new packages/files/submodules need to be dropped
  * Make sure to drop any new `.pytool/Plugins` that may have been added to other repos that are only needed in
    `mu_basecore`
* Keep notes of any major conflicts/sightings, how the were resolved, and any follow up steps that may be needed
* Sync the Azure pipelines and other docs, .gitignore with Basecore. Try to keep things consistent where possible

### c) Clean the Rebase

* Create `rebase/*_1` branch and perform initial cleaning
* Repeat with as many new cleaning branches as necessary
  * Always diff with the `rebase/*_naive` branch to ensure changes are understood
* Create the `rebase/*_staging` branch when complete
* For `mu_basecore`, build and release the BaseTools binary (using the pipeline)
  * Afterwards, update the ext_dep with the updated binary version

### d) Prepare for Testing

* Tag the branch as `*_Rebase` and push tag to remotes
  * NOTE: From here on out, can only make new commits
* On the 3 cicular dependency repos, will need to create a temp commit that updates dependencies to point at
  the corresponding `rebase/*_staging` branch, rather than the final `release/*` branch

### e) Run Testing

* Repeatedly run the PR gate pipelines (recomment using the servers) and resolve build issues as they emerge
  * Each issue should be solved in it's own commit and include an update to the Readme with details and potential
    follow-up actions

### f) Clean Up

* Once passing CI on a given repo, first rebase agains the `*_Rebase` tag to remove the temp commit for dependencies
  if it was created
  * Should only apply to the 3 circular dependency repos
* Confirm all CI Build notes were updated in the Readme
* Tag as `*_CIBuild` and push to all remotes
  * NOTE: Again, from here on out we cannot reinvent history after this tag

## 3) Boot a Reference Platform

Once all rebases have been completed on all repos...

* On a reference platform, create a new branch for integration testing
* Pivot all Mu submodules to the new `rebase/*_staging` branch
* Build platform and fix issues as discovered
  * Update individual Readmes with notes on changes required
  * Try to keep these notes associated with the correct repo. Example: if the platform requires a new PCD to build
    and this PCD is defined in `UefiCpuPkg`, update the `mu_basecore` Readme with a note about the platform decision
    (and ideally include recommendations)
* Once built, boot platform and fix issues as discovered
  * Update individual Readmes with notes on changes required

## 4) Change Default Branches

Once a reference platform successfully boots to Windows...

* Tag all repos as `*_RefBoot` and push tag to remotes
* Create `release/*` branch in all repos and push branch to remotes
* Follow the steps in the tutorial videos to move the public and internal defaults

## 5) Update Security Repos

* Follow the steps in the tutorial videos to update all current Security Patch repos

## 6) Announce Completion

* Use the `Release Announcements` channel in the Project Mu Team to announce completion
