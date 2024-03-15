# tuple Tuples are ordered collection of data items
# Tuple items are separated by commas and enclosed within round brackets (). Immutable cannot change
t=(1,2,3)
print(type(t),t)
t=(1,2)
print(type(t))  # <class 'tuple'>
t=(1)
print(type(t)) # <class 'int'> so if we want to avoid this  comma is nesscesary

t=(1,)
print(type(t))  # <class 'tuple'>

t2=(3,4,5,6)
print(t2[0])
print(t2[1])
print(t2[2])
print(t2[3])

# slicing

t3=(1,2,3,4,5,66,221,21,32,23)
print(t3[:])
print(t3[0:])
print(t3[:10])
print(t3[0:10])
print(t3[3:9])

#  negative slicing

nt=(1,7,9,23,33,45,711)
print(nt[-4])
print(nt[len(nt)-4])


# in keyword


country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")





