#!/usr/bin/python
# -*- coding: utf-8 -*-
#
'''Python dictionaries'''
# 
# In this part of the Python programming tutorial, we will cover Python dictionaries in more detail.
# 
# Python dictionary is a container of key-value pairs. 
# It is mutable and can contain mixed types. 
# A dictionary is an unordered collection. 
# Python dictionaries are called associative arrays or hash tables in other languages. 
# The keys in a dictionary must be immutable objects like strings or numbers. 
# They must also be unique within a dictionary.
# 
'''Creating dictionaries'''
# 
# First, we will show how to create Python dictionaries.
# 
# 
#     #!/usr/bin/python
#      
#     weekend = { "Sun": "Sunday", "Mon": "Monday" }
#     vals = dict(one=1, two=2)
#      
#     capitals = {}
#     capitals["svk"] = "Bratislava"
#     capitals["deu"] = "Berlin"
#     capitals["dnk"] = "Copenhagen"
#      
#     d = { i: object() for i in range(4) }
#      
#     print weekend
#     print vals
#     print capitals
#     print d
# 
# 
# In the example, we create four dictionaries. 
# In four different ways. 
# Later we print the contents of these dictionaries to the console.
# 
#     weekend = { "Sun": "Sunday", "Mon": "Monday" }
# 
# We create a weekend dictionary using dictionary literal notation. The key-value pairs are enclosed by curly brackets. The pairs are separated by commas. The first value of a pair is a key, which is followed by a colon character and a value. The "Sun" string is a key and the "Sunday" string is a value.
# 
#     vals = dict(one=1, two=2)
# 
# Dictionaries can be created using the dict() function.
# 
#     capitals = {}
#     capitals["svk"] = "Bratislava"
#     capitals["deu"] = "Berlin"
#     capitals["dnk"] = "Copenhagen"
# 
# This is the third way. 
# An empty capitals dictionary is created. 
# Three pairs are added to the dictionary. 
# The keys are inside the square brackets, the values are located on the right side of the assignment.
# 
#     d = { i: object() for i in range(4) }
# 
# A dictionary is created using a dictionary comprehension. 
# The comprehension has two parts. 
# The first part is the i: object() expression, which is executed for each cycle of a loop. 
# The second part is the for i in range(4) loop. 
# The dictionary comprehension creates a dictionary having four pairs, 
# where the keys are numbers 0, 1, 2, and 3 and the values are simple objects.
# 
#     $ ./create_dict.py 
#     {'Sun': 'Sunday', 'Mon': 'Monday'}
#     {'two': 2, 'one': 1}
#     {'svk': 'Bratislava', 'dnk': 'Copenhagen', 'deu': 'Berlin'}
#     {0: <object object at 0xb76cb4a8>, 1: <object object at 0xb76cb4b0>, 
#     2: <object object at 0xb76cb4b8>, 3: <object object at 0xb76cb4c0>}

