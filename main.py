#
# This uses the macro plugin 
# https://github.com/fralau/mkdocs_macros_plugin
#
# To install use pip install mkdocs-macros-plugin
#

def declare_variables(variables, macro):
    """
    This is the hook for the functions

    - variables: the dictionary that contains the variables
    - macro: a decorator function, to declare a macro.
    """

    variables['version'] = "0.4"

    import datetime
    @macro
    def buildtime():
      return str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

''' 

SAMPLE OF HOW TO USE MACROS.
    @macro
    def bar(x):
        return (2.3 * x) + 7



    # If you wish, you can  declare a macro with a different name:
    def f(x):
        return x * x

    macro(f, 'barbaz')

    # or to export some predefined function
    import math
    macro(math.floor) # will be exported as 'floor'

'''