# Steps for a New Integration

## Overview

Below, you will find a checklist of the steps that should be followed by any project maintainers when performing a new
upstream integration. This is for reference by the maintainers and by any of the community interested in the process.

We will do our best to keep this up to date, so it's an excellent reference for what to expect if you're waiting on an
integration.

## 1) Announce

Advertist the upcoming update, where it will start from, how long it will take, and what will happen with the existing release branch afterwards.

## 2) Rebase and Test

Start with the repos.
    Create rebase_naive branch
    Update readme, all CI badges, etc.
    Naive rebase
    Any amount of cleaning
        Diff against naive
    Create the rebase staging branch when ready
        On the critical 3, this will have an extra commit
    Tag X_Rebase
    Start working on CI

    Clean up all rebase branches

## 3) Boot a Reference Platform

Document changes for each repo.

## 4) Change Default Branches