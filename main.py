def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    """

    # Due to what seems like a bug in mkdocs-macros-plugin this module must exist with this
    # function.  I have opened a bug https://github.com/fralau/mkdocs_macros_plugin/issues/16
    # and hopefully in the future this module can be removed.
    pass

