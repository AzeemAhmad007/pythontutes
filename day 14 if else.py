# if else  used to check expression is it  evaluate true of false
# if else works  on conditional operators .

a=int(input("Enter your age\n"))
print("your age is ",a)
if a>18:
    print("YEs you can drive")
else:
    print("you cannot drive")


# elif

num=int(input("enter the number\n"))
print("number is ",num)
if num>10:
    print("number is greater")
elif num==5:
    print("number is speciall")
else:
    print("number is smaller")

# nested if means if inside if

budget=int(input("enter  your budget\n"))
if budget==2000:
    print("cant buy phone")
elif budget==1800:
    print("let me think")
elif budget==1200:
    print("easy to buy")
elif budget==800:
    print("buy the phone")
elif budget==500:
    print("buy watch")
elif budget==200:
    print("buy handfree")
elif budget==100:
    print("buy fruits")
else:
    print("buy  nothing")

