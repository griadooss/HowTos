#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''Python language'''
#
# In this part of the Python programming tutorial, we will talk about the Python programming language in general.
#
'''Goal'''
#
# The goal of this tutorial is to get you started with the Python programming language. 
# Python is a great language to learn. 
# It is an ideal language for those, who are new to programming. 
# After reading this tutorial, you will be confident to continue your own studies. 
# You can create scripts, web sites, games or desktop applications in Python. 
# Even if you do not want to become a programmer, Python may be a great tool for occasional programmers or hobbyists.
#
'''Python'''
#
# Python is a general-purpose, dynamic, object-oriented programming language. 
# The design purpose of the Python language emphasizes programmer productivity and code readability. 
# Python was initially developed by Guido van Rossum. It was first released in 1991. 
# Python was inspired by ABC, Haskell, Java, Lisp, Icon and Perl programming languages. 
# Python is a high level, general purpose, multiplatform, interpreted language. 
# It is a minimalistic language. 
# One of its most visible features is that it does not use semicolons nor brackets. 
# Python uses indentation instead.
# 
# There are two main branches of Python currently. 
# Python 2.x and Python 3.x. 
# Python 3.x breaks backward compatibility with previous releases of Python. 
# It was created to correct some design flaws of the language and make the language more clean. 
# The most recent version of Python 2.x is 2.7.3, and of Python 3.x 3.3.0. 
# This tutorial covers Python 2.x versions. Most of the code is written in Python 2.x versions. 
# It will take some time till the software base and programmers will migrate to Python 3.x. 
# Today, Python is maintained by a large group of volunteers worldwide. 
# Python is open source software.
# 
# Python supports several programming styles. 
# It does not force a programmer to a specific paradigm. 
# It supports object oriented and procedural programming. 
# There is also a limited support for functional programming.
# 
# The official web site for the Python programming language is python.org
#
'''Implementations'''
#
# Formally, Python programming language is a specification. 
# There are three main implementations of Python. 
# CPython, IronPython and Jython. CPython is implemented in C language. 
# It is the most widely used implementation of Python. 
# When people talk about Python language, they mostly mean CPython. 
# IronPython is implemented in C. 
# It is part of the .NET framework. 
# Similarly, Jython is an implementation of the Python language in Java. 
# Jython program is translated into the Java bytecode and executed by the JVM (Java Virtual Machine). 
# In this tutorial, we will work with CPython.
#
'''Popularity'''
#
# Python belongs to the most popular programming languages. 
# Both langpop.com and tiobe sites place Python to top ten languages. 
# Some very popular Python projects include a distributed source management tool Mercurial, 
# a Django web framework, a PyQt GUI library or a package management utility called Yum.
#
'''Python scripts'''
#
# Every script in the UNIX starts with a shebang. 
# The shebang is the first two characters in the script: "#!". 
# The shebang is followed by the path to the interpreter, which will execute our script.
# 
#     !/usr/bin/python
#      print "The Python tutorial"
#
# This is our first Python script. 
# The script will print "The Python tutorial" string to the console. 
# Python scripts have py extension.
#
#     $ which python
#     /usr/bin/python
# 
# We can find out the path to the Python interpreter using the which command.
# 
# Python scripts can be run in two ways.
# 
#     $ python first.py
#     The Python tutorial
# 
# Python script is given as an argument to the interpreter.
# 
#     $ chmod +x first.py 
#     $ ./first.py 
#     The Python tutorial
# 
# Or the common way. 
# Use the chmod command to make the file executable. 
# And launch it.
# 
# The next example shows a simple Ruby script.
# 
#     #!/usr/bin/ruby
#      
#     fruits = ["orange", "apple", "pear", "kiwi"]
#     fruits.each {|fruits| puts fruits}
# 
# Note the shebang and the path to the Ruby interpreter.
# 
#     $ ./ruby.rb 
#     orange
#     apple
#     pear
#     kiwi
#       
# This is the output of the Ruby script.
# 
# Finally, we show a small Perl script.
# 
#     #!/usr/bin/perl
#      
#     $perl = "Practical Extraction and Report Language\n";
#      
#     print $perl;
#  
# Now the concept should be clear.
# 
# In this chapter, we have introduced Python language.

