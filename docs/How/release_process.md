# Overview

!!! note
    The basics of this process are identical to those followed by the Project Mu firmware integration and release process internal to Microsoft, but the formal documentation, branch naming, and tagging process is a work in progress. While this is how we expect things to work, there may be changes within the the first few releases driven by feedback within the team and any external consumers/contributors.

In the interest of maintaining a close, well-defined relationship with the upstream project, TianoCore, the primary branch of Project Mu is periodically deprecated and all Mu-related changes are rebased onto a selected commit of TianoCore. This keeps Project Mu up to date with TianoCore while highlighting all Project Mu differences in the most recent commits and encouraging the reverse integration of all universal changes/fixes back into TianoCore.

In general, the life-cycle of a branch looks like:

<center>![Stable Release, Upsteam Rebase, Build/Boot Fixes, Active Development, Stabilization, Stable Release](../img/release_cycle.png)</center>

In general, stable release branches will live in the `stable/*` namespace and development branches will live in the `dev/*` namespace. All other branches are used for feature sharing, demonstration, and collaboration.

!!! important
    Due to the impacts of the rebase process on the history of Mu release branches, any downstream consumers will have to follow a similar integration process when upgrading to a new release. Any custom changes made within the Project Mu repos will have to be rebased from one release to the next.
    
    This is why we recommend to only directly modify Mu where necessary, and instead leverage the distributed repo management system to integrate proprietary code/modules.

## Upstream Integration Phase

At this time, we are targeting upstream integrations for roughly once a quarter. Prior to an integration, the status dashboard (not yet created) will be updated with the target date of completion and the target TianoCore commit.

For example, when transitioning between "release

## Active Development Phase

### Public Contribution/Commentary

### Upstream Cherry-Picks

## Stabilization Phase

### Long-Term Support (LTS)

## Lifetime of a Single Integration
