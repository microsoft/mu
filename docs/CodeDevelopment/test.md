# Tests

Testing firmware is hard.  Lets just stop there. :sob: If you want to read on please do at your own risk.  Project Mu supports a few types of testing and this page will help provide some high level info and links for more information.  

## Static Code Tests (analysis)

*Mu_Build* provides a framework for running static tests on the code base.  Simple tests like character encoding are examples.  In Project Mu we are working to expand this set of tests to include checking guids, checking for library classes, etc.

## UEFI Shell Based Unit Tests

## UEFI Shell Based Functional Tests

## UEFI Shell Based Audit Tests

## Testing Python

* Create pytest and/or python unit-test compatible tests.
* Make sure the python code passes the `flake8` "linter"