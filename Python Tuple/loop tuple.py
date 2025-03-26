
# Loop through a tuple

thistuple = ("apple","banana","cherry")
for x in thistuple:
  print(x)

  # Loop Through The Index Number;
  # You can also loop through the tuple items by refrring to there index number;
  # Use the Range() and Len() functions to crate a suitable iterable;
  # Example;


thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


 # Using a while loop:
 # You can loop through the tuple items by using a while loop:
 # Use the len() function to determine the length of the tuple,thenn start at 0 and loop your way through the tuple
 # items by referring to there indexes.
 # Remember to increase the index by 1 after each iteration:
 # Example
 # Print all items,using a while loop to go through all the index number:

thistuple = ("apple","mango","cherry","banana")
i = 1 
while i < len(thistuple):
   print(thistuple[i])
   i = i + 1





