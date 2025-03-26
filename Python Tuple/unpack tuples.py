fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using Asterisk*
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
#Example
#Assign the rest of the values as a list called "red":

fruits = ("apple","banana","cherry","strawberry","respberry")
(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)


# Example
# Add a list of value the "tropic" values

fruits = ("apple","mango","papaya","pineapple","cherry")
(green,*tropic,red) = fruits
print(green)
print(tropic)
print(red)