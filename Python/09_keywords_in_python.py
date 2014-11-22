#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Keywords in Python'''
# 
# In this part of the Python programming tutorial, we will introduce all keywords in Python language.
# 
'''List of keywords'''
# 
# The following is a list of keywords for the Python programming language.
# 
#         and       del       from      not       while
#         as        elif      global    or        with
#         assert    else      if        pass      yield
#         break     except    import    print
#         class     exec      in        raise
#         continue  finally   is        return 
#         def       for       lambda    try
# 
# Python is a dynamic language. 
# It changes during time. 
# The list of keywords may change in the future.
# 
# 
#     #!/usr/bin/python
#     
#     # keywords.py
#     
#     import sys
#     import keyword
#     
#     
#     print "Python version: ", sys.version_info
#     print "Python keywords: ", keyword.kwlist
# 
# 
# This script prints the version of Python and its actual keyword list.
# 
'''print keyword'''
# 
# The print keyword is use to print numbers and characters to the console. 
# (In Python 3, print is not a keyword anymore, it becomes a function.)
# 
# 
#     #!/usr/bin/python
#     
#     # tutorial.py
#     
#     print "*" * 24
#     print "*" * 24
#     print "*" * 24
#     print 
#     print "\tZetCode"
#     print 
#     print "*" * 24 
#     print "*" * 24
#     print "*" * 24
# 
# 
# The print keyword without any text will line feed.
# 
#     $ ./tutorial.py 
#     ************************
#     ************************
#     ************************
#     
#             ZetCode
#     
#     ************************
#     ************************
#     ************************
# 
'''Control flow'''
# 
# The while keyword is a basic keyword for controlling the flow of the program. 
# The statements inside the while loop are executed, until the expression evaluates to False.
# 
# 
#     #!/usr/bin/python
#     
#     # sum.py
#     
#     numbers = [22, 34, 12, 32, 4]
#     sum = 0
#     
#     i = len(numbers)
#     
#     while (i != 0):
#        i -= 1
#        sum = sum + numbers[i]
#     
#     print "The sum is: ", sum
# 
# 
# In our script we want to calculate the sum of all values in the numbers list. 
# We utilize the while loop. 
# We determine the length of the list. 
# The while loop is executed over and over again, until the i is equal to zero. 
# In the body of the loop, we decrement the counter and calculate the sum of values.
# 
# The break keyword is used to interrupt the cycle if needed.
# 
# 
#     #!/usr/bin/python
#     
#     # testbreak.py
#     
#     import random
#     
#     while (True):
#        val = random.randint(1, 30)
#        print val,
#        if (val ==  22):
#           break
# 
# 
# In our example, we print random integer numbers. 
# If the number equals to 22, the cycle is interrupted with the break keyword.
# 
#     $ ./testbreak.py 
#     14 14 30 16 16 20 23 15 17 22
# 
# The next example shows the continue keyword. 
# It is used to interrupt the current cycle, without jumping out of the whole cycle. 
# New cycle will begin.
# 
# 
#     #!/usr/bin/python
#     
#     # testcontinue.py
#     
#     import random
#     
#     num = 0
#     
#     while (num < 1000):
#        num = num + 1
#        if (num % 2) == 0:
#           continue
#        print num,
# 
# 
# In the example we print all numbers smaller than 1000 that cannot be divided by number 2.
# 
# The if keyword is the commonest used control flow keyword. 
# The if keyword is used to determine, which statements are going to be executed.
# 
# 
#     #!/usr/bin/python
#     
#     # licence.py
#     
#     age = 17
#     
#     if age > 18:
#        print "Driving licence issued"
#     else:
#        print "Driving licence not permitted"
# 
# 
# The if keyword tests if the the person is older than 18. If the condition is met, the driving license is issued. 
# Otherwise, it is not. 
# The else keyword is optional. 
# The statement after the else keyword is executed, unless the condition is True.
# 
# Next we will see, how we can combine the statements using the elif keyword. Stands for else if.
# 
# 
#     #!/usr/bin/python
#     
#     # hello.py
#     
#     name = "Luke"
#     
#     if name == "Jack":
#        print "Hello Jack!"
#     elif name == "John":
#        print "Hello John!"
#     elif name == "Luke":
#        print "Hello Luke!"
#     else:
#        print "Hello there!"
# 
# 
# If the first test evaluates to False, we continue with the next one. 
# If none of the tests is True, the else statement is executed.
# 
#     $ ./hello.py 
#     Hello Luke!
# 
# Output.
# 
# The for keyword is used to iterate over items of a collection in order that they appear in the container.
# 
# 
#     #!/usr/bin/python
#     
#     # lyrics.py
#     
#     lyrics = """\
#     Are you really here or am I dreaming
#     I can't tell dreams from truth 
#     for it's been so long since I have seen you
#     I can hardly remember your face anymore 
#     """
#     
#     
#     for i in lyrics:
#        print i,
# 
# 
# In the example, we have a lyrics variable having a strophe of a song. 
# We iterate over the text and print the text character by character. 
# The comma in the print statement prevents from printing each character on a new line.
# 
#     $ ./lyrics.py 
#     A r e   y o u   r e a l l y   h e r e   o r   a m   I   d r e a m i n g 
#     I   c a n ' t   t e l l   d r e a m s   f r o m   t r u t h   
#     f o r   i t ' s   b e e n   s o   l o n g   s i n c e   I   h a v e   s e e n   y o u 
#     I   c a n   h a r d l y   r e m e m b e r   y o u r   f a c e   a n y m o r e   
# 
# This is the output of the script.
# 
'''Boolean expressions'''
# 
# First we will introduce keywords that work with boolean values and expressions: is, or, and, and not.
# 
# 
#     #!/usr/bin/python
#     
#     # objects.py
#     
#     print None == None
#     print None is None
#     
#     print True is True
#     
#     print [] == []
#     print [] is []
#     
#     print "Python" is "Python"
# 
# 
# The == operator tests for equality 
# The is keyword tests for object identity. 
# Whether we are talking about the same object. 
# Note that multiple variables may refer to the same object.
# 
#     $ ./objects.py 
#     True
#     True
#     True
#     True
#     False
#     True
# 
# The output might be surprising for you. 
# In Python language, there is only one None and one True object. 
# That's why True is equal and also identical to True. 
# There is only one truth out there, anyway. 
# The empty list []is equal to another empty list []. 
# But they are not identical. 
# Python has put them into two different memory locations. 
# They are two distinct objects. 
# Hence the is keyword returns False. 
# On the other hand, "Python" is "Python" returns True. 
# This is because of optimization. 
# If two string literals are equal, they have been put to same memory location. 
# A string is an immutable entity. 
# No harm can be done.
# 
# The not keyword negates a boolean value.
# 
# 
#     #!/usr/bin/python
#     
#     # grades.py
#     
#     grades = ["A", "B", "C", "D", "E", "F"]
#     
#     grade = "L"
#     
#     if grade not in grades:
#        print "unknown grade"
#     In our example we test, whether the grade value is from the list of possible grades.
#     
#     $ ./grades.py 
#     unknown grade
# 
# The keyword and is used if all conditions in a boolean expression must be met.
# 
# 
#     #!/usr/bin/python
#     
#     # youngmale.py
#     
#     sex = "M"
#     age = 26
#     
#     if age < 55 and sex == "M":
#        print "a young male"
# 
# 
# In our example, we test if two conditions are met. 
# The "young male" is printed to the console if variable age is less than 55 and variable sex is equal to M.
# 
#      $ ./youngmale.py 
#     a young male
# 
# The keyword or is used if at least one condition must be met.
# 
# 
#     #!/usr/bin/python
#     
#     # name.py
#     
#     name = "Jack"
#     
#     if ( name == "Robert" or name == "Frank" or name == "Jack" 
#           or name == "George" or name == "Luke"):
#        print "This is a male"
# 
# 
# If at least one of the expressions is true, the print statement is executed.
# 
# When we work with and/or keywords in Python programming language, short circuit evaluation takes place. 
# Short circuit evaluation means that the second argument is only evaluated if the first argument does not 
# suffice to determine the value of the expression: 
#         when the first argument of and evaluates to false, the overall value must be false; 
#         and when the first argument of or evaluates to true, the overall value must be true. (wikipedia)
# 
# A typical example follows.
# 
# 
#     #!/usr/bin/python
#     
#     x = 10
#     y = 0
#     
#     if (y != 0 and x/y < 100):
#        print "a small value"
# 
# 
# The first part of the expression evaluates to False. 
# The second part of the expression is not evaluated. 
# Otherwise, we would get a ZeroDivisionError.

