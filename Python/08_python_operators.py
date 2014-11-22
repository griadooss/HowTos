#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''Python operators'''
# 
# In this part of the Python programming tutorial, we will talk about operators.
# 
# An operator is a special symbol which indicates a certain process is carried out. 
# Operators in programming languages are taken from mathematics. 
# Programmers work with data. 
# The operators are used to process data.
# 
# In Python programming language, we have several types of operators:
# 
#     Arithmetic operators
#     Boolean operators
#     Relational operators
#     Bitwise operators
# 
# An operator may have one or two operands. 
# An operand is one of the inputs (arguments) of an operator. 
# Those operators that work with only one operand are called unary operators. 
# Those who work with two operands are called binary operators.
# 
# The + and - signs can be addition and subtraction operators as well as unary sign operators. It depends on the situation.
# 
#     >>> 2
#     2
#     >>> +2
#     2
#     >>> 
# 
# The plus sign can be used to indicate that we have a positive number. But it is mostly not used. The minus sign changes the sign of a value.
# 
#     >>> a = 1
#     >>> -a
#     -1
#     >>> -(-a)
#     1
# 
# Multiplication and addition operators are examples of binary operators. They are used with two operands.
# 
#     >>> 3 * 3
#     9
#     >>> 3 + 3
#     6
# 
# '''The assignment operator'''
# 
# The assignment operator = assigns a value to a variable. 
# In mathematics, the = operator has a different meaning. 
# In an equation, the = operator is an equality operator. 
# The left side of the equation is equal to the right one.
# 
#     >>> x = 1
#     >>> x
#     1
#     Here we assign a number to an x variable.
#     
#     >>> x = x + 1
#     >>> x
#     2
# 
# The previous expression does not make sense in mathematics. 
# But it is legal in programming. 
# The expression means that we add 1 to the x variable. 
# The right side is equal to 2 and 2 is assigned to x.
# 
#     >>> a = b = c = 4
#     >>> print a, b, c
#     4 4 4
# 
# It is possible to assign a value to multiple variables.
# 
#     >>> 3 = y
#       File "<stdin>", line 1
#     SyntaxError: can't assign to literal
# 
# This code example results in syntax error. 
# We cannot assign a value to a literal.
#
'''Arithmetic operators'''
# 
# The following is a table of arithmetic operators in Python programming language.
# 
#     Symbol    Name
#     +    Addition
#     -    Subtraction
#     *    Multiplication
#     /    Division
#     //    Floor division
#     %    Modulo
#     **    Power
# 
# The following example shows arithmetic operations.
# 
# 
#         #!/usr/bin/python
#         
#         # arithmetic.py
#         
#         a = 10
#         b = 11
#         c = 12
#         
#         add = a + b + c
#         sub = c - a
#         mult = a * b
#         div = c / 3
#         
#         pow = a ** 2
#         
#         print add, sub, mult, div
#         print pow
# 
# 
# All these are known operators from mathematics.
# 
#     $ ./arithmetic.py 
#     33 2 110 4
#     100
# 
# The division operations in Python may be surprising for beginners. 
# It is because by default, the division operator / performs integer division. 
# This means that we get an integer as a result. 
# If we want to get a more exact result, we use at least one floating point number as an operand.
# 
# 
#         #!/usr/bin/python
#         
#         # division.py
#         
#         print 9 / 3
#         print 9 / 4
#         print 9 / 4.0
#         print 9 // 4.0
#         print 9 % 4
# 
# 
# The example demonstrates division operators.
# 
#     print 9 / 4
# 
# This results in 2. The division operator works differently for integers and for floating point numbers. Integer division gives an integer result. The fraction part is truncated. Hence we get: 9 / 4 = 2
# 
#     print 9 / 4.0
# 
# Here we get the expected value: 2.25. One of the operands is a floating point number, so the result is a floating point too.
# 
#     print 9 // 4.0
# 
# Python has also a special floor division operator. The result is the floor of the value returned by true division.
# 
#     print 9 % 4
# 
# The % operator is called the modulo operator. It finds the remainder of division of one number by another. 9 % 4, 9 modulo 4 is 1, because 4 goes into 9 twice with a remainder of 1.
# 
#     $ ./division.py 
#     3
#     2
#     2.25
#     2.0
#     1
# 
#     >>> 'return' + 'of' + 'the' + 'king'
#     'returnoftheking'
# 
# The addition operator can be used to concatenate strings as well.
# 
#         >>> 3 + ' apples'
#     Traceback (most recent call last):
#       File "<stdin>", line 1, in <module>
#     TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 
# We cannot add integers and strings. 
# This results in a TypeError.
# 
#     >>> str(3) + ' apples'
#     '3 apples'
# 
# For the example to work, we must convert the number to a string using the str() function.
# 
# On the other hand, the multiplication operator can be used with a string and a number.
# 
#     >>> 'dollar ' * 5
#     'dollar dollar dollar dollar dollar '
#
'''Boolean operators'''
# 
# In Python, we have and, or and not boolean operators. 
# With boolean operators we perform logical operations. 
# These are most often used with if and while keywords.
# 
# 
#     #!/usr/bin/python
#     
#     # andop.py
#     
#     print True and True
#     print True and False
#     print False and True
#     print False and False
# 
# 
# This example shows the logical and operator. 
# The logical and operator evaluates to True only if both operands are True.
# 
#     $ ./andop.py 
#     True
#     False
#     False
#     False
# 
# The logical or operator evaluates to True if either of the operands is True.
# 
# 
#     #!/usr/bin/python
#     
#     # orop.py
#     
#     print True or True
#     print True or False
#     print False or True
#     print False or False
# 
# If one of the sides of the operator is True, the outcome of the operation is True.
# 
#     $ ./orop.py 
#     True
#     True
#     True
#     False
# 
# The negation operator not makes True False and False True.
# 
# 
#     #!/usr/bin/python
#     
#     # negation.py
#     
#     print not False
#     print not True
#     print not ( 4 < 3 )
# 
# 
# The example shows the not operator in action.
# 
#     $ ./negation.py 
#     True
#     False
#     True
# 
# And, or operators are short circuit evaluated. 
# Short circuit evaluation means that the second argument is only evaluated 
# if the first argument does not suffice to determine the value of the expression: 
#     when the first argument of and evaluates to false, the overall value must be false; 
#     and when the first argument of or evaluates to true, the overall value must be true. (wikipedia)
# 
# A typical example follows.
# 
# 
#     #!/usr/bin/python
#     
#     # shortcircuit.py
#     
#     x = 10
#     y = 0
#     
#     if (y != 0 and x/y < 100):
#           print "a small value"
# 
# 
# The first part of the expression evaluates to False. 
# The second part of the expression is not evaluated. Otherwise, we would get a ZeroDivisionError.
# 
# '''Relational Operators'''
# 
# Relational operators are used to compare values. 
# These operators always result in a boolean value.
# 
#     Symbol    Meaning
#     <    strictly less than
#     <=    less than or equal to
#     >    greater than
#     >=    greater than or equal to
#     ==    equal to
#     != or <>    not equal to
#     is    object identity
#     is not    negated object identity
# 
# The above table shows Python relational operators.
# 
#     >>> 3 < 4
#     True
#     >>> 4 == 3
#     False
#     >>> 4 >= 3
#     True
# 
# As we already mentioned, the relational operators return boolean values: True or False.
# 
# Notice that the relational operators are not limited to numbers. 
# We can use them for other objects as well. 
# Although they might not always be meaningful.
# 
#     >>> "six" == "six"
#     True
#     >>> "a" > 6
#     True
#     >>> 'a' < 'b'
#     True
# 
# We can compare string objects too. 
# We can use relational operators for different object types. 
# In our case we compare a string with a number.
# 
#     >>> 'a' < 'b'
# 
# What exactly happens here? 
# Computers do not know characters or strings. 
# For them, everything is just a number. 
# Characters are special numbers stored in specific tables. Like ASCII.
# 
# 
#     #!/usr/bin/python
#     
#     # compare.py
#     
#     
#     print 'a' < 'b'
#     
#     print "a is:", ord('a')
#     print "b is:", ord('b')
# 
# Internally, the a and b characters are numbers. 
# So when we compare two characters, we compare their stored numbers. 
# The built-in ord() function returns the ASCII value of a single character.
# 
#     $ ./compare.py 
#     True
#     a is: 97
#     b is: 98
# 
# In fact, we compare two numbers, 97 with 98.
# 
#     >>> "ab" > "aa"
#     True
# 
# Say we have a string with more characters. 
# If the first characters are equal, we compare the next ones. 
# In our case, the b character at the second position has a greater value than the a character. 
# That is why "ab" string is greater than "aa" string. 
# Comparing strings in such a way does not make much sense, of course. 
# But it is technically possible.
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
# The == operator tests for equality. 
# The is keyword tests for object identity. 
# Whether we are talking about the same object. 
# Note that more variables may refer to the same object.
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
# The empty list [] is equal to another empty list []. 
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
'''Bitwise operators'''
# 
# Decimal numbers are natural to humans. 
# Binary numbers are native to computers. 
# Binary, octal, decimal or hexadecimal symbols are only notations of the same number. 
# Bitwise operators work with bits of a binary number. 
# We have binary logical operators and shift operators. 
# Bitwise operators are seldom used in higher level languages like Python.
# 
#     Symbol    Meaning
#     ~    bitwise negation
#     ^    bitwise exclusive or
#     &    bitwise and
#     |    bitwise or
#     <<    left shift
#     >>    right shift
# 
# The bitwise negation operator changes each 1 to 0 and 0 to 1.
# 
#     >>> ~7
#     -8
#     >>> ~-8
#     7
# 
# The operator reverts all bits of a number 7. 
# One of the bits also determines, whether the number is negative or not. 
# If we negate all the bits one more time, we get number 7 again.
# 
# The bitwise and operator performs bit-by-bit comparison between two numbers. The result for a bit position is 1 only if both corresponding bits in the operands are 1.
# 
#          00110
#       &  00011
#        = 00010
# 
# The first number is a binary notation of 6, the second is 3 and the final result is 2.
# 
#     >>> 6 & 3
#     2
#     >>> 3 & 6
#     2
# 
# The bitwise or operator performs bit-by-bit comparison between two numbers. The result for a bit position is 1 if either of the corresponding bits in the operands is 1.
# 
#      00110
#   |  00011
#    = 00111
# 
# The result is 00110 or decimal 7.
# 
#     >>> 6 | 3
#     7
# 
# The bitwise exclusive or operator performs bit-by-bit comparison between two numbers. 
# The result for a bit position is 1 if one or the other (but not both) of the corresponding bits in the operands is 1.
# 
#      00110
#   ^  00011
#    = 00101
# 
# The result is 00101 or decimal 5.
# 
#     >>> 6 ^ 3
#     5
# 
# As we mentioned, bitwise operators are seldom used in Python and other high level languages. 
# Yet there are some situations, where they are used. 
# One example is a mask. 
# A mask is a specific bit pattern. 
# It determines whether some property is set or not.
# 
# Let's have an example from GUI programming.
# 
# 
#     #!/usr/bin/python
#     
#     # nominimizebox.py
#     
#     import wx
#     
#     app = wx.App()
#     window = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER 
#         | wx.SYSTEM_MENU | wx.CAPTION |     wx.CLOSE_BOX)
#     window.Show(True)
#     
#     app.MainLoop()
# 
# This is a small example of a wxPython code. 
# The wx.MAXIMIZE_BOX, wx.RESIZE_BORDER, wx.SYSTEM_MENU, wx.CAPTION, and wx.CLOSE_BOX are constants. 
# The bitwise or operator adds all these constants to the mask. 
# In our case, all these properties are set using the bitwise or operator and applied to the wx.Frame widget.
# 
# Finally, we also have bitwise shift operators. 
# The bitwise shift operators shift bits to the right or left.
# 
#     number << n : multiply number 2 to the nth power
#     number >> n : divide number by 2 to the nth power
# 
# These operators are also called arithmetic shift.
# 
#      00110
#   >>  00001
#    = 00011
# 
# We shift each of the bits of number six to the right. It is equal to dividing the six by 2. The result is 00011 or decimal 3.
# 
#     >>> 6 >> 1
#     3
# 
#      00110
#   << 00001
#    = 01100
# 
# We shift each of the bits of number six to the left. 
# It is equal to multiplying the number six by 2. 
# The result is 01100 or decimal 12.
# 
#     >>> 6 << 1
#     12

