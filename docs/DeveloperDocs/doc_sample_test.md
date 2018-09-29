# Documentation Sample / Test file / Advanced doc features

## mkdocs macros plugin

This plugin allows providing some variables in mkdocs.yml file as well as python functions interpreted during the build process.  Today this handles
our version and build date and time. In the near future we expect to use this to compute at build time the commit hash of the other Mu repositories.  See main.py for function usage.  

https://github.com/fralau/mkdocs_macros_plugin

## Material theme

This theme provides the skin for the site.  This also provides capabilities thru plugins.  

https://squidfunk.github.io/mkdocs-material/

## Markdown Extensions

The Material theme supports markdown extensions.  Check the yml file for what extensions are currently on.  Below is more specific info.  

https://squidfunk.github.io/mkdocs-material/extensions/permalinks/
https://squidfunk.github.io/mkdocs-material/extensions/pymdown/

### Admonition plugin

This plugin in combo with the material theme provides great looking ways for doc developers to highlight parts of their message.  
Please check out: https://squidfunk.github.io/mkdocs-material/extensions/admonition/ for the capabilities and syntax.  

One example:

!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

### emoji support

Who doesn't love using emojis. Icon usage has shown to help communicate directions and cross language barriers.  
https://facelessuser.github.io/pymdown-extensions/extensions/emoji/

:smile: :heart: :thumbsup:
