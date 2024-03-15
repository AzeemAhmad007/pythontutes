# There are four types of arguments that we can provide in a function:
#
# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments


def average(a,b):
    average=(a+b)/2
    print("Average is ",average)
average(4,4)

# Default Arguments
def average(a=9,b=21):
    average=(a+b)/2
    print(average)
average() # we dont give any argument here

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy") # mname  and lname is defualt arguments


# Keyword Arguments
# we can provide arguments as a key value pair and  order in which argument passed does not matter

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Wesker", "jade")


# required arguments


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

#name() # TypeError: name() missing 3 required positional arguments: 'fname', 'mname', and 'lname'
name("azeem","rehmat","ali")


# Variable length Arguments

def name(**name):    # ** is used   to call function and  bound in the dictionary
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

# return Statement
# The return statement is used to return the value of the expression back to the calling function.
#
# Example:

def name(fname, mname, lname):
    return "Hello, " + fname  +" " , mname , " " , lname

print(name("James", "Buchanan", "Barnes"))


