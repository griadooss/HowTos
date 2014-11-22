#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Python lexical structure'''
# 
# Computer languages, like human languages, have a lexical structure. 
# A source code of a Python program consists of tokens. 
# Tokens are atomic code elements. 
# In Python language, we have comments, variables, literals, operators, delimiters, and keywords.
#
'''Comments'''
#  
# Comments are used by humans to clarify the source code. 
# All comments in Python language follow the '# character'.
#  
#  
#     #!/usr/bin/python
#      
#     # commemts.py
#     # author jan bodnar
#     # ZetCode 2008
#      
#     def main():
#         print "Comments example"
#      
#     main()
#  
# Everything that follows the '# character' is ignored by the Python interpreter.

'''Variables'''
#  
# A variable is an identifier, which holds a value. 
# In programming we say that we assign a value to a variable. 
# Technically speaking, a variable is a reference to a computer memory, where the value is stored. 
# In Python language, a variable can hold a string, a number or various objects like a function or a class. 
# Variables can be assigned different values over time.
#  
# Variables in Python can be created from alphanumeric characters and underscore _ character. 
# A variable cannot begin with a number. 
# The Python interpreter can easier distinguish between a number and a variable.
#  
#  
#     Value
#     value2
#     company_name
#  
#  
# These were valid identifiers.
#  
#  
#     12Val
#     exx$
#     first-name
#  
#  
# These were examples of invalid identifiers.
#  
# The variables are case sensitive. 
# This mean that Price, price, and PRICE are three different identifiers.
#  
#  
#     #!/usr/bin/python
#      
#     number = 10
#     Number = 11
#     NUMBER = 12
#      
#     print number, Number, NUMBER
#  
#  
# In our script, we assign three numeric values to three identifiers.
#  
#     10 11 12
#  
# This is the output of the script.

'''A literal'''
#  
# A literal is any notation for representing a value within the Python source code. 
# Technically, a literal will be assigned a value at compile time, while a variable will be assigned at runtime.
#  
#  
#     age = 29
#     nationality = "Hungarian"
#  
#  
# Here we assign two literals to variables. Number 29 and string Hungarian are literals.
#  
#  
#     #!/usr/bin/python
#      
#     # literals.py
#      
#     name1 = "Jane"
#     age1 = 12
#      
#     name2 = "Rose"
#     age2 = 16
#      
#     "Patrick"
#     34
#      
#     "Luke"
#     23
#      
#     print name1, age1
#     print name2, age2
#  
#  
# If we do not assign a literal to a variable, there is no way, how we can work with it. 
# It is dropped.
#  
#  
#     $ ./literals.py 
#     Jane 12
#     Rose 16
#  
#  
# This is the output of the literals.py script.

'''Operators'''
#
# An operator is a symbol used to perform an action on some value.
# 
# 
    # +    -    ~    *    **    /    %
    # <<    >>    &    |    ^
    # and    or    not    in    not in 
    # is    is not    <    >    !=    <>
    # ==    <=    >=
    # 
# 
# This is a list of operators available in Python language. 
# We will talk about operators later in the tutorial.
# 
'''Indentation'''
# 
# Indentation is used to delimit blocks in Python. 
# Where other programming languages use curly brackets or keywords such as begin, end, Python uses white space. 
# An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block. 
# The Python style guide recommends using 4 spaces per indentation level.
# 
# 
    # if age > 18:
    #     print "adult person"
    # 
    # for i in range(5):
    #     print i
#     
#     
# After the if keyword a code block is expected. 
# A new statement is started on a new line, indented with 4 space characters. 
# The indentation for the following for keyword is decreased back to the initial one. 
# The for keyword starts a new code block, where its statement(s) are indented.
# 
'''Delimiters'''
# 
# A delimiter is a sequence of one or more characters used to specify the boundary between separate, 
# independent regions in plain text or other data stream.
# 
# 
    # (       )       [       ]       {       }      
    # ,       :       .       `       =       ;
    # +=      -=      *=      /=      //=     %=
    # <=      |=      ^=      >>=     <<=     **=
    # '       "       \       @
# 
# 
# Delimiters are used in various area of the Python language. 
# They are used to build expressions, string literals, tuples, dictionaries, or lists.
# 
'''Keywords'''
#  
# A keyword is a reserved word in the Python programming language. 
# Keywords are used to perform a specific task in a computer program. 
# For example, print a value to the console, do repetitive tasks or perform logical operations. 
# A programmer cannot use a keyword as an ordinary variable.
#  
#  
#     and       del       from      not       while
#     as        elif      global    or        with
#     assert    else      if        pass      yield
#     break     except    import    print
#     class     exec      in        raise
#     continue  finally   is        return 
#     def       for       lambda    try
#  
#  
# This is a list of Python keywords. 
# We have dedicated a special chapter to keywords in this tutorial.
#  
# This was the Python lexical structure.