'''Modules'''
# 
# The following keywords are used with modules. 
# Modules are files, in which we organize our Python code.
# 
# The import keyword is used to import other modules into a Python script.
# 
# 
#     #!/usr/bin/python
#     
#     # pi.py
#     
#     import math
#     
#     print math.pi
# 
# 
# We use the import keyword to import the math module into the namespace of our script. 
# We print the PI value.
# 
# We use the as keyword if we want to give a module a different alias.
# 
# 
#     #!/usr/bin/python
#     
#     # rand.py
#     
#     import random as rnd
#     
#     for i in range(10):
#        print rnd.randint(1, 10), 
# 
# 
# In this case, we import the random module. 
# We will print ten random integer numbers. 
# We give the random module a different alias, namely rnd. 
# In the script we reference the module with the new alias. 
# Notice that we cannot name the script random.py or rnd.py. 
# We would get errors.
# 
#     $ ./rand.py 
#     1 2 5 10 10 8 2 9 7 2
# 
# The from keyword is used for importing a specific variable, class or a function from a module.
# 
# 
#     #!/usr/bin/python
#     
#     # testfrom.py
#     
#     from sys import version
#     
#     print version
# 
# 
# From the sys module, we import the version variable. 
# If we want to print it, we do not need to use the module name. 
# The version variable was imported directly to our namespace and we can reference it directly.
# 
#     $ ./testfrom.py 
#     2.5.1 (r251:54863, Mar  7 2008, 03:41:45) 
#     [GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)]

