#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
'''Iterators and Generators'''
# 
# According to Wikipedia, an iterator is an object which allows a programmer to traverse through all the elements of a collection, 
# regardless of its specific implementation.
# 
# In Python programming language, an iterator is an object which implements the iterator protocol. 
# The iterator protocol consists of two methods. 
# The __iter__() method, which must return the iterator object and the next() method, 
# which returns the next element from a sequence.
# 
# Python has several built-in objects, which implement the iterator protocol. 
# For example lists, tuples, strings, dictionaries or files.
# 
# 
#     #!/usr/bin/python
#     
#     # iter.py
#     
#     
#     str = "formidable"
#     
#     for i in str:
#        print i,
#     
#     print
#     
#     it = iter(str)
#     
#     print it.next()
#     print it.next()
#     print it.next()
#     
#     print list(it)
# 
# 
# In the code example, we show a built-in iterator on a string. 
# In Python a string is an immutable sequence of characters. 
# The iter() function returns an iterator on object. We can also use the list() or tuple() functions on iterators.
# 
#     $ ./iter.py 
#     f o r m i d a b l e
#     f
#     o
#     r
#     ['m', 'i', 'd', 'a', 'b', 'l', 'e']
# 
# Iterators have several advantages:
# 
#     Cleaner code
#     Iterators can work with infinite sequences
#     Iterators save resources
#     By saving system resources we mean that when working with iterators, we can get the next element in a sequence without keeping the entire dataset in memory.
# 
# 
#     #!/usr/bin/python
#     
#     # wantme1.py
#     
#     f = open('ifyouwantme', 'r')
#     
#     while True:
#        line = f.readline()
#        if not line: break
#        else: print line,
#     
#     f.close()
# 
# 
# This code prints the contents of the ifyouwantme file.
# 
# 
#     #!/usr/bin/python
#     
#     # wantme2.py
#     
#     f = open('ifyouwantme', 'r')
#     
#     for line in f:
#        print line,
#     
#     f.close()
# 
# 
# The wantme2.py script does the same. 
# In this case, we use iterators. 
# The code is cleaner.
# 
# In the following example, we create our own object that will implement the iterator protocol.
# 
# 
#     #!/usr/bin/python
#     
#     # iterator.py
#     
#     
#     class seq:
#        def __init__(self):
#           self.x = 0
#     
#        def next(self):
#           self.x += 1
#           return self.x**self.x
#     
#        def __iter__(self):
#           return self
#     
#     
#     s = seq()
#     n = 0
#     
#     for i in s:
#        print i
#        n += 1
#        if n > 10:
#           break
# 
# 
# In the code example, we create a sequence of numbers 1, 4, 27, 256, ... . 
# This demonstrates that with iterators, we can work with infinite sequences. 
# The for statement calls the iter() function on the container object. 
# The function returns an iterator object that defines the method next() which accesses elements in the container one at a time.
# 
#      def next(self):
#         self.x += 1
#         return self.x**self.x
# 
# The next() method returns the next element of a sequence.
# 
#      def __iter__(self):
#         return self
# 
# The __iter__ method returns the iterator object.
# 
#      if n > 10:
#           break
# 
# Because we are working with an infinite sequence, we must interrupt the for loop.
# 
#     $ ./iterator.py 
#     1
#     4
#     27
#     256
#     3125
#     46656
#     823543
#     16777216
#     387420489
#     10000000000
#     285311670611
# 
# The loop can be interrupted in another way. 
# In the class definition we must raise a StopIteration exception. 
# In the following example, we redo our previous example.
# 
# 
#     #!/usr/bin/python
#     
#     # stopiter.py
#     
#     
#     class seq14:
#        def __init__(self):
#           self.x = 0
#     
#        def next(self):
#           self.x += 1
#           if self.x > 14:
#              raise StopIteration
#           return self.x**self.x
#     
#        def __iter__(self):
#           return self
#     
#     
#     s = seq14()
#     
#     for i in s:
#        print i
# 
# 
# The code example will print first 14 numbers of a sequence.
# 
#     if self.x > 14:
#         raise StopIteration
# 
# The StopIteration exception will cease the for loop.
#  
'''Generators'''
# 
# In general, a generator is a special routine that can be used to control the iteration behaviour of a loop. 
# A generator is similar to a function returning an array. 
# A generator has parameters, it can be called and it generates a sequence of numbers. 
# But unlike functions, which return a whole array, a generator yields one value at a time. 
# This requires less memory. (Wikipedia)
# 
# Generators in Python:
# 
#     Are defined with the def keyword
#     Use the yield keyword
#     May use several yield keywords
#     Return an iterator
# 
# Let's look at an generator example.
# 
# 
#     #!/usr/bin/python
#     
#     # generator.py
#     
#     
#     def gen():
#        x, y = 1, 2
#        yield x, y
#        x += 1
#        yield x, y
#     
#     
#     it = gen()
#     
#     print it.next()
#     print it.next()
#     
#     try:
#        print it.next()
#     except StopIteration:
#        print "Iteration finished"
# 
# 
# As we can see, a generator is defined with a def keyword, just like normal functions. 
# We use two yield keywords inside the body of a generator. 
# Now it is important to understand, how actually the yield keyword works. 
# It exits the generator and returns a value. 
# Next time the next() function of an iterator is called, we continue on the line following the yield keyword. 
# Note that the local variables are preserved throughout the iterations. 
# When there is nothing left to yield, a StopIteration exception is raised.
# 
#     $ ./generator.py 
#     (1, 2)
#     (2, 2)
#     Iteration finished
# 
# The following example we will calculate Fibonacci numbers. 
# The first number of the sequence is 0, the second number is 1, and each subsequent number is equal to 
# the sum of the previous two numbers of the sequence itself.
# 
# 
#     #!/usr/bin/python
#     
#     # fibonacci.py
#     
#     import time
#     import sys
#     
#     def fib():
#        a, b = 0, 1
#        while True:
#           yield b
#           a, b = b, a + b
#     
#     
#     iter = fib()
#     
#     try:
#        for i in iter:
#           print i,
#           time.sleep(1)
#           sys.stdout.flush()
#     except KeyboardInterrupt:
#        print "Calculation stopped"
# 
# 
# The script will continuously print Fibonacci numbers to the console.
# 
# In this chapter, we have covered iterators and generators in Python.