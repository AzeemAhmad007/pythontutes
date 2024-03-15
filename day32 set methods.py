# union and union update
s1={1,2,3,4,5}
s2={5,6,7,8,9}
s3=s1.union(s2)
print(s3)
print(s1)
print(s2) # s1 and s2 are untouched same as it is

# now if we update then it will update the original set

s1={1,2,3,4,5}
s2={5,6,7,8,9}
s1.update(s2)
print(s1) # it will update the original set


# intersection and intersection update

cities1={"lahore","karachi","multan"}
cities2={"lahore","islamabad","multan"}
cities3=cities1.intersection(cities2)
print(cities3)

# Now using update with intersection

cities1={"lahore","karachi","multan"}
cities2={"lahore","islamabad","multan"}
cities1.intersection_update(cities2)
print(cities1) #  it change the original set of cities1


# symmetric differnce and update
#  those values thats not common
# (a union b)- ( a intersection b)

fruits1={"apple","banana","cherry"}
fruits2={"apple","banana","cherry2"}
fruits3=fruits1.symmetric_difference(fruits2)
print(fruits3)

# Symmertric-update
fruits1.symmetric_difference_update(fruits2)
print(fruits1) # same no changes appear


# difference and difference update ::
# returned set contains items that exist only
# in the first set, and not in both sets.

originalset={"a","b",1,"c"}
set={"d","e","c"}
set3=originalset.difference(set)
print(set3) # c is in both thats why it give a and b

# difference update

originalset={"a","b","c"}
set={"d","e","c"}
originalset.difference_update(set)
print(originalset)  # same no changes appear

# ====================set methods======================

# isdisjoint set:
# if  sets have no common item means intersection is zero it return true else false

cars1={"prado","mercedes","bmw","tesla"}
cars2={"prado","mercedes","bmw","tesla"}
print(cars1.isdisjoint(cars2)) #false

cars1={"prado","mercedes","bmw","tesla"}
cars2={"prado2","mercedes2","bmw2","tesla2"}
print(cars1.isdisjoint(cars2)) # true


# issuper set:
# set A is considered as the superset of B, if all the
#elements of set B are the elements of set A
A={1,2,3}
B={1,2,3}
print(A.issuperset(B)) #true

A={1,2,3}
B={1,2,3,4}
#print(A.issuperset(B)) #FALSE  because 4 not in A


# is subset:
# a set of which all the elements are contained in another set.

A={1,2,3}
B={1,2,3,}
print(A.issubset(B)) # A ki all values b ma ho to true


# add :
# used to add single elment
numbers={1,2,3,4}
numbers.add(5)
print(numbers)

#  remove  and discord

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
#cities.remove("newyork")
#print(cities)  # remove raise error when item not present and we want to remove that

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("newyork")
print(cities)  # no error found


# pop removes a random value
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(item) # it will show  the  element that remove  that could be any from set
print(cities)

# del method

l={22,23.5,"apple",True}
del l
#print(l)  # name 'l' is not defined

#  clear  method  clears the whole list
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)  # set()


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")




# symetric difference


a={1,2,3,4 ,15,6}
b={1,2,3,4,5,6}
print(a.union(b) - a.intersection(b))
print(a.symmetric_difference(b)) # symettric difference means  all values that not common
print(a) # a will be untouched

# difference means  those element  that in first  set not in both
x={1,2,3,4,"a"}
y={1,2,3,4,5,6}
print(x.difference(y)) # 1 to 4  are  in both set so all ignore also 5 ,6 ignore so it print "a"


t1={1,2}
t2={11,12}
print(t1.isdisjoint(t2)) # true because intersection is 0



# super set

a1={"a","b"}
a2={"a","b","c"}
print(a1.issuperset(a2)) # superset a ki all value agar b ma ho to true
print(a1.issubset(a2)) # subset bki all value agar a ma ho to true






# practice
#
# names1={"azeem","harry","ahmad","hammad"}
# names2={"azeem","harry","ahmad","hammad"}
# names3={"azeem","harry","ahmad","hammad3","hammad"}
# names4={"azeem3","names"}
# print(names1.symmetric_difference(names2)) # empty because as defination intersection should be 0
# print(names1.symmetric_difference(names3)) # values that not commen is hammad and hammad3
#
# print(names1.difference(names2)) #  empty because set 1 ki wo values jo set 2 ma na ho 2 wale ki ignore
# print(names1.difference(names3))  # hammad
#
# print(names1.isdisjoint(names4)) # true because intersection is 0
#
# print(names1.issuperset(names2)) # true because b ki all values a ma ho to
# print(names1.issuperset(names3)) #  false
# print(names2.issubset(names1)) # true because a ki all values b ma ho to
# print(names2.issubset(names3)) #  ik b miss hoi to  it will return false

num1={1,2,3,4,5}
num2={11,12,13,14,15}
num12={11,12,13,14,15}
print(num2.symmetric_difference(num1)) # all values jo k commen na ho

print(num1.difference(num12)) # set 1 ki all values jo k set  2 ma na ho
print(num1.isdisjoint(num2)) # true because 0 intersection

a3={1,2,3,4}
a4={1,2,3}
print(a3.issubset(a4))   # true agar a ki all valus b ma ho
print(a3.issuperset(a4))   # true agar  b ki all valus a ma ho
a3.add(66)
print(a3)
a3.remove(3)
#a3.remove(13)  # it will give error
print(a3)
a3.discard(13)
print(a3)  # no error found

a4.clear()
print(a4)
del a3
#print(a3)
try:
    del a3
    print(a3)
except Exception as e:
    print(e)
print(a3)  # it show error