'''Functions'''
# 
# Here we will describe keywords associated with functions. 
# The def keyword is used to create a new user defined function. 
# Functions are objects in which we organize our code.
# 
# 
#     #!/usr/bin/python
#     
#     # function.py
#     
#     
#     def root(x):
#        return x * x
#     
#     a = root(2)
#     b = root(15)
#     
#     print a, b
# 
# 
# The example demonstrates a simple new function. 
# The function will calculate the square of a number. 
# The return key is closely connected with a function definition. 
# The keyword exits the function and returns a value. 
# The value is than assigned to the a and b variables.
# 
# The lambda keyword creates a new anonymous function. 
# An anonymous function is a function, which is not bound to a specific name. 
# It is also called an inline function.
# 
# 
#     !/usr/bin/python
#     
#     # lambda.py
#     
#     for i in (1, 2, 3, 4, 5):
#        a =  lambda x: x * x
#        print a(i),
# 
# 
# As you can see in the previous example, we do not create a new function with a def keyword. 
# Instead of that we use an inline function on the fly.
# 
#     $ ./lambda.py 
#     1 4 9 16 25
# 
# If we want to access variables defined outside functions, we use the global keyword.
# 
#     #!/usr/bin/python
#     
#     # testglobal.py
#     
#     x = 15
#     
#     def function():
#        global x
#        x = 45
#     
#     function()
#     print x
# 
# 
# Normally, assigning to x variable inside a function, we create a new local variable, which is valid only in that function. 
# But if we use the global keyword, we change a variable ouside the function definition.
# 
#     $ ./testglobal.py 
#     45

'''Exceptions'''
# 
# Next we will work with keywords that are used with exception handling.
# 
#     $ cat films
#     Fargo
#     Aguirre, der Zorn Gottes
#     Capote
#     Grizzly man
#     Notes on a scandal
# 
# This is a file, containing some film titles. 
# In the code example, we are going to read it.
# 
# 
#     #!/usr/bin/python
#     
#     # files.py
#     
#     f = None
#     
#     try:
#        f = open('films', 'r')
#        for i in f:
#           print i,
#     except IOError:
#        print "Error reading file"
#     
#     finally:
#        if f:
#            f.close()
# 
# 
# We try to read a films file. 
# If no exception occurs, we print the contents of the file to the console. 
# There might be an exception. 
# For example, if we provided an incorrect file name. 
# In such a case a IOError exception is raised. 
# The except keyword catches the exception and executes its code. 
# The finally keyword is always executed in the end. 
# We use it to clean up our resources.
# 
# In the next example, we show how to create a user defined exception using the raise keyword.
# 
# 
#     #!/usr/bin/python
#     
#     # userexception.py
#     
#     class YesNoException(Exception):
#        def __init__(self):
#           print 'Invalid value'
#     
#     
#     answer = 'y'
#     
#     if (answer != 'yes' and answer != 'no'):
#        raise YesNoException
#     else:
#        print 'Correct value'
# 
# 
# In the example, we expect only yes/no values. 
# For other possibilities, we raise an exception.
# 
#     $ ./userexception.py 
#     Invalid value
#     Traceback (most recent call last):
#       File "./userexception.py", line 13, in <module>
#         raise YesNoException
#     __main__.YesNoException

