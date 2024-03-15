# lambda functions are small  anonymous functions which has no name
# A lambda function can take any number of arguments, but can only have one expression. (single)
# use function as a variable
# only used when we need to make  mini functions
# main use :: we can pass function as a argument also we an pass funcation as a function

# def triple(x):
#     return x*3
#
# print(triple(2))

triple=lambda x:x*3
print(triple(2)) # same answer

cube=lambda x:x*x*x
print(cube(5))

double=lambda x:x*x
print(double(5))


# multiples values

average=lambda x,y:(x+y)/2
print(average(3,5))


average=lambda x,y,z:(x+y+z)/3
print(average(3,5,10))


sum=lambda x,y:x+y
print(sum(9,6))


# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y
print(multiply(3,10))
# Lambda function to calculate the product of two numbers
multiplication=lambda x, y: x * y
print(multiply(3,10))

# used as arguments to higher-order functions, such as map, filter, and reduce.

def func(fx, value):
    return 10 + fx(value)

print(func(double,2)) #  square of 2 and add 10

# we can also do this without  making lambda function

print(func(lambda x:x*x,5))
