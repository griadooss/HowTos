#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''Introspection in Python'''
# 
# In this part of the Python programming tutorial, we will talk about introspection.
# 
# Introspection is an act of self examination. 
# In computer programming, introspection is the ability to determine the type of an object at runtime. 
# Python programming language has a large support of introspection. 
# Everything in Python is an object. 
# Every object in Python may have attributes and methods. 
# By using introspection, we can dynamically inspect Python objects.
#  
'''The dir() function'''
# 
# The dir() function is the most important function when doing introspection. 
# The function returns a sorted list of attributes and methods belonging to an object.
# 
#     >>> dir(())
#     ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', 
#     '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
#     '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', 
#     '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', 
#     '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', 
#     '__str__', '__subclasshook__', 'count', 'index']
# 
# Here we see an output of the dir() function for a tuple object.
# 
#     >>> print ().__doc__
#     tuple() -> empty tuple
#     tuple(iterable) -> tuple initialized from iterable's items
# 
# 
# If the argument is a tuple, the return value is the same object.
# 
# Our investigation showed that there is a __doc__ attribute for a tuple object.
# 
# 
#     #!/usr/bin/python
#     
#     # dir.py
#     
#     import sys
#     
#     class Object:
#        def __init__(self):
#           pass
#        def examine(self):
#           print self
#     
#     
#     o = Object()
#     
#     print dir(o)
#     print dir([])
#     print dir({})
#     print dir(1)
#     print dir()
#     print dir(len)
#     print dir(sys)
#     print dir("String")
# 
# 
# The example examines several objects using the dir() function. 
# A user defined object, native data types, a function, a string or a number.
# 
# Without any argument, the dir() returns names in the current scope.
# 
#     >>> dir()
#     ['__builtins__', '__doc__', '__name__', '__package__']
#     >>> import sys
#     >>> import math, os
#     >>> dir()
#     ['__builtins__', '__doc__', '__name__', '__package__', 'math', 'os', 'sys']
# 
# We execute the dir() function before and after we include some modules.
#  
'''The type(), id() functions'''
# 
# The type() function returns the type of an object.
# 
# 
#     #!/usr/bin/python
#     
#     # types.py
#     
#     import sys
#     
#     
#     def function(): pass
#     
#     class MyObject():
#        def __init__(self):
#           pass
#     
#     o = MyObject()
#     
#     print type(1)
#     print type("")
#     print type([])
#     print type({})
#     print type(())
#     print type(object)
#     print type(function)
#     print type(MyObject)
#     print type(o)
#     print type(sys)
# 
# 
# The example print various types of objects to the console screen.
# 
#     $ ./types.py 
#     <type 'int'>
#     <type 'str'>
#     <type 'list'>
#     <type 'dict'>
#     <type 'tuple'>
#     <type 'type'>
#     <type 'function'>
#     <type 'classobj'>
#     <type 'instance'>
#     <type 'module'>
# 
# Output of the types.py script.
#  
'''The id() returns a special id of an object.'''
# 
# 
#     #!/usr/bin/python
#     
#     # ids.py
#     
#     import sys
#     
#     def fun(): pass
#     
#     class MyObject():
#        def __init__(self):
#           pass
#     
#     o = MyObject()
#     
#     print id(1)
#     print id("")
#     print id({})
#     print id([])
#     print id(sys)
#     print id(fun)
#     print id(MyObject)
#     print id(o)
#     print id(object)
# 
# 
# The code example prints ids of various objects, both built-in and custom.
# 
#     $ ./ids.py 
#     135717024
#     3084304536
#     3084111220
#     3084104940
#     3084304500
#     3084112812
#     3084074556
#     3084130444
#     135568640
#  
'''The sys module'''
# 
# The sys module provides access to system specific variables and functions used or maintained by the interpreter 
# and to functions that interact strongly with the interpreter. 
# The module allows us to query about the Python environment.
# 
#     >>> import sys
#     >>> sys.version
#     '2.7.2+ (default, Oct  4 2011, 20:03:08) \n[GCC 4.6.1]'
#     >>> sys.platform
#     'linux2'
#     >>> sys.path
#     ['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-linux2', 
#     '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', 
#     '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', 
#     '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PIL', 
#     '/usr/lib/python2.7/dist-packages/gst-0.10', '/usr/lib/python2.7/dist-packages/gtk-2.0', 
#     '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']
# 
# In the above code we examine the Python version, platform and search path locations.
# 
# We will have another four variables of the sys module. 
# We can use the dir() function to get a full list of variables and functions of the sys module.
# 
#     >>> sys.maxint
#     2147483647
#     >>> sys.executable
#     '/usr/bin/python'
#     >>> sys.argv
#     ['']
#     >>> sys.byteorder
#     'little'
# 
# The example presents maxint, executable, argv, and byteorder attributes of the sys module.
# 
#     >>> sys.maxint
#     2147483647
# 
# The maxint is the largest positive integer supported by Python's regular integer type.
# 
#     >>> sys.executable
#     '/usr/bin/python'
# 
# The executable is a string giving the name of the executable binary for the Python interpreter, 
# on systems where this makes sense.
# 
#     >>> sys.argv
#     ['']
# 
# This gives a list of command line arguments passed to a Python script.
# 
#     >>> sys.byteorder
#     'little'
# 
# The byteorder is an indicator of the native byte order. 
# This will have the value 'big' on big-endian (most-significant byte first) platforms, 
# and 'little' on little-endian (least-significant byte first) platforms.
#  
'''Various'''

