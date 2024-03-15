# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time
timestamp = time.strftime('%H:%M:%S')
#print("Current time is ",timestamp)
name=input("enter your name\n")
hours=int(time.strftime("%H"))
if hours >= 0 and hours <= 12:
    print("good morning ",name,"sir")
elif hours >12 and hours <=16:
    print("good afternoon",name,"sir")
    if hours > 16 and hours <=19:
        print("good evening",name,"sir")
else:
    print("good night",name,"sir")
