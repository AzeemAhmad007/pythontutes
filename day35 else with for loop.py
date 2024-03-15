# else with for loop

# for i in range(5):
#     print(i)
# else:
#     print("out of the loop")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("out of the loop")

# when loop completely break  else part not execute


j=0
while j<8:
    print(j+1)
    j=j+1
    if j==5:
        break
else:
    print("else part")