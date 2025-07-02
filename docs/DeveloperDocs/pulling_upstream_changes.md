# Pulling Upstream Changes into Project Mu Repositories

Project Mu is based on the upstream EDK2 project, which serves as its foundational codebase. The EDK2 community actively
accepts bug fixes and code improvements, ensuring a robust and evolving platform. Sometimes, changes that are merged into
EDK2 need to be added to Project Mu before the next scheduled integration. This document describes the process for
applying such upstream changes to Project Mu in a manner that enables maintainers to track the provenance of the commits.

## Cherry-Pick Process

To cherry-pick changes from the EDK2 repository into a Project Mu repository, follow these steps:

1. **Identify the Commit(s):**
    - Locate the commit hash(es) in the EDK2 repository that you want to apply to Project Mu.

2. **Sync Your Local Repository:**
    - Ensure your local Project Mu repository is up to date:

      ```sh
      git checkout <target-branch>
      git pull origin <target-branch>
      ```

3. **Add the EDK2 Remote (if not already added):**

    ```sh
    git remote add edk2 https://github.com/tianocore/edk2.git
    git fetch edk2
    ```

4. **Cherry-Pick the Commit(s):**
    - Use the commit hash from EDK2:

      ```sh
      git cherry-pick <edk2-commit-hash> -x
      ```

    - If conflicts arise, resolve them, then continue:

      ```sh
      git add <resolved-files>
      git cherry-pick --continue
      ```

    - Amend the commit message to contain `[Cherry-Pick]` in the title.

    ```sh
    git commit --amend
    ```

5. **Document the Change:**
    - In the commit message, reference the original EDK2 commit hash and provide a brief description.
    - Example:

      ```sh
      [Cherry-pick] <original commit title>
      ```

6. **Push the Changes:**

    ```sh
    git push origin <target-branch>
    ```

7. **Create a Pull Request:**
    - Open a pull request in the Project Mu repository.
    - Clearly indicate that this is a cherry-pick from EDK2 and link to the original commit(s).

This process ensures traceability and helps maintainers track upstream changes integrated into Project Mu.

## Handling Merge Commits

When cherry-picking from EDK2, you may encounter merge commits. These require special handling because
`git cherry-pick` does not support merge commits directly. Here are some resources and strategies for dealing
with them:

- [Git Documentation: Cherry-pick a merge commit](https://git-scm.com/docs/git-cherry-pick#_cherry_picking_a_merge_commit)
- [Git Documentation: Resolving merge conflicts](https://git-scm.com/docs/git-merge#_how_conflicts_are_presented)

These resources provide detailed guidance and examples for handling merge commits during upstream integration.
