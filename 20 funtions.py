# A function is a block of code that performs a specific task whenever it is called.
# function is used to break big  program into small programs.


# Builtin functions:
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.


# user defined functions created by using  def keyword.

 # syntex:
# def function_name(parameters):
#   pass
  # Code and Statements
def sum(a,b):
    print("sum",a+b)
sum(9,6)
sum(14,16)

def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
gmean(7,8)


num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))
def isgreater(a,b):
    if a>b:
        print("First number is greater, way 1")
    else:
        print("second number is greater, way 1")
isgreater(num1,num2)
def isgreater(c,d):
    if c>d:
        print("c is greater, way 1")
    else:
        print("d is greater, way 1")
isgreater(4,9)


# now using   function in this  2nd way::
a=40
b=30
c=20
d=50
def isgreater(a,b):
    if a > b:
        print("First number is greater, 2nd way")
    else:
        print("second number is greater , 2nd way")
isgreater(a,b)
isgreater(c,d)

def average(a,b):
    average=(a+b)/2
    print("The average of \"a\" and \"b\"  is ",average)
average(4,6)


def islesser(g,h):
    if g<h:
        print("g is lesser")
    else:
        print("h is lesser")
islesser(1,2)

def name(fname, mname,lname):
    print("Hello,", fname,mname, lname)

name("azeem", "rehmat", "ali")