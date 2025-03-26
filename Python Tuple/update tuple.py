# Change Tuples Values
"""
Once a tuple is created,you cannot change its Value.
Tuples are unchangeable,or immutable as it also as called.
But there is workaround,You can convert tuples into a list.
change the list,and convert the list back into tuple.
"""
# Example
# Convert the tuple into a list to be able to change it.

x = ("apple","banana","cherry","mango")
y = list(x)
y[3] = 'orange'
x = tuple(y)

print(x)


# Add items in tuple
# since
# tuple are immutable, they do not have built-in append() methods,but there are other ways to add items to a tuple.
'''
 1. Convert into a list : Just like workaround for changing a tuple,you can convert into a list,add yours item(s)
     and convert it back into a tuple.
'''
#   Example;convert the tuple into a list ,add,orange and convert into back a tuple.

thistuple = ('apple','banana','cherry')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)

print(thistuple)



'''
2. Add tuple to a tuple - You are allowed to add tuple to tuples,so if you want add one item,(or many),
create a new tuple with the item(s),and add to it the existing tuple.'
'''#Example  (create a new tuple with the value "orange",and add that tuple)

thistuple = ("apple","banana",'cherry')
y = "mango",
thistuple += (y)

print(thistuple)


# Remove Items
# Note : you can't remove items in a tuple
""" tuple are unchangeable,so you can't remove items from it,but you can use the smae workaround as we used for changing
    and adding tuple items,"""
# Example
# Convert the tuple into a list,remove 'apple' and convert into back in tuple.

thistuple = ("apple","mango","banana","orange")
y = list(thistuple)
y.remove("orange")

thistuple = tuple(y)
print(thistuple)

# or you can delete the tuple completely:
# Exmaple:

thistuple = ("MOHD","ARSHAD","KHAN")
del thistuple
print(thistuple)