'''Other keywords'''
# 
# The del keyword deletes objects.
# 
# 
#     #!/usr/bin/python
#     
#     # delete.py
#     
#     a = [1, 2, 3, 4]
#     
#     print a
#     del a[:2]
#     print a
# 
# 
# In our example, we have a list of four integer numbers. 
# We delete the first numbers from the list. 
# The outcome is printed to the console.
# 
#     $ ./delete.py 
#     [1, 2, 3, 4]
#     [3, 4]
# 
# Output.
# 
# The pass keyword does nothing. 
# It is a very handy keyword in some situations.
# 
#      def function():
#          pass
# 
# We have a function. 
# This function is not implemented yet. 
# It will be later. 
# The body of the function must not be empty. 
# So we can use a pass keyword here, instead of printing something like "function not implemented yet" or similar.
# 
# The assert keyword is used for debugging purposes. 
# We can use it for testing conditions that are obvious to us. 
# For example, we have a program that calculates salaries. 
# We know that the salary cannot be less than zero. 
# So we might put such an assertion to the code. 
# If the assertion fails, the interpreter will complain.
# 
# 
#     #!/usr/bin/python
#     
#     # salary.py
#     
#     salary = 3500
#     salary -= 3560 # a mistake was done
#     
#     assert salary > 0
# 
# 
# During the execution of the program a mistake was done. 
# The salary becomes a negative number.
# 
#     $ ./salary.py 
#     Traceback (most recent call last):
#       File "./salary.py", line 9, in <module>
#         assert salary > 0
#     AssertionError
# 
# The execution of the script will fail with an AssertionError.
# 
# The class keyword is the most important keyword in object oriented programming. 
# It is used to create new user defined objects.
# 
# 
# #!/usr/bin/python
# 
# # square.py
# 
#     class Square:
#        def __init__(self, x):
#           self.a = x
#     
#        def area(self):
#           print self.a * self.a
#     
#     
#     sq = Square(12)
#     sq.area()
# 
# 
# In the code example, we create a new Square class. 
# Then we instantiate the class and create an object. 
# We compute the area of the square object.
# 
# The exec keyword executes Python code dynamically.
# 
# 
#     #!/usr/bin/python
#     
#     # execution.py
#     
#     exec("for i in [1, 2, 3, 4, 5]: print i,")
# 
# 
# We print five numbers from a list using a for loop. 
# All within the exec keyword.
# 
#     $ ./execution.py 
#     1 2 3 4 5
# 
# Finally, we mention the in keyword.
# 
# 
#     #!/usr/bin/python
#     
#     # inkeyword.py
#     
#     print 4 in (2, 3, 5, 6)
#     
#     for i in range(25):
#        print i,
# 
# 
# In this example, the in keyword tests if the number four is in the tuple. 
# The second usage is traversing a tuple in a for loop. 
# The built-in function range() returns integers 0 .. 24.
# 
#     $ ./inkeyword.py 
#     False
#     0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
# 
# The yield keyword is used with generators.
# 
# 
#     #!/usr/bin/python
#     
#     # yieldkeyword.py
#     
#     
#     def gen():
#        x = 11
#        yield x
#     
#     it = gen()
#     
#     print it.next()
# 
# 
# The yield keyword exits the generator and returns a value.
# 
#     $ ./yieldkeyword.py 
#     11
# 
# In this part of the Python tutorial, we have covered Python keywords.
