# Security

## Active Security Patching

### Summary

In order to simplify adoption and to ensure that security fixes make it into the core repository as quickly as
possible, Project Mu maintains "Security Patch" versions of all applicable repos that are constantly synced
with the public versions. These Security Patch repos are identical to the top of tree in the public repos, but
already have all known (and relevant) security patches applied, to the best of our judgement (any choices that
were required when authoring the patch are described in the patch notes).

Each of the security-specific patches are noted with `SECURITY PATCH` in the commit title and a `MU_SEC_***`
tag in the commit title that indicates the related bug database tracking the issue (e.g. TianoCore Bugzilla, CVE, etc.).

### Requesting Access

Due to a number of factors including disclosure embargoes, these repos are available to the public by request only. If
you are interested in getting access, please contact us through the Project Mu Team. Access will be granted to any
members who can establish that they have already been given prior clearance to the relevant bug tracking databases.

### Usage

The Security Patch repos maintain branches that are 1:1 matches with public branches. All that is necessary to ingest
the security patches is to re-target your Git submodule at the Security Patch repo and pull the branch with the same name.
They are also kept in sync with any `*_RC` tags that are applied to the public repo, so it should be simple to identify
which public commit corresponds to which SP repo commit.

## Active Security Patch Auditing

In project Mu's public repos a `SecurityFixes.yaml` file will exist in any package that CVE's have been entered against.
This yaml file will be both human and machine readable to enable both human inspection and scripting. These files will
allow a firmware developer to ensure that the firmware they are building is up to date with the latest CVE's. In addition
to what is in the public, the embargoed fixes described above will also have their own entries in the Security repos.

```yaml
UNIQUE_NAME:
# In most scenarios this will be the CVE, however may be whatever is deemed clearest to the consumer
    
    commit_titles: 
    # This section contains the commit titles that patched the CVE, this allows for finding the commits even if 
    # the repo was rebased. If your firmware is patched your git log will contain these git messages

        - # Upstreamed Tianocore EDK2 Patch
        # Most CVE's will only have a single, patch but additional entries may be used to confirm that a CVE has
        # been patched by any of the patches. An example of this is when a CVE has been patched internally 
        # and the upstream repo has chosen a different patch.
          
            - 'SecurityPkg: Example commit message fixing code related to the CVE' 
            - 'SecurityPkg: An additional commit message fixing a different section of code'
        - # Internal patch
            - 'SecurityPkg: Our version of the patch that chose to take'
    
    cve:
    # This is the CVE being patched
        CVE-XXXX-YYYYY
    
    date_reported:
    # This is the date the CVE was first reported
        1970-01-01
    
    description:
    # A short description of the issue take from the security issue
        'imporper bounds checking on user data for <feature>'
    
    notes:
    # An optional section where a contributor make notes they want consumers to see
        - This is a note

    files_impacted:
    # This is a list of all the files impacted by this change
        - # The lists are broken down by patch
            - SecurityPkg/Library/ExampleFile.c

    links:
    # At a minimum this section should contain links to the security issue
    # If there is a CVE link to the nist and mitre orgs for the relevant CVE
    # Any links to the patch, pull request, diff should be added here to help a consumer inspect
        - https://bugzilla.tianocore.org/show_bug.cgi?id=123
    
    other_packages_impacted:
    # This list should show any additional packages where this CVE was patched so they can be cross referenced
```
