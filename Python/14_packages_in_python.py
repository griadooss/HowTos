#!/usr/bin/python
# -*- coding: utf-8 -*-
 
'''Packages in Python'''
# 
# In this part of the Python programming tutorial, we will talk about packages.
# 
# A package is a collection of modules which have a common purpose. 
# Technically a package is a directory which must have one special file called __init__.py.
# 
# There are several ways to manage Python code:
# 
#     functions
#     classes
#     modules
#     packages
# 
# When we deal with large projects containing hundreds or thousands of modules, using packages is crucial. 
# For example, we could put all database related modules in a database package, user interface code in ui package etc.
# 
#   
#     read.py
#     constants/
#               __init__.py
#               names.py 
# 
# In our current working directory we have a constants directory and a read.py script.
# 
# The constants directory has two files. __init__.py file makes constants a Python package. 
# The names.py is an ordinary module.
# 
#     from names import names
#     
#     print "initializing constants package"
# 
# The __init__.py file is initialized when the package is imported. 
# Here we can control, what object will be available to the module, which imports the package.
# 
# 
#     #!/usr/bin/python
#     
#     # names.py
#     
#     names = ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
# 
# 
# The names.py module has a tuple of 5 names.
# 
#     #!/usr/bin/python
#     
#     # read.py
#     
#     import constants
#     
#     print constants.names
# 
# 
# Finally, the read.py script imports the constants package. 
# We print the names tuple from the package.
# 
#     $ ./read.py 
#     initializing constants package
#     ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
# 
# We can also create subpackages. 
# To access subpackages, we use the dot operator.
# 
#     read.py
#     constants/
#               __init__.py
#               names.py 
#               numbers/
#                        __init__.py
#                        integers.py
# 
# This is the new hierarchy. 
# We have a subpackage called numbers.
# 
#     from integers import integers
# 
# The __init__.py file in the numbers package has this one line.
# 
# 
#     #!/usr/bin/python
#     
#     # integers.py
#     
#     
#     integers = (2, 3, 45, 6, 7, 8, 9)
# 
# 
# The integers module defines a tuple of 7 integers. 
# This tuple will be accessed from the read.py script.
# 
# 
#     #!/usr/bin/python
#     
#     # read.py
#     
#     import constants
#     import constants.numbers as int
#     
#     print constants.names
#     print int.integers
# 
# 
# The read.py script is modified a bit.
# 
#     $ ./read.py 
#     initializing constants package
#     ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
#     (2, 3, 45, 6, 7, 8, 9)
# 
# 
# The from package import * construct in a __init__.py file could cause problems on some older operating systems. 
# Therefore a special variable __all__ has been introduced. 
# This variable controls what objects will be imported from a package.
# 
#     __all__ = ["names"]
#     
#     print "initializing constants package"
# 
# Here we modify the __init__.py file in the constants directory.
# 
# 
#     #!/usr/bin/python
#     
#     # read.py
#     
#     from constants import names
#     import constants.numbers as int
#     
#     print names.names
#     print int.integers
# 
# 
# We also change the read.py script accordingly.
# 
#     $ ./read.py
#     initializing constants package
#     ('Jack', 'Jessica', 'Robert', 'Lucy', 'Tom')
#     (2, 3, 45, 6, 7, 8, 9)
# 
# The output is the same.
# 
# In this chapter, we have covered packages in Python.