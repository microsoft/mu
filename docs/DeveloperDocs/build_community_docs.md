# Building Community Docs

!!! info
    Today this process has been validated for use on Windows 10. This setup process is expected to roughly the same on other operating systems
    and none of the actual documentation source or tools should have any OS dependency.

## Get the docs

First, you need to clone the project mu docs repo.
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
    pip install mkdocs
    pip install mkdocs-material
    pip install mkdocs-macros-plugin
    pip install pymdown-extensions
    ```

5. if wanting to use spell check

    1. Install nodejs from https://nodejs.org/en/
    2. Install cspell
        ``` cmd
        npm install -g cspell
        ```

## Build the docs

1. navigate to root of repository (should see a docs folder, the mkdocs.yml file, and a few other things)
2. open command window
3. run the build
    ``` cmd
    mkdocs build -s -v
    ```
4. should complete with no errors

## Spell check the docs

1. navigate to root of repository (should see a docs folder, the mkdocs.yml file, and a few other things)
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

## Conventions and lessons learned

Please update this list as you learn more.

1. filenames should all be lowercase.  
2. filenames should use "_" to separate words and should not have spaces.  
3. all links to pages are case sensitive (when published to github the server is case sensitive)
4. use a code editor like vscode for markdown.  It has linting support and will identify issues prior to build.

## Advanced doc features

We do turn on a few advanced/extension features.  Please use these carefully as they may break compatibility if the publishing engine is changed.  Checkout the [sample syntax / test page](doc_sample_test.md) for syntax and information.
