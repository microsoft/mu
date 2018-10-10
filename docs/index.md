# Welcome to Project Mu

![Greek Mu](img/project_mu.png)

Project Mu is a modular adaptation of TianoCore's [edk2](https://github.com/tianocore/edk2) tuned for building modern devices using a scalable, maintainable, and reusable pattern.  Mu is built around the idea that shipping and **maintaining** a UEFI product is an ongoing collaboration between numerous partners.  For too long the industry has built products using a "forking" model combined with copy/paste/rename and with each new product the maintenance burden grows to such a level that updates are near impossible due to cost and risk.  

Project Mu also tries to address the complex business relationships and legal challenges facing partners today.  To build most products it often requires both closed-source, proprietary assets as well as open source and industry standard code.  The distributed build system and multi-repository design allow product teams to keep code separate and connected to their original source while respecting legal and business boundaries.  

Project Mu originated from building modern Windows PCs but its patterns and design allow it to be scaled down or up for whatever the final product's intent.  IoT, Server, PC, or any other form factor should be able to leverage the content.  

## Primary Goals

Initially, this project will focus on two central goals.

### Share our active code tree to both solicit feedback and entice partners to collaborate

Project Mu is an active project.  This is not a side project, mirror, clone, or example.  This is the same code used today on many of Microsoft's 1st party devices and it will be kept current because it must be to continue to enable shipping products.  

### Promote, evangelize, and support an industry shift to a more collaborative environment so we all can build and maintain products with lower costs and higher quality

Today's open source projects although extremely valuable are very resource intensive to interact with.  This friction leads to major industry players avoiding public interaction thus diminishing the overall community’s value.  The modern era of open source projects has incorporated new tools and procedures to lower this friction and it is our goal to leverage those tools.  GitHub provides issue tracking, Pull Requests, Gated builds, tracked/required web-based code reviews, and CI/CD (Continuous builds and testing).   It is our belief that by leveraging and extending this automation and workflow we can lower the friction and foster a safe place for all contributors to work.  

## Guiding Principles

* Less is More [*](faq#is-this-really-following-less-is-more)
* Be open to change / flexible - Keep learning.  If it was easy this would have been solved before
* Design for code reuse
* Leverage tools / invest in automation

## Navigation

Have a look around this site to see what is Project Mu.  Start by reviewing the details of the community and our process.  See how to interact and get involved, why it's different, how to work within or extend it, as well as where everything is located.  Finally, explore the [Developer Docs](DeveloperDocs/developer_docs.md) if you want to review more in-depth details.  

## Having trouble?

Skim the [FAQ](faq.md)

## Road map

### Days

* [x] Engaging with existing partners to collect feedback
* [ ] Pull Request documentation & gates
* [ ] Automated builds & compile tests of all repos
* [ ] Developer documentation on building & testing
* [ ] Determine communication venue (e.g. email list, Slack, Teams, ...), currently testing MS Teams

### Weeks

* [ ] Update to latest, stable EDK2 release
* [ ] Automated build & tests on a public platform
* [ ] Automated build & tests on Surface devices
* [ ] Feature documentation
* [ ] Draft process for security collaboration with partners & Tianocore
* [ ] Documentation on Governance
* [ ] Announce project & evangelize

### Months

* [ ] Add support for partner-requested compilers and Containerized builds

## Join Us

Contact info and additional methods to collaborate coming soon.

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Reporting Issues

Short answer: Open a github issue.  
More details: [Contributing](How/contributing)

## Contributing

Short answer: Open a pull request.  
More details: [Contributing](How/contributing)

## License

Refer to [License](license)

Version: {{version}}  
Build Time: {{buildtime()}}
