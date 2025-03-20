

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

  #Nagetive Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


  #Range of Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  
  #By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


   #Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


"""
Check if Item Exists
To determine if a specified item is present in a list use the in keyword:
Example
Check if "apple" is present in the list:
"""

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")