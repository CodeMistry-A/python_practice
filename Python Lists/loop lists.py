
   # you can loop through the list items by using a for loop:
thislist = ["apple",'banana',"cherry"]
for x in thislist:
   print(x)


   # you can also loop through the list itmes by reffering to their index number:
   # Use the range() and len() functions to create a suitable lterable:
thislist = ["Apple","Banana","Cherry"] 
for i in range (len(thislist)):
 print(thislist[i]) 
   # The iterable created in the example above is [0, 1, 2].


   # Using a while loop
thislist = ["apple","banana","cherry","mango"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  

  # looping using list comprehension
  # A short hand for loop that will print all items in a list:
thislist = ["Apple", "Banana", "Cherry"]
[print(x)for x in (thislist)]   
