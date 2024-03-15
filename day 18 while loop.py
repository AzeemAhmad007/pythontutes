# while loop  while loops execute statements while the condition is True.
i=10
while i>0:
    print(i)
    i=i-1  #decrement loop
    # when ever we use ">"  we decrement the loop


print("increment while loop")
j=0
while j<5:
    print(j)
    j=j+1
    # when ever we use "<"  we increment the loop


# taking input from user
K=int(input("Enter the number\n"))
while K<=35:
    K = int(input("Enter the number\n"))
    print(K)
    break
print("done with the loop")

# infinite while loop

# i=10
# while i>0:
#     print(i)
#     i=i+1  # due to "+"

# else with while loop


j=0
while j<=5:
    print(j)
    j=j+1
else:
    print("i am inside else")