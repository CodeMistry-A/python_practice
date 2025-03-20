  #Remove "And":
thsilist = ["Arshad","And","Anjum"]
thsilist.remove("And")
print(thsilist)



  #Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)



  #Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)


  #Remove the last item
thislist =["apple","banana",'cherry'] 
thislist.pop()
print(thislist)


  #the del keyword also remove specified index:
thislist = ["apple","banana","cherry"]
del thislist[0]
print(thislist)  

  #the del keyword can also delete the list completely:
thislist = ["apple","banana",'cherry'] 
del thislist 


  #the clear() methods empeties the list
thislist =["apple",'banana',"cherry"]
thislist.clear()
print(thislist)  