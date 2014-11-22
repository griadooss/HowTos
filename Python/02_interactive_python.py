#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Interactive Python'''
# 
# In this part of the Python programming tutorial, we will talk about interactive Python interpreter.
#  
# Python code can be launched in two basic ways. 
# As a script or inside an interactive interpreter.
#  
#     #!/usr/bin/python
#      
#     # first.py
#      
#     print "The Python tutorial"
#  
#  
# This is an example of a small Python script. It is launched from a UNIX shell.
#  
#     $ ./first.py 
#     The Python tutorial
#
'''Interactive interpreter'''
#  
# Another way of running Python code is the interactive Python interpreter. 
# The Python interpreter is very useful for our explorations. 
# When we quickly want to test some basic functionality of the Python language and we don't want to write a whole script. 
# To get the interactive interpreter, we execute the Python command on our favourite shell.
# 
# 
#     $ python
#     Python 2.7.2+ (default, Jul 20 2012, 22:12:53) 
#     [GCC 4.6.1] on linux2
#     Type "help", "copyright", "credits" or "license" for more information.
#     >>> 
# 
# 
# This is the welcome message of the Python interpreter. 
# We see the version of Python on our machine. 
# In our case it is Python 2.7.2. 
# The ">>>" is the prompt used in the Python interactive mode. 
# To leave the interpreter and return back to the shell, we can type Ctrl+D or quit(). 
# Typing Ctrl+L will clear the screen of the Python interpreter.
#  
# Now we can query for some useful information.
# 
# 
# >>> credits
#     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
#     for supporting Python development.  See www.python.org for more information.
#  
#  
# If we type credits we get some information about organizations involved in Python development.
#  
#  
#     >>> copyright
#     Copyright (c) 2001-2011 Python Software Foundation.
#     All Rights Reserved.
#      
#     Copyright (c) 2000 BeOpen.com.
#     All Rights Reserved.
#      
#     Copyright (c) 1995-2001 Corporation for National Research Initiatives.
#     All Rights Reserved.
#      
#     Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
#     All Rights Reserved.
#  
#  
# The copyright command gives the copyright of the Python programming language.
# 
# The license() command provides several pages regarding the license of Python.

