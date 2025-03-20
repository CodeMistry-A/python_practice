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
# 1. Convert into a list : Just like workaround for changing a tuple,you can convert into a list,add yours item(s)
#     and convert it back into a tuple.

#   Example;convert the tuple into a list ,add,orange and convert into back a tuple.

thistuple = ('apple','banana','cherry')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)

print(thistuple)