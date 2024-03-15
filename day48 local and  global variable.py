# variable created inside the function called local variable
# variable created outside the function called global variable

#  we can not use local varaiable outside the  function



x=5 # global variable
def hello():
    x=6  #local variable
    print(f"thi is  local variable : {x}")
    print("hello")
hello()
print(f"this is global variable : {x}")


# Global keyword

# we can change global variable inside the function using  global keyword


y=55
def function():
    global y
    print(f"before updating the value : {y}")
    y=100
    print(f"after using global keyword new value : {y}")
function()


def input():
    z=1
    print(z) # we can just use it inside the function
input()
#print(z) # NameError: name 'z' is not defined