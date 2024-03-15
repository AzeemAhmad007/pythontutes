# is and == are both comparison operators
# used to check if two values are equal


#  is operator compares the identity of two objects
# == operator compares the values of the objects

#  is will only return True if the objects being compared are
#  the exact same object in memory

 #  == will return True if the objects have the same value.


a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True because both are same in value
print(a is b)  # False because   not the same object in memory


# for immutable objects it will return true for both and  is and == will always return the same result

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True

tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)
print(tuple1 is tuple2) # true
print(tuple1 == tuple2) # true



# ========= mutable objects such as lists and dictionaries, is and == can behave differently===========


# use is when you want to check if two objects are the same object in memory.
# use == when we need to campare 2 values


































































