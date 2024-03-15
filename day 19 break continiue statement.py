#  Break and continue

# Break statement :breaking out(exit) of the loop
for i in range(1,11):
    print("5 X",i, "=",5*i)
    if i==5:
        break
   # the loop will be exit

for i in range(1,10):
    print(i)
    if(i==8):
        break
print("Thank you")

# continue : skip the perticular itreation
for i in range(1,6):
    if i==3:
        continue
    print(i)
