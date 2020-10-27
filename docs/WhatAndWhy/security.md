# Active Security Patching

## Summary

In order to simplify adoption and to ensure that security fixes make it into the core repository as quickly as
possible, Project Mu maintains "Security Patch" versions of all applicable repos that are constantly synced
with the public versions. These Security Patch repos are identical to the top of tree in the public repos, but
already have all known (and relevant) security patches applied, to the best of our judgement (any choices that
were required when authoring the patch are described in the patch notes).

Each of the security-specific patches are noted with `SECURITY PATCH` in the commit title and a `MU_SEC_***`
tag in the commit title that indicates the related bug database tracking the issue (e.g. TianoCore Bugzilla, CVE, etc.).

## Requesting Access

Due to a number of factors including disclosure embargoes, these repos are available to the public by request only. If
you are interested in getting access, please contact us through the Project Mu Team. Access will be granted to any
members who can establish that they have already been given prior clearance to the relevant bug tracking databases.

## Usage

The Security Patch repos maintain branches that are 1:1 matches with public branches. All that is necessary to ingest
the security patches is to retarget your Git submodule at the Security Patch repo and pull the branch with the same name.
They are also kept in sync with any `*_RC` tags that are applied to the public repo, so it should be simple to identify
which public commit corresponds to wich SP repo commit.
