# Developer Docs

## Philosophy

Documentation is critical.  There is a steep learning curve in UEFI and no amount of documentation will change that, but at a minimum quick, clear, and easy documentation can help everyone adopt features faster and with higher confidence.  Our documentation system will focus on making this an easy, low friction, and collaborative process.  The pull request process will eventually compel developers to submit documentation whenever they submit new components and refactoring.

Documentation will be done in markdown as this has the benefit of being easily readable in both plain text as well as transformed into a richer experience. It also is quick to learn and to write. Currently, we leverage mkdocs as our publishing engine but since all content is in markdown it could be transitioned to another engine without significant reinvestment.  

## Community documentation

This content is documented in static markdown files within the Project Mu repository.  We leverage mkdocs to generate web-hosted content on every change and host these using github.io.   These static files focus on how the project and community interact.  We strongly encourage contribution and follow the standard PR model for all changes, big and small.  

## Developer documentation

This content is documented in a couple of ways.

1. There are static markdown files in the Project Mu repository.  This contains details about high level concepts, howto articles, and features of the project and all repos within Project Mu.  Examples: Code layout, git usage, tools, building, packaging, etc.  
2. There is repo and package level documentation for features.  These are also static markdown files but these are contained within the repo that contains the feature.  A “docs” folder for each repo and each package will host this content.   Changes will also follow the standard PR model for the containing repo.
3. Next, there is feature and instance documentation.  This should inform a developer interested in the implementation specifics of what this module is and what additional requirements it has including code dependencies and limitations.  This should be documented in markdown files located with the component.  These should be updated whenever the component is updated and should be part of a code PR.  
4. Finally, for API and traditional functional documentation, our current stance is this is required in code (public APIs) but the published documentation (doxygen html, pdf, etc) is not necessary.  Code tools like vscode already provide a lower friction method to index, find def, and search that uses this content directly embedded in the code.
