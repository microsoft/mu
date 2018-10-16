# Building Community Docs

!!! info
    Today this process has been validated for use on Windows 10. This setup process is expected to roughly the same on other operating systems
    and none of the actual documentation source or tools should have any OS dependency.

## Get the docs repository

First, you need to clone the project mu docs repository.
``` cmd
git clone https://github.com/Microsoft/mu.git
```

## Install required tools

1. Install python (Current suggested version is 3.7.x).  Current min requirement is python 3.4+.  Checkout python.org for directions.
2. Install pip.  Generally, this is done when installing python but can also be done as its own process.  Details here https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip
3. Update pip.
    ``` cmd
    python -m pip install --upgrade pip
    ```
4. Install dependencies.
    ``` cmd
    pip install --upgrade -r requirements.txt
    ```

5. if wanting to use spell check
    * Install nodejs from https://nodejs.org/en/
    * Install cspell
        ``` cmd
        npm install -g cspell
        ```
6. Install Git on your path (Required for generating dynamic repo based content during preprocess)

## General Suggested documentation workflow

1. open two command windows at the root of docs repository  
    1. Window 1: Use to serve files locally
        * Use ```mkdocs serve``` 
        * Any changes from the *DocBuild* process will be picked up and served
    2. Window 2: Use to preprocess the source repo files
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

    * Note you can also run it on any dynamic content by using a different *RootDir* parameter.  
    * Use *-h* for usage to get more detailed information of any failures

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
    cspell docs/**/*.md
    ```
4. should complete with no errors

??? bug "False Spelling Errors"
    If the spelling error is a false positive there are three solutions:

    1. If its a firmware or UEFI word:  Add the word to the **uefi-words.txt** file
    2. Add the word to the **cspell.json** config file `words` section
    3. Update the **cspell.json** file `ignorePaths` element to ignore the entire file.

## Locally serve the docs

One great feature of mkdocs is how easy it is to locally serve the docs to validate your changes.

1. Use mkdocs to serve your local copy
    ``` cmd
    mkdocs serve
    ```
2. navigate to 127.0.0.1:8000 in web browser

!!! important
    If you get an error like ```Config file 'mkdocs.yml' does not exist``` you must run the preprocess step.

## Conventions and lessons learned

Please update this list as you learn more.

1. filenames should all be lowercase.  
2. filenames should use "_" to separate words and should not have spaces.  
3. all links to pages are case sensitive (when published to GitHub the server is case sensitive)
4. use a code editor like vscode for markdown.  It has linting support and will identify issues prior to build.

## Advanced doc features

We do turn on a few advanced/extension features.  Please use these carefully as they may break compatibility if the publishing engine is changed.  Checkout the [sample syntax / test page](doc_sample_test.md) for syntax and information.
