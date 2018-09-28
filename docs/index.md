# Welcome to Project Mu

![Greek Mu](img/mu.png)

Project Mu is a modular adaptation of TianoCore's [edk2](https://github.com/tianocore/edk2) tuned for building modern devices using a scalable, maintainable, and reusable pattern.  Mu is built around the idea that shipping and **maintaining** a UEFI product is an ongoing collaboration between numerous partners.  For too long the industry has built products using a "forking" model combined with copy/paste/rename and with each new product the maintenace burden grows to such a level that updates are near impossible due to cost and risk.  

Project Mu also tries to address the complex business relationships and legal challenges facing partners today.  To build most products it often requires both closed-source, proprietary assets as well as open source and industry standard code.  The distributed build system and multi-repository design allows product teams to keep code separate and connected to their original source while respecting legal and business boundaries.  

Project Mu originated from building modern Windows PCs but its patterns and design allows it to be scaled down or up for whatever the final product's intent.  IoT, Server, PC, or any other form factor should be able to leverage the content.  

## Primary Goals
Initially this project will focus on two central goals. 

### &#x1F539; Share our active code tree to both solicit feedback and entice partners to collaborate.  
Project Mu is an active project.  This is not a side project, mirror, clone, or example.  This is the same code used today on many of Microsoft's 1st party devices and it will be kept current because it must be to continue to enable shipping products.  

### &#x1F539; Promote, evangelize, and support an industry shift to a more collaborative environment so we all can build and maintain products with lower costs and higher quality.  
Today's open source projects although extremely valuable are very resource intensive to interact with.  This friction leads to major industry players avoiding public interaction thus diminishing the overall community’s value.  The modern era of open source projects has incorporated new tools and procedures to lower this friction and it is our goal to leverage those tools.  GitHub provides issue tracking, Pull Requests, Gated builds, tracked/required web-based code reviews, and CI/CD (Continuous builds and testing).   It is our belief that by leveraging and extending this automation and workflow we can lower the friction and foster a safe place for all contributors to work.  


## Guiding Principles

* Less is More [*](faq)
* Be open to change / flexible - Keep learning.  If it was easy this would have been solved before
* Design for code reuse 
* Leverage tools / invest in automation

## Navigation

Have a look around this site to see what is Project Mu, why is it different, how to work within or extend it, as well as where everything is located.

## Having trouble?

Skim the [FAQ](faq)

Contact info to come.

## Reporting Issues

Refer to [Contributing](How/contributing)

## Contributing

Refer to [Contributing](How/contributing)

## License

Refer to [License](license)

Version: {{version}}  
Build Time: {{buildtime()}}