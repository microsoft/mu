# Project Mu

[![Build status](https://dev.azure.com/projectmu/mu/_apis/build/status/Publish%20Mu)](https://dev.azure.com/projectmu/mu/_build/latest?definitionId=3)

This repository contains documentation of the Project Mu.  

You can find the documentation at <https://microsoft.github.io/mu/>.

## How to build the docs

We are using [**MkDocs**](https://www.mkdocs.org) to build the documentation.

The following gives you a rough overview how to serve it locally:

* Run `pip install --upgrade -r requirements.txt`
* Run `DocBuild.py --Build --Clean --yml mkdocs_base.yml`
* Run `mkdocs serve`

Now you should be able to open <http://127.0.0.1:8000/mu> on your machine.

A more detailed information how to build this project can be found
[here](https://microsoft.github.io/mu/DeveloperDocs/build_community_docs/).