# Next we will show various other ways of inspecting our objects.
# 
# 
#     #!/usr/bin/python
#     
#     # attr.py
#     
#     def fun(): pass
#     
#     
#     print hasattr(object, '__doc__')
#     print hasattr(fun, '__doc__')
#     print hasattr(fun, '__call__')
#     
#     print getattr(object, '__doc__')
#     print getattr(fun, '__doc__')
# 
# 
# The hasattr() function checks if an object has an attribute. 
# The getattr() function returns the contents of an attribute if there are some.
# 
#     $ ./attr.py 
#     True
#     True
#     True
#     The most base type
#     None
# 
# The isinstance function checks if an objects is an instance of a specific class.
# 
#     >>> print isinstance.__doc__
#     isinstance(object, class-or-type-or-tuple) -> bool
#     
#     Return whether an object is an instance of a class or of a subclass thereof.
#     With a type as second argument, return whether that is the object's type.
#     The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for
#     isinstance(x, A) or isinstance(x, B) or ... (etc.).
# 
# We can get the describtion of a function interactively.
# 
# 
#     #!/usr/bin/python
#     
#     # instance.py
#     
#     
#     class MyObject():
#        def __init__(self):
#           pass
#     
#     o = MyObject()
#     
#     print isinstance(o, MyObject)
#     print isinstance(o, object)
#     print isinstance(2, int)
#     print isinstance('str', str)
# 
# 
# As we know, everything is an object in Python. 
# Even numbers or strings. 
# The object is a base type of all objects in Python. 
# That is why isinstance(o, object) returns True.
# 
#     $ ./instance.py 
#     True
#     True
#     True
#     True
# 
# The issubclass() function checks, if a specific class is a derived class of another class.
# 
# 
#     #!/usr/bin/python
#     
#     # subclass.py
#     
#     class Object():
#        def __init__(self):
#           pass
#     
#     class Wall(Object):
#        def __init__(self):
#           pass
#     
#     print issubclass(Object, Object)
#     print issubclass(Object, Wall)
#     print issubclass(Wall, Object)
#     print issubclass(Wall, Wall)
# 
# 
# In our code example, the Wall class is a subclass of the Object class. 
# Object and Wall are also subclasses of themselves. 
# The Object class is not a subclass of class Wall.
# 
#     $ ./subclass.py 
#     True
#     False
#     True
#     True
# 
# The __doc__ attribute gives some documentation about an object and the __name__ attribute holds the name of the object.
# 
# 
#     #!/usr/bin/python
#     
#     # namedoc.py
#     
#     def noaction():
#        '''A function, which does nothing'''
#        pass
#     
#     
#     funcs = [noaction, len, str]
#     
#     for i in funcs:
#        print i.__name__
#        print i.__doc__
#        print "-" * 75
# 
# 
# In our example, we crete a list of three functions: one custom and two native. 
# We go through the list and print the __name__ and the __doc__ attributes.
# 
#     $ ./namedoc.py
#     noaction
#     A function, which does nothing
#     ---------------------------------------------------------------------------
#     len
#     len(object) -> integer
#     
#     Return the number of items of a sequence or mapping.
#     ---------------------------------------------------------------------------
#     str
#     str(object) -> string
#     
#     Return a nice string representation of the object.
#     If the argument is a string, the return value is the same object.
#     ---------------------------------------------------------------------------
# 
# Output.
# 
# Finally, there is also a callable() function. 
# The function checks if an object is a callable object. 
# Or in other words, if an object is a function.
# 
# 
#     #!/usr/bin/python
#     
#     # callable.py
#     
#     class Car:
#           
#         def setName(self, name):
#             self.name = name    
#     
#     def fun():
#         pass
#     
#     c = Car()    
#         
#     print callable(fun)
#     print callable(c.setName)
#     print callable([])
#     print callable(1)
#     In the code example we check if three objects are callables.
#     
#     print callable(fun)
#     print callable(c.setName)
# 
# 
# The fun() function and the setName() method are callables. 
# (A method is a function bound to an object.)
# 
#     $ ./callable.py
#     True
#     True
#     False
#     False
# 
# In this part of the Python tutorial, we have talked about introspection in Python. 
# More tools for doing introspection can be found in the inspect module.