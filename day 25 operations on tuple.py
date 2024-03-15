# as  we know tuple  is immutable we cannot change it directly but we can change it indirectly

countries = ("Spain", "Italy", "India", "England", "Germany")
t = list(countries)  # we use  here list function to convert in list then we can do various operations
t.append("Russia")       #add item at the end
t.pop(3)                 #remove item at the index 3
t[2] = "Finland"         #change item  add finland at index 2
countries = tuple(t)  # here we again convert into  tuple .also can be dict set tuple list etc
print(countries)

# COUNT
tuple=(1,2,2,4,5,6,7,2,2,4)
print(tuple.count(2))
#
# #  index()
# This method returns the index of the first occurrence of the tuple item.
print(tuple.index(7)) #it gives the index
# print(tuple.index(766)) # error:x not in tuple
