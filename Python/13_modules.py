#!/usr/bin/python
# -*- coding: utf-8 -*-
 
'''Modules'''
# 
# In this part of the Python programming tutorial, we will talk about Python modules.
# 
# A module is a file in which we have Python code. 
# The modules in Python have the .py extension.
# 
# There are several ways to manage Python code:
# 
#     functions
#     classes
#     modules
#     packages
# 
# Python modules are used to organize Python code. 
# For example, database related code is placed inside a database module, security code in a security module etc. 
# Smaller Python scripts can have one module. 
# But larger programs are split into several modules. 
# Modules are grouped together to form packages.
# 
'''Module names'''
# 
# A module name is the file name with the .py extension. 
# When we have a file called empty.py, empty is the module name. 
# The __name__ is a variable that holds the name of the module being referenced. 
# The current module, the module being executed (called also the main module) has a special name: '__main__'. 
# With this name it can be referenced from the Python code.
# 
# We have two files: empty.py and modulename.py. 
# The second module is the main module, which is executed. 
# It imports the first module. 
# Modules are imported using the import keyword.
# 
#     $ cat empty.py
#     """
#     An empty module
#     """
# 
# This is empty.py module.
# 
# 
#     #!/usr/bin/python
#     
#     import empty
#     import sys
#     
#     print __name__
#     print empty.__name__
#     print sys.__name__
# 
# 
# In this code example we import two modules. 
# One built-in module sys and one custom module (empty). 
# We print the names of modules to the console.
# 
#     $ ./modulename.py 
#     __main__
#     empty
#     sys
# 
# The name of the module, which is being executed is always '__main__'. 
# Other modules are named after the file name. 
# Modules can be imported into other modules using the import keyword.
# 
'''Locating modules'''
# 
# When a module is imported the interpreter first searches for a built-in module with that name. 
# If not found, it then searches in a list of directories given by the variable sys.path. 
# The sys.path is a list of strings that specifies the search path for modules. 
# It consists of the current working directory, directory names specified in the PYTHONPATH environment variable plus 
# some additional installation dependent directories. 
# If the module is not found, an ImportError is raised.
# 
# 
#     #!/usr/bin/python
#     
#     import sys
#     import textwrap
#     
#     sp = sorted(sys.path)
#     dnames = ', '.join(sp)
#     
#     print textwrap.fill(dnames)
# 
# 
# The script prints all directories from sys.path variable.
# 
#     import textwrap
# 
# The textwrap module is used for easy formatting of paragraphs.
# 
#     sp = sorted(sys.path)
# 
# We retrieve a list of directories from the sys.path variable and sort them.
# 
#     dnames = ', '.join(sp)
# 
# We make a string out of the list.
# 
#     $ ./syspath.py 
#     /home/janbodnar/programming/python/modules,
#     /usr/lib/pymodules/python2.7, /usr/lib/python2.7, /usr/lib/python2.7
#     /dist-packages, /usr/lib/python2.7/dist-packages/PIL,
# ...
# 
# Sample output.

