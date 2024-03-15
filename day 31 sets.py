# Sets are unordered collection of data items.
# Set items are separated by commas and enclosed within curly brackets {}
# Sets are unchangeable,
# Sets do not contain duplicate items.


azeem={}
print(type(azeem)) # it show dict

# for empty set

s=set()
print(type((s)))

info = {"Carla", 19, False, 5.9, 19}
print(info) # order not maintain


# as set  set are unordered so we can not  access index numbers .
# Also sets do not allow duplicate values.

info = { 19, 19, 19}
print(info) #duplicate not allowed


# we can access using for loops


info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)  # order not maintain


t=()
print(type(t))

l=[]
print(type(l))
s=set()
print(type(s))


d={}
print(type(d))