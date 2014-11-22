#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Files in Python'''
# 
# In this part of the Python programming tutorial, we will talk about files.
# 
# Everything in Python is an object. 
# Everything in UNIX is a file.
# 
''Standard I/O''
# 
# There are three basic I/O connections. 
# Standard input, standard output and standard error. 
# Standard input is the data that goes to the program. 
# The standard input comes from a keyboard. 
# Standard output is where we print our data with the print keyword. 
# Unless redirected, it is the terminal console. 
# The standard error is a stream where programs write their error messages. 
# It is usually the text terminal.
# 
# Conforming to the UNIX philosophy, the standard I/O streams are file objects.
#  
''Standard input''
# 
# Standard input is the data that goes to the program.
# 
# 
#     #!/usr/bin/python
#     
#     # name.py
#     
#     import sys
#     
#     
#     print 'Enter your name: ',
#     
#     name = ''
#     
#     while True:
#        c = sys.stdin.read(1)
#        if c == '\n':
#           break
#        name = name + c
#     
#     print 'Your name is:', name
# 
# 
# In order to work with standard I/O streams, we must import the sys module. 
# The read() method reads one character from the standard input. 
# In our example we get a prompt saying "Enter your name". 
# We enter our name and press enter. 
# The enter key generates the new line character: \n.
# 
#     $ ./name.py 
#     Enter your name: Jan
#      Your name is: Jan
# 
# For getting input we can use higher level functions: input() and raw_input() .
# 
# The input() function prints a prompt if it is given, reads input and evaluates it.
# 
# 
#     #!/usr/bin/python
#      
#     # input.py
#      
#      
#     data = input('Enter expression: ')
#      
#     print 'You have entered:', data
# 
# 
#     $ ./input.py 
#     Enter expression: 3*3
#     You have entered: 9
# 
# 
# The raw_input() prints a prompt if it is present. 
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
# 
# 
# #!/usr/bin/python
# 
# # rawinput.py
# 
# 
# name = raw_input('Enter your name: ')
# 
# print 'You have entered:', name
# 
#  
'''Standard output'''
# 
# The standard output is where we print our data.
# 
# 
#     #!/usr/bin/python
#     
#     # stdout.py
#     
#     import sys
#     
#     sys.stdout.write('Honore de Balzac, Father Goriot\n')
#     sys.stdout.write('Honore de Balzac, Lost Illusions\n')
# 
# 
# In the example, we write some text to the standard output. 
# This is in our case the terminal console. 
# We use the write() method.
# 
#     $ ./stdout.py 
#     Honore de Balzac, Father Goriot
#     Honore de Balzac, Lost Illusions
# 
# The print keyword puts some text into the sys.stdout by default.
# 
# 
#     #!/usr/bin/python
#     
#     # printkeyw.py
#     
#     print 'Honore de Balzac, The Splendors and Miseries of Courtesans'
#     print 'Honore de Balzac, Gobseck'
# 
# 
# We do not provide the sys.stdout explicitly. 
# It is done behind the scenes. 
# There is another form of the print keyword. 
# If we want, we can use it to write some data into a regular file.
# 
# 
#     #!/usr/bin/python
#     
#     # works.py
#     
#     f = open('works', 'w')
#     
#     print >> f, 'Beatrix'
#     print >> f, 'Honorine'
#     print >> f, 'The firm of Nucingen'
#     
#     f.close()
# 
# 
# We open a file and write three titles of Balzac books into it. 
# This form is also called print chevron.
# 
#     $ cat works
#     Beatrix
#     Honorine
#     The firm of Nucingen
#  
'''Redirection'''
# 
# File objects can be redirected. 
# In the following example, we redirect the standard output to a regular file.
# 
# 
#     #!/usr/bin/python
#     
#     # redirect.py
#     
#     import sys
#     
#     
#     f = open('output', 'w')
#     sys.stdout = f
#     
#     print 'Lucien'
#     sys.stdout.write('Rastignac\n')
#     sys.stdout.writelines(['Camusot\n', 'Collin\n'])
#     
#     sys.stdout = sys.__stdout__
#     
#     print 'Bianchon'
#     sys.stdout.write('Lambert\n')
# 
# 
# In the redirect.py script, we redirect a standard output to a regular file called output. 
# Then we restore the original standard output back. 
# The original value of the std.output is kept in a special sys.__stdout__ variable.
# 
#     $ ./redirect.py 
#     Bianchon
#     Lambert
#     $ cat output 
#     Lucien
#     Rastignac
#     Camusot
#     Collin
#  
'''The open function'''
# 
# The open() function is used to open files in our system.
# 
#     open(filename, [mode='r'], [bufsize])
# 
# The filename is the name of the file to be opened. 
# The mode indicates, how the file is going to be opened. 
# For reading, writing, appending etc. 
# The bufsize is an optional buffer. 
# It specifies the file's desired buffer size: 
#     0 means unbuffered, 
#     1 means line buffered, any other positive value means use a buffer of that size. 
#     A negative bufsize means to use the system default. 
# If omitted, the system default is used.
# 
#     The file modes:
#     
#     Mode    Meaning
#     r    Reading
#     w    Writing
#     a    Appending
#     b    Binary data
#     +    Updating
# 
# The following little script prints the contents of a file.
# 
# 
#     #!/usr/bin/python
#     
#     # wantme.py
#     
#     f = open('ifyouwantme', 'r')
#     
#     for line in f:
#        print line,
#     
#     f.close()
# 
# 
# We open a file in read mode. 
# We traverse the contents of the file with the for loop. 
# In the end, we close the file object.
# 
#     $ ./wantme.py 
#     Are you really here or am I dreaming
#     I can't tell dreams from truth 
#     for it's been so long since I have seen you
#     I can hardly remember your face anymore 
#     
#     When I get really lonely
#     and the distance causes our silence
#     I think of you smiling 
#     with pride in your eyes a lover that sighs 
#     
#     ...
# 
# In the next example, we do the same. 
# Now we use the readline() method.
# 
# 
#     #!/usr/bin/python
#     
#     # wantme2.py
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
# There is yet another simple way, how we can print the contents of a file. 
# Using the readlines() method. 
# The readlines() method reads all the contents of a file into the memory. 
# This is not applicable for very large files, though.
# 
# 
#     #!/usr/bin/python
#     
#     # wantme3.py
#     
#     f = open('ifyouwantme', 'r')
#     
#     contents = f.readlines()
#     
#     for i in contents:
#        print i,
#     
#     f.close()
# 
# 
# In the next example, we will demonstrate writing to a file. 
# We will write a simple strophe into a regular file.
# 
# 
#     #!/usr/bin/python
#     
#     # strophe.py
#     
#     text = """Incompatible, it don't matter though
#     'cos someone's bound to hear my cry
#     Speak out if you do
#     You're not easy to find\n"""
#     
#     
#     f = open('strophe', 'w')
#     f.write(text)
#     
#     f.close()
# 
# 
# This time we open the file in a w mode, so that we can write into it. 
# If the file does not exist, it is created. 
# If it exists, it is overwritten.
# 
#     $ cat strophe
#     Incompatible, it don't matter though
#     'cos someone's bound to hear my cry
#     Speak out if you do
#     You're not easy to find
#     
'''The pickle module'''
# 
# So far, we have been working with simple textual data. 
# What if we are working with objects rather than simple text? 
# For such situations, we can use the pickle module. 
# This module serializes Python objects. 
# The Python objects are converted into byte streams and written to text files. 
# This process is called pickling. 
# The inverse operation, reading from a file and reconstructing objects is called deserializing or unpickling.
# 
# 
#     #!/usr/bin/python
#     
#     # pickle.py
#     
#     import pickle
#     
#     class Person:
#        def __init__(self, name, age):
#           self.name = name
#           self.age = age
#     
#        def getName(self):
#           return self.name
#     
#        def getAge(self):
#           return self.age
#     
#     
#     person = Person('Monica', 15)
#     print person.getName()
#     print person.getAge()
#     
#     f = open('monica', 'w')
#     pickle.dump(person, f)
#     f.close()
#     
#     f = open('monica', 'r')
#     monica = pickle.load(f)
#     f.close()
#     
#     print monica.getName()
#     print monica.getAge()
# 
# 
# In our script, we define a Person class. 
# We create one person. 
# We pickle the object using the dump() method. 
# We close the file, open it again for reading. 
# Unpickle the object using the load() method.
# 
#     $ ./monica.py 
#     Monica
#     15
#     Monica
#     15
# 
#     $ file monica
#     monica: ASCII text
# 
# The file to which we write is a simple text file.
# 
# In this part of the Python tutorial, we covered files.