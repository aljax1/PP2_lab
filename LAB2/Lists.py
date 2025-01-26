#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#5
list1 = ["abc", 34, True, 40, "male"]
print(list1)
#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))




#Access List Items
#1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])




#Change List Items
#1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)



#Add List Items
#1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove List Items
#1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#4
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)



#Loop Lists
#1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension
#1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)




#Sort Lists
#1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Copy Lists
#1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#3
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


#Join Lists
#1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