'''The import keyword'''
# 
# The import keyword can be used in several ways.
# 
#     from module import *
# 
# This construct will import all Python definitions into the namespace of another module. 
# There is one exception. Objects beginning with underscore character _ are not imported. 
# They are expected to be used only internally by the module being imported. 
# This way of importing modules is not recommended.
# 
# 
#     #!/usr/bin/python
#     
#     from math import *
#     
#     print cos(3)
#     print pi
# 
# 
# This import construct has imported all definitions from the built-in math module. 
# We can call the math functions directly, without referencing the math module.
# 
#     $ ./everything.py 
#     -0.9899924966
#     3.14159265359
# 
# The use of this import construct may result in namespace pollution. 
# We may have several objects of the same name and their definitions can be overridden.
# 
# 
#     #!/usr/bin/python
#     
#     from math import  *
#     
#     pi = 3.14
#     
#     print cos(3)
#     print pi
# 
# 
# The example will print 3.14 to the console. 
# Which may not be, what we wanted. 
# The namespace pollution may become critical in larger projects.
# 
# The following example will show definitions that are not being imported using this import construct.
# 
# 
#     #!/usr/bin/python
#     
#     """
#     names is a test module
#     """
#     
#     _version = 1.0
#     
#     names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]
#     
#     def show_names():
#        for i in names:
#           print i
#     
#     def _show_version():
#        print _version
# 
# 
# This is the names.py module.
# 
# 
#     #!/usr/bin/python
#     
#     from names import *
#     
#     print locals()
#     
#     show_names()
# 
# 
# The _version variable and the _show_version() function are not imported into the private.py module. 
# We do not see them in the namespace. 
# The locals() function give us all the definitions available in the private module.
# 
#     $ ./private.py 
#     {'__builtins__': <module '__builtin__' (built-in)>, '__file__': './private.py', 
#     'show_names': <function show_names at 0xb7dd233c>, 
#     'names': ['Paul', 'Frank', 'Jessica', 'Thomas', 'Katherine'],
#      '__name__': '__main__', '__doc__': None}
#     Paul
#     Frank
#     Jessica
#     Thomas
#     Katherine
#     from module import fun, var
# 
# This import construct imports only specific objects from a module. 
# This way we import only definitions that we need.
# 
# 
#     #!/usr/bin/python
#     
#     from math import sin, pi
#     
#     print sin(3)
#     print pi
# 
# 
# We import two objects from the math module. 
# There is no way, how we could reference other definitions like e.g. a cos function.
# 
# 
#     #!/usr/bin/python
#     
#     from names import _version, _show_version
#     
#     print _version
#     _show_version()
# 
# 
# We could also import definitions beginning with an underscore. 
# But this is a bad practice.
# 
#     $ ./imnames.py 
#     1.0
#     1.0
#     import module
# 
# The last construct is most widely used. 
# It prevents the namespace pollution and enables to access all definitions from a module.
# 
# 
#     #!/usr/bin/python
#     
#     import math
#     
#     pi = 3.14
#     
#     print math.cos(3)
#     print math.pi
#     print math.sin(3)
#     print pi
# 
# 
# In this case, we reference the definitions via the module name. 
# As we can see, we are able to use both pi variables. 
# Our definition and the one from the math module.
# 
#     $ ./widely.py 
#     -0.9899924966
#     3.14159265359
#     0.14112000806
#     3.14
# 
# 
#     #!/usr/bin/python
#     
#     # importas.py
#     
#     import math as m
#     
#     print m.pi
#     print m.cos(3)
# 
# 
# We can change the name through which we can reference the module. To do this, we use the as keyword.
# 
#     $ ./importas.py 
#     3.14159265359
#     -0.9899924966
# 
# An ImportError is raised if a module cannot be imported.
# 
# 
#     #!/usr/bin/python
#     
#     try:
#         import empty2
#     except ImportError, e:
#         print 'Failed to import:', e
# 
# 
# We have not created an empty2 module. Therefore an exception is raised.
# 
#     $ ./importerror.py
#     Failed to import: No module named empty2
# 
# Example output.
#  
'''Executing modules'''
# 
# Modules can be imported into other modules or they can be also executed. 
# Module authors often create a testing suite to test the module. 
# Only if the module is executed as a script, the __name__ attribute equals to __main__.
# 
# We will demonstrate this on a fibonacci module. 
# Fibonacci numbers is a sequence of numbers, where each is the sum of its two immediate predecessors.
# 
# 
#     #!/usr/bin/python
#     
#     """
#     A module containing the fibonacci
#     function. 
#     """
#     
#     def fib(n):
#         a, b = 0, 1
#         while b < n:
#             print b,
#             (a, b) = (b, a + b)
#     
#     
#     # testing
#     
#     if __name__ == '__main__':
#        fib(500)
# 
# 
# The module can be normally imported as usual. 
# The module can be also executed.
# 
#     $ ./fibonacci.py 
#     1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 
# If we do import the fibonacci module, the test is not executed automatically.
# 
#     >>> import fibonacci as fib
#     >>> fib.fib(500)
#     1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 
# The fibonacci module is imported and the fib() function is executed.
#  
'''The dir() function'''
# 
# The built-in dir() function gives a sorted list of strings containing the names defined by a module.
# 
# 
#     #!/usr/bin/python
#     
#     """
#     This is dirfun module 
#     """
#     
#     import math, sys
#     
#     version = 1.0
#     
#     names = ["Paul", "Frank", "Jessica", "Thomas", "Katherine"]
#     
#     def show_names():
#       
#        for i in names:
#           print i
#     
#     print dir(sys.modules['__main__']) 
# 
# 
# In this module, we import two system modules. 
# We define a variable, a list and a function.
# 
#     print dir(sys.modules['__main__']) 
# 
# The dir() function returns all the names available in the current namespace of the module. 
# '__main__' is the name of the current module. 
# The sys.modules is a dictionary that maps module names to modules which have already been loaded.
# 
#     $ ./dirfun.py
#     ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'math', 
#     'names', 'show_names', 'sys', 'version']
# 
# We can see some built-in names like '__file__' or '__name__' and all the others that we have defined.
#  
'''The globals() function'''
# 
# The globals() function returns a dictionary that represents the current global namespace. 
# It is a dictionary of global names and their values. It is the dictionary of the current module.
# 
# 
# #!/usr/bin/python
# 
#     import sys
#     import textwrap
#     
#     version = 1.0
#     
#     def myfun():
#         pass
#     
#     gl = globals()    
#     gnames = ', '.join(gl)
#     
#     print textwrap.fill(gnames) 
# 
# 
# We use the globals() function to print all the global names of the current module.
# 
#     $ ./globalsfun.py
#     __builtins__, __file__, textwrap, __package__, sys, myfun, version,
#     __name__, gl, __doc__
# 
# These are the global names of the current module.
#  
'''The __module__ attribute'''
# 
# The __module__ class attribute has the name of the module in which the class is defined.
# 
#     """
#     module animals
#     """
#     
#     class Cat:
#       pass
#     
#       
#     class Dog:
#       pass
# 
# 
# This are the contents of the animals.py file. We have two classes.
# 
# 
#     #!/usr/bin/python
#     
#     from animals import Cat
#     
#     class Being:
#         pass
#       
#       
#     b = Being()
#     print b.__module__
#     
#     c = Cat()
#     print c.__module__
# 
# 
# In this code we use the __module__ attribute.
# 
#     from animals import Cat
# 
# From the animals module, we import the Cat class.
# 
#     class Being:
#         pass
# 
# In the current module, we define a class Being.
# 
#     b = Being()
#     print b.__module__
# 
# An instance of the Being class is created. 
# We print the name of its module.
# 
#     c = Cat()
#     print c.__module__
# 
# We create an object from the Cat class. 
# We also print the module, where it was defined.
# 
#     $ ./mclass.py
#     __main__
#     animals
#     
# The current module's name is __main__. And the Cat's module name is animals.
# 
# This chapter was about modules in Python.