#
# # try exeption is  used to avoid  the program from error so  the program will not terminate.
# # if  error will be in the  mid of the program the  remaining  prorgram will not  run it will be
# #haled so  avoid this we  use  try exeption
#
#
# #  Get  Multiplication  of any table
#
# # number=int(input("Enter the  number: "))
# # print(f"The multiplication table of {number} is:")
# # for i in range(1,11):
# #     print(f"{number} X {i} = {number*i}")
#
#
# try:
#     for i in range(1,11):
#         print(f"{int(number)} X {i} = {int(number)*i}")
# except Exception as e:
#     print(e)
#
#
#
# try:
#     num = int(input("Enter an integer: "))
# except Exception as e:
#     print(e)
#
#
# l=[1,2,0,"string",5,4.6]
# try:
#     print(10/0)
# except Exception as e:
#     print(e)
# try:
#     print(2/l)
# except Exception as e:
#     print(e)
try:
    age = int(input("Enter your age: "))
    if age < 0 or age > 120:
        raise ValueError("Invalid age")
except ValueError as e:
    print(e)

