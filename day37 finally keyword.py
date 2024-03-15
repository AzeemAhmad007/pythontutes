# # finnaly keyword:
#
# # this is also the part  of  the  try  except exception.
# #The finally block is always executed
#
#
# #============================ most imp intreview question why we use finnally==================
#
#
# # because  inside the function after returning the value it  always execute
# # but in simple print statement in function  that will not execute after returning the value
#
# #
# #
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Error: Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: Division by zero!")
#
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Error: Please enter a valid number.")
# else:
#     print("Number entered:", num)
#
#
# num1=int(input("enter first number :"))
# num2=int(input("enter second number :"))
# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print("division by zero")
# try:
#     num = int(input("enter a number"))
#     print("you enter number",num)
# except ValueError:
#     print("please enter a valid number")
#
# list=[5,6,7,8,9,10]
# try:
#     num=int(input("enter the number : "))
#     print(list[num]) # give the index if exist in list otherwise print out of range
# except IndexError as e :
#     print(e)
#
# # after returning the value finnally still executing
# def func():
#     try:
#         num=int(input("enter the number : "))
#         list=[1,2,3,4,5]
#         print(list[num])
#         return  1
#     except:
#         print("some error occur")
#         return 0
#     finally:
#         print("but i will always execute")
# x=func()
# print(x)
#
# # without finnaly
#
# def func():
#     try:
#         num=int(input("enter the number : "))
#         list=[1,2,3,4,5]
#         print(list[num])
#         return  1
#     except:
#         print("some error occur")
#         return 0
#     print("my name is azeem") # is not  printing because we return the value
# x=func()
# print(x)

def func2():
    try:
        number=int(input("enter a number : \n"))
        list=[1,2,3,4,5,6,7]
        if number  in list:
            print("yes  number is in list ")
            return  1
        else:
            print("number is not in list")
            return 0
    finally:
        print("i am always executed")

x=func2()
print(x)