'''Getting help'''
#  
# The help command provides some help about Python.
#  
#  
#     >>> help
#     Type help() for interactive help, or help(object) for help about object.
#     >>> 
#  
#  
# We can use the command in two ways. 
# Either we can get some help about a specific object or we enter a interactive help mode.
#  
# For example, if we type help(True), we get some information about bool objects.
#  
#  
# Help on bool object:
#  
#     class bool(int)
#      |  bool(x) -> bool
#      |  
#      |  Returns True when the argument x is true, False otherwise.
#      |  The builtins True and False are the only two instances of the class bool.
#      |  The class bool is a subclass of the class int, and cannot be subclassed.
#      |  
#      |  Method resolution order:
#      |      bool
#      |      int
#      |      object
#      |  
#      |  Methods defined here:
#      |  
#      |  __and__(...)
#      |      x.__and__(y) <==> x&y
#  
#  
#  ...
# If the topic is larger than one page, we can scroll it using the arrows. 
# If we want to quit the topic, we press the q key.
#  
# If we type help() we get the interactive help mode of the interpreter.
#  
#  
#     >>> help()
#  
# Welcome to Python 2.7!  This is the online help utility.
#  
# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at http://docs.python.org/tutorial/.
#  
# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".
#  
# To get a list of available modules, keywords, or topics, type "modules",
# "keywords", or "topics".  Each module also comes with a one-line summary
# of what it does; to list the modules whose summaries contain a given word
# such as "spam", type "modules spam".
#  
#     help> 
#      
#      
#     To leave the help mode and return to the interpreter, we use the quit command.
#      
#     The keywords command gives a list of available keywords in Python programming language.
#     
#     
#     help> keywords
#      
#     Here is a list of the Python keywords.  Enter any keyword to get more help.
#      
#     and                 elif                if                  print
#     as                  else                import              raise
#     assert              except              in                  return
#     break               exec                is                  try
#     class               finally             lambda              while
#     continue            for                 not                 with
#     def                 from                or                  yield
#     del                 global              pass
#  
#  
# If we type any of the keywords, we get some help on it.
#  
# The modules command gives a list of available modules. 
# Again, typing a name of the module will provide additional help.
#  
# Finally, we have the topics command.
#  
#  
#     help> topics
#      
#     Here is a list of available topics.  Enter any topic name to get more help.
#      
#     ASSERTION           DEBUGGING           LITERALS            SEQUENCEMETHODS2
#     ASSIGNMENT          DELETION            LOOPING             SEQUENCES
#     ATTRIBUTEMETHODS    DICTIONARIES        MAPPINGMETHODS      SHIFTING
#     ATTRIBUTES          DICTIONARYLITERALS  MAPPINGS            SLICINGS
#     AUGMENTEDASSIGNMENT DYNAMICFEATURES     METHODS             SPECIALATTRIBUTES
#     BACKQUOTES          ELLIPSIS            MODULES             SPECIALIDENTIFIERS
#     BASICMETHODS        EXCEPTIONS          NAMESPACES          SPECIALMETHODS
#     BINARY              EXECUTION           NONE                STRINGMETHODS
#     BITWISE             EXPRESSIONS         NUMBERMETHODS       STRINGS
#     BOOLEAN             FILES               NUMBERS             SUBSCRIPTS
#     CALLABLEMETHODS     FLOAT               OBJECTS             TRACEBACKS
#     CALLS               FORMATTING          OPERATORS           TRUTHVALUE
#     CLASSES             FRAMEOBJECTS        PACKAGES            TUPLELITERALS
#     CODEOBJECTS         FRAMES              POWER               TUPLES
#     COERCIONS           FUNCTIONS           PRECEDENCE          TYPEOBJECTS
#     COMPARISON          IDENTIFIERS         PRINTING            TYPES
#     COMPLEX             IMPORTING           PRIVATENAMES        UNARY
#     CONDITIONAL         INTEGER             RETURNING           UNICODE
#     CONTEXTMANAGERS     LISTLITERALS        SCOPING             
#     CONVERSIONS         LISTS               SEQUENCEMETHODS1   
#      
#  
# The topics command gives a list of topics regarding Python programming language. 
# Here we can find some useful information.
#
#
'''Python Code'''
# 
# Now we will see the real benefit of the Python interpreter.
#  
#  
#     >>> 2 + 4
#     6
#     >>> 5 * 56
#     280
#     >>> 5 - 45
#     -40
#     >>> 
#  
#  
# Python interpreter can be used as a calculator. 
# Each expression is executed right away and the result is shown on the screen.
#  
#  
#     >>> a = 3
#     >>> b = 4
#     >>> a**b
#     81
#     >>> a == b
#     False
#     >>> a < b
#     True
#     >>>
#  
#  
# We can define variables and perform operations on them.
#  
#  
#     >>> import random
#     >>> dir(random)
#     ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 
#     'SystemRandom', 'TWOPI', 'WichmannHill', '_BuiltinMethodType', '_MethodType',
#     '__all__', '__builtins__', '__doc__', '__file__', '__name__', '_acos', 
#     '_ceil', '_cos', '_e', '_exp', '_hexlify', '_inst', '_log', '_pi', '_random',
#     '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 
#     'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss', 
#     'getrandbits', 'getstate', 'jumpahead', 'lognormvariate', 'normalvariate',
#     'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed',
#     'setstate', 'shuffle', 'uniform', 'vonmisesvariate', 'weibullvariate']
#     >>> 
#  
#  
# Here we imported a random module. 
# With the dir() function, we further explore the random module.
#  
# With the help of the special __doc__ string, we can get help on a specific function.
#  
#  
#     >>> print random.seed.__doc__
#     Initialize internal state from hashable object.
#      
#             None or no argument seeds from current time or from an operating
#             system specific randomness source if available.
#      
#             If a is not None or an int or long, hash(a) is used instead.
#     >>> 
#  
#  
# The locals() command shows our current local namespace.
#  
#  
#     >>> locals()
#     {'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', 
#     'random': <module 'random' from '/usr/lib/python2.5/random.pyc'>, '__doc__': None}
#  
#  
# We can see the random module that we have previously imported.
#  
#  
#     >>> class Car:
#     ...   pass
#     ... 
#     >>> def function():
#     ...   pass
#     ... 
#     >>> for i in range(5):
#     ...   print i
#     ... 
#     0
#     1
#     2
#     3
#     4
#     >>> 
#  
#  
# We can define our own classes, functions or use control flow structures. 
# We must not forget to indent the code. 
# To finish each of these blocks of code, we type enter key twice.
#  
#  
#     >>> import os
#     >>> os.getcwd()
#     '/home/vronskij/programming/python'
#     >>> os.system('ls')
#     empty.pyc       fibonacci.pyc  ifyouwantme~  monica     old        perl.pl
#     ruby.rb         stopiter.py    tests         works
#  
#  
# Here we import the os module and interact with the operating system.
#  
# Finally, we want to exit the interpreter. We can exit the interpreter in several ways:
#  
#     * Ctrl+D
#     * quit()
#  
# We can also exit the interpreter programatically.
#  
#  
#     >>> raise SystemExit
#     $ 
#  
#  
# or
#  
#  
#     >>> import sys
#     >>> sys.exit()
#     $
#  
#  
# The interpreter is exited.

'''The Zen of Python'''
#  
# The Zen of Python is a set of rules how to write good Python code. 
# It reflects somehow the philosophy of the language.
#  
#  
#     >>> import this
#     The Zen of Python, by Tim Peters
#      
#     Beautiful is better than ugly.
#     Explicit is better than implicit.
#     Simple is better than complex.
#     Complex is better than complicated.
#     Flat is better than nested.
#     Sparse is better than dense.
#     Readability counts.
#     Special cases aren't special enough to break the rules.
#     Although practicality beats purity.
#     Errors should never pass silently.
#     Unless explicitly silenced.
#     In the face of ambiguity, refuse the temptation to guess.
#     There should be one-- and preferably only one --obvious way to do it.
#     Although that way may not be obvious at first unless you're Dutch.
#     Now is better than never.
#     Although never is often better than *right* now.
#     If the implementation is hard to explain, it's a bad idea.
#     If the implementation is easy to explain, it may be a good idea.
#     Namespaces are one honking great idea -- let's do more of those!
#     The rules can be read by launching import this.
#  
#  
# In this chapter we have looked at Python interactive interpreter.

