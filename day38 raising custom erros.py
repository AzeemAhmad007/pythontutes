# we can raise custom erros using custom errors
# to stop the program if we dont want any un aspected thing

#  raise keyword is used to raise an error
#
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
#

a = (input("Enter any value between 5 and 9 : "))

if a.lower() == "quit":
    print("no error found")
elif int(a)<5 or  int(a)>9:
    raise SyntaxError("enter a valid integer")