'''Basic operations'''
# 
# The following examples will show some basic operations with Python dictionaries.
# 
# 
#     #!/usr/bin/python
#      
#     basket = { 'oranges': 12, 'pears': 5, 'apples': 4 }
#      
#     basket['bananas'] = 5
#      
#     print basket
#     print "There are %d various items in the basket" % len(basket)
#      
#     print basket['apples']
#     basket['apples'] = 8
#     print basket['apples']
#      
#     print basket.get('oranges', 'undefined')
#     print basket.get('cherries', 'undefined')
# 
# 
# We have a basket with different fruits. 
# We perform some operations on the basket dictionary.
# 
#     basket = { 'oranges': 12, 'pears': 5, 'apples': 4 }
# 
# The basket dictionary is created. It has initially three key-value pairs.
# 
#     basket['bananas'] = 5
# 
# A new pair is created. 
# The 'bananas' string is a key, the 5 integer is the value.
# 
#     print "There are %d various items in the basket" % len(basket)
# 
# The len() function gives the number of pairs in the dictionary.
# 
#     print basket['apples']
# 
# The value of the 'apples' key is printed to the terminal.
# 
#     basket['apples'] = 8
# 
# The value of the 'apples' key is modified. 
# It is set to number 8.
# 
#     print basket.get('oranges', 'undefined')
# 
# The get() method retrieves the value of a specified key. 
# If there is no such a key, the second parameter of the method is returned.
# 
#     print basket.get('cherries', 'undefined')
# 
# This line returns 'undefined'. There are no cherries in the basket.
# 
# $ ./basics.py
# {'bananas': 5, 'pears': 5, 'oranges': 12, 'apples': 4}
# There are 4 various items in the basket
# 4
# 8
# 12
# undefined
# 
# Example output.
# 
# The next example will present two dictionary methods: the fromkeys() and the setdefault() method.
# 
# 
#     #!/usr/bin/python
#      
#     basket = ('oranges', 'pears', 'apples', 'bananas')
#      
#     fruits = {}.fromkeys(basket, 0)
#     print fruits
#      
#     fruits['oranges'] = 12
#     fruits['pears'] = 8
#     fruits['apples'] = 4
#      
#     print fruits.setdefault('oranges', 11)
#     print fruits.setdefault('kiwis', 11)
#      
#     print fruits
# 
# 
# The fromkeys() method creates a new dictionary from a list. 
# The setdefault() method returns a value if a key is present. 
# Otherwise it inserts a key with a specified default value and returns the value.
# 
#     basket = ('oranges', 'pears', 'apples', 'bananas')
# 
# We have a list of strings. From this list a new dictionary will be constructed.
# 
#     fruits = {}.fromkeys(basket, 0)
# 
# The fromkeys() method creates a new dictionary, where the list items will be the keys. Each key will be initiated to 0. Note that the fromkeys() method is a class method and needs the class name, which is {} in our case, to be called.
# 
#     fruits['oranges'] = 12
#     fruits['pears'] = 8
#     fruits['apples'] = 4
# 
# Here we add some values to the fruits dictionary.
# 
#     print fruits.setdefault('oranges', 11)
#     print fruits.setdefault('kiwis', 11)
# 
# The first line prints 12 to the terminal. The 'oranges' key exists in the dictionary. In such a case, the method returns the its value. In the second case, the key does not exist yet. A new pair 'kiwis': 11 is inserted to the dictionary. And value 11 is printed to the console.
# 
#     $ ./fruits.py 
#     {'bananas': 0, 'pears': 0, 'oranges': 0, 'apples': 0}
#     12
#     11
#     {'kiwis': 11, 'bananas': 0, 'pears': 8, 'oranges': 12, 'apples': 4}
# 
# We receive this output, when we launch the fruits.py script.
# 
# The next code example will show, how to add two Python dictionaries.
# 
# 
#     #!/usr/bin/python
#      
#     domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
#     domains2 = { "us": "United States", "no": "Norway" }
#      
#     domains.update(domains2)
#      
#     print domains
# 
# 
# We have two dictionaries. 
# They are joined with the update() method.
# 
#     domains.update(domains2)
# 
# The domains2 dictionary is added to the domains dictionary with the update() method.
# 
#     $ ./domains.py
#     {'sk': 'Slovakia', 'de': 'Germany', 'no': 'Norway', 
#     'us': 'United States', 'hu': 'Hungary'}
# 
# The result shows all values from both dictionaries.
# 
# Now we will show, how to remove a pair from a dictionary.
# 
# 
#     #!/usr/bin/python
#      
#     items = { "coins": 7, "pens": 3, "cups": 2, 
#         "bags": 1, "bottles": 4, "books": 5 }
#      
#     print items    
#      
#     items.pop("coins")
#     print items
#      
#     del items["bottles"]
#     print items
#      
#     items.clear()
#     print items
# 
# 
# The items dictionary has 6 key-value pairs. 
# We will delete pairs from this dictionary.
# 
#     items.pop("coins")
# 
# The pop() method removes a pair with a specified key.
# 
#     del items["bottles"]
# 
# The del keyword deletes a "bottles": 4 pair from the items dictionary.
# 
#     items.clear()
# 
# The clear() method clears all items from the dictionary.
# 
#     $ ./removing.py 
#     {'bags': 1, 'pens': 3, 'coins': 7, 'books': 5, 'bottles': 4, 'cups': 2}
#     {'bags': 1, 'pens': 3, 'books': 5, 'bottles': 4, 'cups': 2}
#     {'bags': 1, 'pens': 3, 'books': 5, 'cups': 2}
#     {}
#
#  This is the example output.

