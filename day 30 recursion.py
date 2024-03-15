# # recursion is  a method to call function inside himself.
#
# # factorial(7) = 7*6*5*4*3*2*1
# # factorial(6) = 6*5*4*3*2*1
# # factorial(5) = 5*4*3*2*1
# # factorial(4) = 4*3*2*1
# # factorial(0) = 1
#
# # formula= n(n-1)
# #
# def facturial(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return (n) *facturial(n-1)
# print(facturial(4))
# print(facturial(3))
# print(facturial(2))
# print(facturial(1))
# print(facturial(0))
#
# # quick quize
# # fibonacci series
# # f(0) = 0
# # f(1) = 1
# # f(2) = f(1) + f(0)
# # f(n) = f(n-1) + f(n-2)
#
# def fibonacci(n):
#     if n ==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))






def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))