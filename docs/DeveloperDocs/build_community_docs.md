# Building Community Docs

!!! info
    Today this process has been validated for use on Windows 11. This setup process is expected to roughly the same on
    other operating systems and none of the actual documentation source or tools should have any OS dependency.

## Get the docs repository

First, you need to clone the project mu docs repository.

``` cmd
git clone https://github.com/Microsoft/mu.git
```

## Install required tools

1. Install python. Recommended version can be viewed on [mu_devops](https://github.com/microsoft/mu_devops/blob/main/.sync/Version.njk).
2. Install pip.  Generally, this is done when installing python but can also be done as its own process.
   Details here <https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip>
3. Update pip.

    ``` cmd
    python -m pip install --upgrade pip
    ```

4. Install dependencies.

    ``` cmd
    pip install --upgrade -r requirements.txt
    ```

5. Install nodejs for more tooling
   * Install nodejs from <https://nodejs.org/en/>
   * Include npm for package management

6. Install markdownlint cli tool for linting the markdown

    ``` cmd
    npm install -g markdownlint-cli
    ```

7. Install cspell cli tool for spell checking the markdown

    ``` cmd
    npm install -g cspell
    ```

8. Install Git on your path (Required for generating dynamic repo based content during pre-process)

## General Suggested documentation workflow

1. open two command windows at the root of docs repository
    1. Window 1: Use to serve files locally
        * Use ```mkdocs serve```
        * Any changes from the *DocBuild* process will be picked up and served
    2. Window 2: Use to pre-process the source repo files
        * Run the DocBuild.py command from this window
2. Make changes to the docs in source repos or this repo and then re-run the DocBuild.py build command

## Pre-process with dynamic content from source repo(s)

1. Create "repos" folder (somewhere outside of workspace)
2. Clone all repositories for dynamic content here
3. Set each repo to the branch/commit that you want to document
4. run the *DocBuild.py* command supplying the parameters

    ```cmd
    DocBuild.py --clean --build --OutputDir docs --yml mkdocs_base.yml --RootDir ..\repos
    ```

## Pre-process with no source repo(s) content

1. run the DocBuild.py command supplying minimal parameters

    ```cmd
    DocBuild.py --clean --build --yml mkdocs_base.yml
    ```

## Clean / Remove all pre-processed content

1. use *DocBuild.py* command

    ```cmd
    DocBuild.py --clean --yml <path to yml base file> --OutputDir <docs folder>
    ```

## Check for character encoding issues

1. navigate to root of repository (should see a *docs* folder, the *mkdocs_base.yml* file, and a few other things)
2. open command window
3. run  Utf8Test python script cmd prompt

    ``` cmd
    Utf8Test.py --RootDir docs
    ```

4. should complete with no errors

!!! Note
    - Note you can also run it on any dynamic content by using a different *RootDir* parameter.
    - Use *-h* for usage to get more detailed information of any failures

## Use mkdocs to build the docs

1. navigate to root of repository (should see a *docs* folder, the *mkdocs_base.yml* file, and a few other things)
2. open command window
3. run  mkdocs build from cmd prompt at root

    ``` cmd
    mkdocs build -s -v
    ```

4. should complete with no errors

## Spell check the docs

1. navigate to root of repository (should see a *docs* folder, the *mkdocs_base.yml* file, and a few other things)
2. open command window
3. run command to spell check

    ``` cmd
    cspell "docs/**/*.md"
    ```

4. should complete with no errors

    ??? bug "False Spelling Errors"  
    If the spelling error is a false positive there are two solutions:  
        1. If it is a valid word or commonly understood term then add the word to the **cspell.json**
        config file `words` section  
        2. Update the **cspell.json** file `ignorePaths` element to ignore the entire file.

## Lint the Markdown

1. navigate to root of repository (should see a *docs* folder, the *mkdocs_base.yml* file, and a few other things)
2. open command window
3. run command to lint the markdown

    ``` cmd
    markdownlint "**/*.md"
    ```

4. Should complete with no errors.
    * Rules can be found here <https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md>
    * Configuration info here <https://github.com/DavidAnson/markdownlint#configuration>
    * Project specific configuration is is in `.markdownlint.yaml` file at the root

## Locally serve the docs

One great feature of mkdocs is how easy it is to locally serve the docs to validate your changes.

1. Use mkdocs to serve your local copy

    ``` cmd
    mkdocs serve
    ```

2. navigate to 127.0.0.1:8000 in web browser

!!! important
    If you get an error like ```Config file 'mkdocs.yml' does not exist``` you must run the pre-process step.

## Advanced doc features

We do turn on a few advanced/extension features.  Please use these carefully as they may break compatibility
if the publishing engine is changed.  Checkout the [sample syntax / test page](doc_sample_test.md) for syntax
and information.
