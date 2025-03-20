# Built-in Data Types

# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

# Text type  = str
# Numeric type  = int,float,complex
# Sequence type = list,tuple,range
# Mapping type = dict
# Set type = set, frozenset
# Boolen type = bool
# Binary type = bytes,bytesarray,memoryview
# None type = none


# # Getting the Data Type
# You can get the data type of any object by using the type() function:

# Example
# Print the data type of the variable x:

a = "Arshad"
print (type(a))

b = 5
print(type(b))

c = 4.3
print(type(c))

d = (7j)
print(type(d))

e = ["apple", "banana", "cherry"]	
print(type(e))

f = ("apple", "banana", "cherry")	
print(type(f))

g = range(3)
print(type(g))

h = {"Name" : "Arshad", "Age" : 22}
print(type(h))

i = {"Arshad", "Good", "Boy"}
print(type(i))

j = frozenset({"Data","Types","Python"})
print(type(j))

k = True
print(type(k))

l = b'333,Arshad'
print(type(l))

m = bytearray(98876)
print(type(m))

n = memoryview(bytes(76))
print(type(n))

o = None
print(type(o))








# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Example	                                           Data Type	Try it

# x = "Hello World"	                                   str	
# x = 20	                                            int	
# x = 20.5	                                              float	
# x = 1j	                                              complex	
# x = ["apple", "banana", "cherry"]	                        list	
# x = ("apple", "banana", "cherry")	                         tuple	
# x = range(6)	                                            range	
# x = {"name" : "John", "age" : 36}	                           dict	
# x = {"apple", "banana", "cherry"}	                           set	
# x = frozenset({"apple", "banana", "cherry"})	          frozenset	
# x = True	                                              bool	
# x = b"Hello"	                                            bytes	
# x = bytearray(5)	                                          bytearray	
# x = memoryview(bytes(5))	                             memoryview	
# x = None	                                                NoneType	



# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	                                        Data Type	

# x = str("Hello World")	                         str	
# x = int(20)	                                     int	
# x = float(20.5)	                                float	
# x = complex(1j)	                                complex	
# x = list(("apple", "banana", "cherry"))	         list	
# x = tuple(("apple", "banana", "cherry"))	        tuple	
# x = range(6)	                                     range	
# x = dict(name="John", age=36)	                     dict	
# x = set(("apple", "banana", "cherry"))	          set	
# x = frozenset(("apple", "banana", "cherry"))	    frozenset	
# x = bool(5)	                                     bool	
# x = bytes(5)	                                     bytes	
# x = bytearray(5)	                               bytearray	
# x = memoryview(bytes(5))	                       memoryview	