'''Keys and values'''
# 
# A Python dictionary consists of key-value pairs. 
# The keys() method returns a list of keys from a dictionary. 
# The values() method creates a list of values. 
# And the items() method returns a list of key-value tuples.
# 
# 
#     #!/usr/bin/python
#      
#     domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
#         "us": "United States", "no": "Norway"  }
#      
#     print domains.keys()
#     print domains.values()
#     print domains.items()
#      
#     print "de" in domains
#     print "cz" in domains
# 
# 
# We demonstrate the above mentioned methods. 
# We also check if a key is present with the in keyword.
# 
#     print domains.keys()
# 
# We print the list of keys of a domains dictionary with the keys() method.
# 
#     print domains.values()
# 
# We print the list of values of a domains dictionary with the values() method.
# 
#     print domains.items()
# 
# And finally, we print the list of key-value tuples of a domains dictionary using the items() method.
# 
#     print "de" in domains
#     print "cz" in domains
# 
# With the in keyword, we check if the "de", "cz" keys are present in the domains dictionary. 
# The return value is either True or False.
# 
#     $ ./keys_values.py
#     ['sk', 'de', 'no', 'us', 'hu']
#     ['Slovakia', 'Germany', 'Norway', 'United States', 'Hungary']
#     [('sk', 'Slovakia'), ('de', 'Germany'), ('no', 'Norway'), 
#     ('us', 'United States'), ('hu', 'Hungary')]
#     True
#     False
# 
# Output of the example.

'''Looping'''
# 
# Looping through the dictionary is a common programming job. This can be done with the for keyword.
# 
# 
#     #!/usr/bin/python
#      
#     domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary",
#         "us": "United States", "no": "Norway"  }
#      
#     for key in domains:
#         print key
#          
#     for k in domains:
#         print domains[k]
#          
#     for k, v in domains.items():
#         print ": ".join((k, v))
# 
# 
# In the example, we traverse the domains dictionary to print the keys, values and both keys and values of the dictionary.
# 
#     for key in domains:
#         print key
# 
# This loop prints all the keys of the dictionary.
# 
#     for k in domains:
#         print domains[k]
# 
# The second loop prints all values of the dictionary.
# 
#     for k, v in domains.items():
#         print ": ".join((k, v))
# 
# In the final loop, all keys and values are printed.
# 
#     $ ./looping.py
#     sk
#     de
#     no
#     us
#     hu
#     Slovakia
#     Germany
#     Norway
#     United States
#     Hungary
#     sk: Slovakia
#     de: Germany
#     no: Norway
#     us: United States
#     hu: Hungary
# 
# Output of the example.