'''Compound assignment operators'''
# 
# The compound assignment operators consist of two operators. 
# They are shorthand operators.
# 
#     >>> i = 1
#     >>> i = i + 1
#     >>> i
#     2
#     >>> i += 1
#     >>> i
#     3
# 
# The += compound operator is one of these shorthand operators. 
# They are less readable than the full expressions but experienced programmers often use them.
# 
# Other compound operators are:
# 
#     -=   *=   /=   //=   %=   **=   &=   |=   ^=   >>=   <<=
# 
'''Operator precedence'''
# 
# The operator precedence tells us which operators are evaluated first. 
# The precedence level is necessary to avoid ambiguity in expressions.
# 
# What is the outcome of the following expression, 28 or 40?
# 
#     3 + 5 * 5
# 
# Like in mathematics, the multiplication operator has a higher precedence than addition operator. So the outcome is 28.
# 
#     (3 + 5) * 5
# 
# To change the order of evaluation, we can use square brackets. 
# Expressions inside square brackets are always evaluated first.
# 
# The following list shows operator precedence in Python.
# 
#    unary +  -  ~
#    **
#    *  /  %
#    +  -
#    >>  <<
#    &
#    ^
#    |
#    <  <=  ==  >=  >  !=  <>  is
#    not
#    and 
#    or
# 
# The operators on the same row have the same level of precedence. 
# The precedence grows from bottom to top.
# 
# 
#     #!/usr/bin/python
#     
#     # precedence.py
#     
#     
#     print 3 + 5 * 5
#     print (3 + 5) * 5
#     
#     print 2 ** 3 * 5
#     print not True or True
#     print not (True or True)
# 
# In this code example, we show some common expressions. 
# The outcome of each expression is dependent on the precedence level.
# 
#     rint 2 ** 3 * 5
# 
# The power operator has higher precedence than the multiplication operator. 
# First, the 2 ** 3 is evaluated, which returns 8. 
# Than the outcome is multiplied by 5. 8 * 5. 
# And the result is 40.
# 
#     print not True or True
#     
# In this case, the not operator has a higher precedence. 
# First, the first True value is negated to False that the or operator combines False and True, which gives True in the end.
# 
#     $ ./precedence.py 
#     28
#     40
#     40
#     True
#     False
# 
# The relational operators have a higher precedence than logical operators.
# 
# 
#     #!/usr/bin/python
#     
#     # positive.py
#     
#     a = 1
#     b = 2
#     
#     if (a > 0 and b > 0):
#        print "a and b are positive integers"
# 
# 
# The and operator awaits two boolean values. If one of the operands would not be a boolean value, we would get a syntax error. In Python, the relational operators are evaluated first. The logical operator then.
# 
#     $ ./positive.py 
#     a and b are positive integers
# 
'''Associativity'''
# 
# Sometimes the precedence is not satisfactory to determine the outcome of an expression. 
# There is another rule called associativity. 
# The associativity of operators determines the order of evaluation of operators with the same precedence level.
# 
#     9 / 3 * 3
# 
# What is the outcome of this expression, 9 or 1? The multiplication, deletion, and the modulo operator are left to right associated. So the expression is evaluated this way: (9 / 3) * 3 and the result is 9.
# 
# Arithmetic, boolean, relational and bitwise operators are all left to right associated.
# 
# On the other hand, the assignment operator is right associated.
# 
#     >>> a = b = c = d = 0
#     >>> a, b, c, d
#     (0, 0, 0, 0)
# 
# If the association was left to right, the previous expression would not be possible.
# 
# The compound assignment operators are right to left associated.
# 
#     >>> j = 0
#     >>> j *= 3 + 1
#     >>> j
#     0
# 
# You might expect the result to be 1. 
# But the actual result is 0. 
# Because of the associativity. 
# The expression on the right is evaluated first and than the compound assignment operator is applied.
# 
# In this chapter, we have talked about operators in Python.