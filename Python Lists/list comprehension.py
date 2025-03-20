   
# List comprehension

fruits = ['Apple', "banana", 'Mango', "orange"]
newlist = []
for x in fruits:
    if 'o' in x:
      newlist.append(x)
print(newlist)

   # With list comprehension you can do all that with only one line of code:

fruits = list(("apple", "banana","mango","cherry", "orange"))
newlist = [x for x in fruits if 'a' in x]
print(newlist)



  # The Syntax
'''
   newlist = [expression for item in iterable if condition == True]
'''#The return value is a new list, leaving the old list unchanged.

  # Condition
  #  The condition is like a filter that only accepts the items that evaluate to True.

   # Example
    # Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]
print(newlist)



   # With no if statement:

newlist = [x for x in fruits]
print(newlist)

'''
Iterable
The iterable can be any iterable object, like a list, tuple, set etc.
Example
You can use the range() function to create an iterable:
'''

newlist = [x for x in range(10)]
print(newlist)


'''
Same example, but with a condition:
Example
Accept only numbers lower than 5:
'''
newlist = [x for x in range(10) if x < 5]
print(newlist)


'''
Expression
The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
Example
Set the values in the new list to upper case:
'''
newlist = [x.upper() for x in fruits]
print(newlist)


  # Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
print(newlist)

'''
The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
Example
Return "orange" instead of "banana":
'''
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)