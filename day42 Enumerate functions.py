# #  enumerate functions  builtin in python
# # allows you loops  over the sequence of (tuple,string,dic,list)
# # used to get the index and the value of the  of the sequence
#
#
# # syntax
#
# # for index, i in enumerate(range):
# #     print(index,i)
#
#
# list_of_marks=[2,55,66,77,88,99,100,23,22,45,70,65,89]
# for index,marks in enumerate(list_of_marks):
#     print(index,":" ,marks)
#
#
# print("with list\n")
#
# name="AzeemAhmad"
# for index,characters in enumerate(name):
#     print(index , characters)
#
# tuple=("car","bike","bicycle","train","plane","ship")
# for index, vehicals in enumerate(tuple):
#     print(index, ":",vehicals)
#     if index==3:
#         print("something special")
#
# list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
# for index, numbers in enumerate(list_of_numbers,start=0):
#     print(index , numbers)
#     if index== 5:
#         print(" this number is special")
#
#


numbers=[1,2,3,4,5]
for index,number in enumerate(numbers):
    print(index ,":" ,number)

cars={1,2,43,4}
for index,number in enumerate(cars):
    print(index, ":", number)

tuple=(1,2,4,5,6,7)

for index,number in enumerate(tuple):
    print("index :",index , "value :",number)