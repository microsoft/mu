## Overview

!!! warning "Contents and Process Under Active Development"
    The basics of this process are identical to those followed by the Project Mu firmware integration and release process internal to Microsoft, but the formal documentation, branch naming, and tagging process is a work in progress. While this is how we expect things to work, there may be changes within the the first few releases driven by feedback within the team and any external consumers/contributors.

In the interest of maintaining a close, well-defined relationship with the upstream project, TianoCore, the active release branch of Project Mu is periodically deprecated and all Mu-related changes are rebased onto a selected commit of TianoCore. This keeps Project Mu up to date with TianoCore while highlighting all Project Mu differences in the most recent commits and encouraging the reverse integration of all universal changes/fixes back into TianoCore.

In general, the life-cycle of active code follows the following path:

<center>![Stable Release, Upsteam Rebase, Build/Boot Fixes, Active Development, Stabilization, Stable Release](../img/release_cycle.png)</center>

All active work in Project Mu is performed on a `release/*` branch, usually named sequentially according to the date of TianoCore commit that it's based on (eg. `release/201808` is based on the `edk2-stable201808` branch in TianoCore). Work proceeds on that branch until a new TianoCore integration is targeted, at which point a new branch in created and all existing changes are rebased onto the new branch and the new branch is used for all active development going forward. At this point, the previous branch enters a stabilization period where further tests are performed and only bug fixes are allowed to be committed. After stabilization, the branch is labeled as `stable` and will only receive critical bug fixes either directly to the branch or backported from a more recent release.

`release/*` branches will be maintained in LTS for at least the next two releases.

<center>![Multiple, staggared branches from EDK2, with rebased changes](../img/repo_release_graph.png)</center>

The below diagram illustrates the life-cycle of a single branch and indicates the critical points in its lifetime. These critical points will be applied as tags for reference and documentation. The tags are given a name relative to the target branch and consist of: Upstream base, Rebase complete, Rebase builds, Rebase boots, RC _N_, and Stable. These tags are discussed in more detail below.

<center>![The phases of a release branch: integration, active dev, stabilization, LTS](../img/branch_release_graph.png)</center>

!!! danger "Important"
    Due to the impacts of the rebase process on the history of Mu release branches, any downstream consumers will have to follow a similar integration process when upgrading to a new release. Any custom changes made within the Project Mu repos will have to be rebased from one release to the next.
    
    This is why we strongly discourage forking Project Mu for direct modification (ie. consumption, not contribution). Instead, leverage the distributed repo management system and override management system to integrate proprietary code/modules.

## Upstream Integration Phase

At this time, we are targeting upstream integrations for roughly once a quarter, attempting to align 1:1 with the TianoCore stable release cadence. Prior to an integration, the status dashboard (not yet created) will be updated with the target date of completion and the target TianoCore commit and/or release. For example, a plan was made to transition off of `release/20180529` when TianoCore announced the `edk2-stable201808` release.

Once a commit is selected, a set of rebase commits will be chosen from the active (previous) `release/*` branch. Ideally, these commits would include everything from the previous rebase through the most recent `*_RC` tag. For example, when moving from the `release/201808` branch, the commits will be selected from `1808_Upstream` (not inclusive) tag to `1808_RC1`.

After selection, this list of commits will be evaluated to determine whether any changes are no longer needed in the Mu history. The most likely causes of this action are:

* A change was submitted to TianoCore and has been accepted since the last rebase. Therefore, the change is no longer needed in Mu history.
* A change was reverted or modified more recently in Mu history, and the history of this change was squashed to maintain simplicity when comparing with upstream (TianoCore).

Once all evaluation is completed, the rebase will be performed in the new `release/*` branch. This branch will then be built for a reference platform (to be selected by internal team) and booted, at which point it will be considered the active development branch.

### Integration Milestone Tags

During integration, multiple tags are applied to the branch to serve as milestones. They also serve as reference point for changelog documentation that is produced during the integration process. These tags are described below:

* `*_Upstream`
    * This tag is placed on the exact TianoCore commit that a given release branch started from. This is used as a reference point between branches and relative to the rebase operation. The documentation produced for this tag contains the differences in TianoCore between this branch and the previous branch. For branches that originated from TianoCore releases, this changelog should be almost identical to the TianoCore changelog.
* `*_Rebase`
    * This tag is placed on the commit at the branch HEAD once the rebase is completed. The only changes to the commits from the last branch should be merge conflict resolutions and any history simplification as described above. The documentation produced for this tag contains a record of these resolutions and simplifications.
* `*_RefBuild`
    * This tag is placed on the commit where a reference platform consuming a large portion of the Mu code can successfully build. The documentation produced for this tag contains any changes required to get the reference platform building. It includes a list of changes outside the Mu project that are recommended for any consuming platform.
* `*_RefBoot`
    * This tag is placed on the commit where a reference platform consuming a large portion of the Mu code can successfully boot. The documentation produced for this tag contains any changes required to get the reference platform booting. It includes a list of changes outside the Mu project that are recommended for any consuming platform.

In each of these cases, the `*` will be replaced with a corresponding branch name. For example, the tags associated with `release/201808` will be prefixed with `1808` (eg. `1808_Rebase`, `1808_RC1`, etc.).

## Active Development Phase

During the active development phase, the release branch is open for comment and contribution both internally and publicly. The Project Mu team strives to do as much of its work in the open as possible, but there are still times when it will be necessary to 

Direct mirror internal and external.

### Public Contribution/Commentary

### Upstream Cherry-Picks

## Stabilization Phase

Transition branches.

### Long-Term Support (LTS)

## Lifetime of a Single Integration

***TBD***
