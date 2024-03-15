# map filter and reduce are builtin functions
# used to apply a function  to a sequence of elements and  return a new sequence
# known as higher-order functions, as they take other functions as arguments.


# MAP::
# map function is used to  apply a function to a sequence of elements and return a new sequence



#  syntax::

# average=map(function,iterable[list,set,tuple,dic])


marks=[4,5,88,9,1,2]
# we need to apply the sum function that add "2" to all elements\

def sum(x):
    return x+2

# after_sum_function=[]
#
# for item in marks:
#     after_sum_function.append(sum(item))
#
# print(after_sum_function)

# instead of doing this we can use map function  and that is ,much easy

marks=[4,5,88,9,1,2]
def sum(x):
    return x+2
new_marks=map(sum,marks)
print(new_marks) #  <map object at 0x0000000000468FD0>
new_marks=list(map(sum,marks))
print(new_marks) #  [6, 7, 90, 11, 3, 4]





tuple=(5.5,7.0,8.9,1.1,2.5,9.4)
def multiply(x):
    return x*2
new_tuple=map(multiply,tuple)
print(new_tuple) # <map object at 0x00000000025D8940>

new_tuple=list(map(multiply,tuple))
print(new_tuple)  # [11.0, 14.0, 17.8, 2.2, 5.0, 18.8]


print("this is filter program\n")

# FILTER
marks=[4,5,8,9,1,2]
def filter1(x):
    return x>4 # if condition true it will print else not  print

filter=list(filter(filter1,marks))
print(filter) # [5, 8, 9]


# practice

list_of_strings=["azeem","harry","tashif","sharaf"]
def string(a):
    return a +" is a good boy\n"
newlist=map(lambda a:a+" is a good boy\n",list_of_strings) # lambda method also work
newlist=map(string,list_of_strings)
print(newlist) #<map object at 0x0000000001E48970>
print(list(newlist))

newlist=list(map(string,list_of_strings))
print(newlist)

for  name in newlist:
    print(name,end="")



#Filter

fruits=["apple","grapes","dates","watermellon","berry","strawberry"]
def f(a):
    return len(a) > 5
try:
    filtered_fruits=filter(f,fruits) # already use filter thats why erros showing
    print(list(filtered_fruits))  # ['grapes', 'watermellon', 'strawberry']
except Exception as e:
    print(e)

#REDUCE

# higher-order functions
# applies a function to a sequence and returns a single value.
# first we need to import from functools

from functools import reduce

l=[1,2,3,4,5,6]
# l=[1,2,3,4,5,6]
# l=[3,3,4,5,6]
# l=[6,4,5,6]
# l=[10,5,6]
# l=[15,6]
# l=[21]

def add(x,y):
    return x+y
newl=reduce(add,l)
print(newl) # 21

#  for lambada function

newl2=reduce(lambda x,y:x*y,l)
print(newl2) # 720