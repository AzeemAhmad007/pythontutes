# list methods

# sort: used  to convert in ascending order
listofnumbers=[2,5,3,5,77,1,2,4,73,6,10]
print(listofnumbers)
listofnumbers.sort()
print(listofnumbers) #sorting ascending  order
listofnumbers.sort(reverse=True)
print(listofnumbers) # descending  order

#reverse: used to reverse list
list=[5,4,3,2,1]
list.reverse()
print(list)

#  index()
# This method returns the index of the """first""" occurrence of the list item.

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))

# count
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(3)) # 2



# copy()
# Returns copy of the list. This can be done to perform operations on
# the list without modifying the original list.
list2=["apple","mango","bannana","guava"]
nlist=["dates","strawberry"]
list1=list2.copy()
print(list2)
print(nlist)

# append

list2=["apple","mango","bannana","guava"]
(list2.append("dates"))
(list2.append("grapes"))
print(list2)

# insert  method is used  to inserts an item at the given index

cars=["mercedes","carola","suzoki","bmw"]
cars.insert(2,"swift")
cars.insert(0,"parado")
print(cars)


# extend  is used to add entire list  or tuple dict etc to the exicinting list

list2=["apple","mango","bannana","guava"]
nlist=["dates","strawberry"]
list2.extend(nlist)
print(list2)



# concetinating  two lists:

print("with the help of concetinating")

list2=["apple","mango","bannana","guava"]
nlist=["dates","strawberry"]
print(list2+nlist)