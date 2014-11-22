#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''Exceptions in Python'''
# 
# In this part of the Python programming tutorial, we will talk about exceptions in Python.
# 
# Errors detected during execution are called exceptions. 
# During the execution of our application, many things might go wrong. 
# A disk might get full and we cannot save our file. 
# An Internet connection might go down and our application tries to connect to a site. 
# All these might result in a crash of our application. 
# To prevent this, we must cope with all possible errors that might occur. 
# For this, we can use the exception handling.
# 
#     >>> 3 / 0
#     Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#     ZeroDivisionError: integer division or modulo by zero
# 
# It is not possible to divide by zero. 
# If we try to do this, a ZeroDivisionError is raised and the script is interrupted.
# 
#     $ cat zerodivision.py 
#     #!/usr/bin/python
#     
#     # zerodivision.py
#     
#     
#     def input_numbers():
#         a = float(raw_input("Enter first number:"))
#         b = float(raw_input("Enter second number:"))
#         return a, b
#     
#     x, y = input_numbers()
#     print "%d / %d is %f" % (x, y, x/y)
# 
# 
# In this script, we get two numbers from the console. 
# We divide these two numbers. 
# If the second number is zero, we get an exception.
# 
#     $ ./zerodivision.py 
#     Enter first number:2
#     Enter second number:0
#     Traceback (most recent call last):
#       File "./zerodivision.py", line 12, in <module>
#         print "%d / %d is %f" % (x, y, x/y)
#     ZeroDivisionError: float division
# 
# We could handle this in two ways.
# 
# 
#     #!/usr/bin/python
#     
#     # zerodivision2.py
#     
#     
#     def input_numbers():
#         a = float(raw_input("Enter first number:"))
#         b = float(raw_input("Enter second number:"))
#         return a, b
#     
#     
#     x, y = input_numbers()
#     
#     while True:
#         if y != 0:
#             print "%d / %d is %f" % (x, y, x/y)
#             break
#         else:
#            print "Cannot divide by zero"
#            x, y = input_numbers() 
# 
# 
# First, we simply check that y value is not zero. 
# If the y value is zero, we print a warning message and repeat the input cycle again. 
# This way, we handled the error and the script is not interrupted.
# 
#     $ ./zerodivision2.py 
#     Enter first number:4
#     Enter second number:0
#     Cannot divide by zero
#     Enter first number:5
#     Enter second number:0
#     Cannot divide by zero
#     Enter first number:5
#     Enter second number:6
#     5 / 6 is 0.833333
# 
# The other way is to use exceptions.
# 
# 
#     #!/usr/bin/python
#     
#     # zerodivision3.py
#     
#     
#     def input_numbers():
#         a = float(raw_input("Enter first number:"))
#         b = float(raw_input("Enter second number:"))
#         return a, b
#     
#     
#     x, y = input_numbers()
#     
#     while True:
#         try:
#             print "%d / %d is %f" % (x, y, x/y)
#             break
#         except ZeroDivisionError:
#            print "Cannot divide by zero"
#            x, y = input_numbers() 
# 
# 
# After try keyword, we put the code, where we expect an exception. 
# The except keyword catches the exception, if it is raised. We specify, what kind of exception we are looking for.
# 
#     except ValueError:
#        pass
#     except (IOError, OSError):
#        pass
# 
# To handle more exceptions, we can either use more except keywords or place the exception names inside a tuple.
#  
'''Second argument of the except keyword'''
# 
# If we provide a second argument for the except keyword, we get a reference to the exception object.
# 
# 
#     #!/usr/bin/python
#     
#     # zero.py
#     
#     try:
#         3/0
#     except ZeroDivisionError, e:
#         print "Cannot divide by zero"
#         print "Message:", e.message
#         print "Class:", e.__class__
# 
# 
# From the exception object, we can get the error message or the class name.
# 
#     $ ./zero.py 
#     Cannot divide by zero
#     Message: integer division or modulo by zero
#     Class: <type 'exceptions.ZeroDivisionError'>
#  
'''The hierarchy of exceptions'''
# 
# The exceptions are organized in a hierarchy, being Exception the parent of all exceptions.
# 
# 
#     #!/usr/bin/python
#     
#     # interrupt.py
#     
#     try:
#         while True:
#            pass
#     except KeyboardInterrupt:
#        print "Program interrupted"
# 
# 
# The script starts and endless cycle. 
# If we press Ctrl+C, we interrupt the cycle. Here, we caught the KeyboardInterrupt exception.
# 
#     Exception
#       BaseException
#         KeyboardInterrupt
# 
# This is the hierarchy of the KeyboardInterrupt exception.
# 
# 
#     #!/usr/bin/python
#     
#     # interrupt.py
#     
#     try:
#         while True:
#            pass
#     except BaseException:
#        print "Program interrupted"
# 
# 
# This example works too. 
# The BaseException also catches the keyboard interruption. 
# Among other exceptions.
#  
'''User defined exceptions'''
# 
# We can create our own exceptions if we want. 
# We do it by defining a new exception class.
# 
# 
#     #!/usr/bin/python
#     
#     # b.py
#     
#     
#     class BFoundError(Exception):
#        def __init__(self, value):
#           print "BFoundError: b character found at position %d" % value
#     
#     string = "You make me want to be a better man."
#     
#     
#     pos = 0
#     for i in string:
#        if i == 'b':
#           raise BFoundError, pos
#        pos = pos + 1
# 
# 
# In our code example, we have created a new exception. 
# The exception is derived from the base Exception class. 
# If we find any occurrence of letter b in a string, we raise our exception.
# 
#     $ ./b.py 
#     BFoundError: b character found at position 20
#     Traceback (most recent call last):
#       File "./b.py", line 16, in <module>
#         raise BFoundError, pos 
#     __main__.BFoundError
#  
'''The cleanup'''
# 
# There is a finally keyword, which is always executed. 
# No matter if the exception is raised or not. 
# It is often used to do some cleanup of resources in a program.
# 
# 
#     #!/usr/bin/python
#     
#     # cleanup.py
#     
#     f = None
#     
#     try:
#        f = file('indaclub', 'r')
#        contents = f.readlines()
#        for i in contents:
#           print i,
#     except IOError:
#        print 'Error opening file'
#     finally:
#        if f:
#           f.close()
# 
# 
# In our example, we try to open a file. 
# If we cannot open the file, an IOError is raised. 
# In case we opened the file, we want to close the file handler. 
# For this, we use the finally keyword. In the finally block we check if the file is opened or not. 
# If it is opened, we close it. 
# This is a common programming construct when we work with databases. 
# There we similarly cleanup the opened database connections.
# 
# In this chapter, we have covered exceptions in Python.