'''Sorting'''
# 
# Python dictionaries are orderless. 
# This also implies that they cannot be sorted like a Python list. 
# Programmers can create sorted representations of Python dictionaries. 
# In this section, we will show several ways to create a sorted output.
# 
# Programmers might want to sort the data in a normal or reverse order. 
# They could sort the data by keys or by values.
# 
# 
#     #!/usr/bin/python
#      
#     items = { "coins": 7, "pens": 3, "cups": 2, 
#         "bags": 1, "bottles": 4, "books": 5 }
#          
#     kitems = items.keys()
#     kitems.sort()
#      
#     for k in kitems:
#         print ": ".join((k, str(items[k])))
# 
# 
# The first example provides the simplest solution to have the data sorted by the keys.
# 
#     kitems = items.keys()
#     kitems.sort()
# 
# A list of keys is obtained from the dictionary. The list is sorted with the sort() method.
# 
#     for k in kitems:
#         print ": ".join((k, str(items[k])))
# 
# In the loop we print the sorted keys together with their values from the dictionary.
# 
#     $ ./simplesort.py
#     bags: 1
#     books: 5
#     bottles: 4
#     coins: 7
#     cups: 2
#     pens: 3
# 
# The items dictionary is sorted by its keys.
# 
# More efficient sorting can be done with the built-in sorted() function.
# 
# 
#     #!/usr/bin/python
#      
#     items = { "coins": 7, "pens": 3, "cups": 2, 
#         "bags": 1, "bottles": 4, "books": 5 }
#          
#     for key in sorted(items.iterkeys()):
#         print "%s: %s" % (key, items[key])
#      
#     print "####### #######"    
#          
#     for key in sorted(items.iterkeys(), reverse=True):
#         print "%s: %s" % (key, items[key])
# 
# 
# In the example we print sorted data by their keys in ascending and descending order using the sorted() function.
# 
#     for key in sorted(items.iterkeys()):
#         print "%s: %s" % (key, items[key])
# 
# In this for loop, we print the pairs sorted in ascending order. 
# The iteritems() function returns an iterator over the dictionary’s (key, value) pairs.
# 
#     for key in sorted(items.iterkeys(), reverse=True):
#         print "%s: %s" % (key, items[key])
# 
# In the second for loop, the data is sorted in descending order. 
# The order type is controlled by the reverse parameter.
# 
#     $ ./sorting.py
#     bags: 1
#     books: 5
#     bottles: 4
#     coins: 7
#     cups: 2
#     pens: 3
#     ####### #######
#     pens: 3
#     cups: 2
#     coins: 7
#     bottles: 4
#     books: 5
#     bags: 1
# 
# Output of the sorting.py script.
# 
# In the next example, we are going to sort the items by their values.
# 
# 
#     #!/usr/bin/python
#      
#     items = { "coins": 7, "pens": 3, "cups": 2, 
#         "bags": 1, "bottles": 4, "books": 5 }
#          
#     for key, value in sorted(items.iteritems(), 
#         key=lambda (k,v): (v,k)):
#              
#         print "%s: %s" % (key, value) 
#      
#     print "####### #######"    
#          
#     for key, value in sorted(items.iteritems(), 
#         key=lambda (k,v): (v,k), reverse=True):
#               
#         print "%s: %s" % (key, value)  
# 
# 
# The example prints the data in ascending and descending order by their values.
# 
#     for key, value in sorted(items.iteritems(), 
#         key=lambda (k,v): (v,k)):
# 
# Dictionary pairs are sorted by their values and printed to the console. 
# The key parameter takes a function, which indicates, how the data is going to be sorted.
# 
#     $ ./sorting2.py
#     bags: 1
#     cups: 2
#     pens: 3
#     bottles: 4
#     books: 5
#     coins: 7
#     ####### #######
#     coins: 7
#     books: 5
#     bottles: 4
#     pens: 3
#     cups: 2
#     bags: 1
# 
# From the output we can see that this time the pairs were sorted according to their values.
# 
'''Views'''
# 
# Python 2.7 introduced dictionary view objects. 
# Views provide a dynamic view on the items of a dictionary. 
# They bear similarity to SQL views. 
# When the dictionary changes, the view reflects these changes. 
# The dict.viewkeys(), dict.viewvalues() and dict.viewitems() methods return view objects.
# 
# A view is a virtual read-only container. 
# A view does not make a copy of a dictionary.
# 
# 
#     #!/usr/bin/python
#      
#     fruits = { 'oranges': 12, 'pears': 5, 'apples': 4, 'bananas': 4 }
#      
#     vi = fruits.viewitems()
#     vv = fruits.viewvalues()
#     vk = fruits.viewkeys()
#      
#     for k, v in vi:
#         print k, v
#      
#     for v in vv:
#         print v
#          
#     for k in vk:
#         print k
# 
# 
# Three view objects of the dictionary's items, dictionary's keys and dictionary's values are created. 
# We traverse the view with the for loops.
# 
#     vi = fruits.viewitems()
# 
# The viewitems() creates a view of the dictionary's items.
# 
#     for k, v in vi:
#         print k, v
# 
# We traverse the created view and print the keys and values in the for loop.
# 
#     $ ./views.py
#     bananas 4
#     pears 5
#     oranges 12
#     apples 4
#     4
#     5
#     12
#     4
#     bananas
#     pears
#     oranges
#     apples
# 
# Output of the views.py script.
# 
# In the next example we show that a view reflects dictionary changes.
# 
# 
#     #!/usr/bin/python
#      
#     fruits = { 'oranges': 12, 'pears': 5, 'apples': 4, 'bananas': 4}
#      
#     vi = fruits.viewitems()
#      
#     for k, v in vi:
#         print k, v
#      
#     fruits.pop('apples')
#     fruits.pop('oranges')
#      
#     print "########### ##########"
#      
#     for k, v in vi:
#         print k, v
# 
# 
# A view is created on the fruits dictionary. 
# Two items are deleted from the dictionary. 
# Then we traverse the view to see if the changes are reflected.
# 
#     vi = fruits.viewitems()
# 
# A view is created on the fruits dictionary.
# 
#     fruits.pop('apples')
#     fruits.pop('oranges')
# 
# Two items are deleted with the pop() method.
# 
#     for k, v in vi:
#         print k, v
# 
# We loop through the view of the fruits.
# 
#     $ ./views2.py
#     bananas 4
#     pears 5
#     oranges 12
#     apples 4
#     ########### ##########
#     bananas 4
#     pears 5
# 
# From the output we can see that the changes were reflected in the view.
# 
# In this part of the Python tutorial, we have written about Python dictionaries.