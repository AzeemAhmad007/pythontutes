# # day50 also include  here
#
# # syntax to open file
#
# # Syntax=(file name , mod)
#
# """"
# r= read mode used to open file  for reading
# w= write mode used to open file  for writing but the old  content  will  be lost
# x= xclusive mode is  used to create file if not exist
# a= append mode is used to  add content in file
# t= text mode is used to open file as a text rt also a defualt mode
# b = binary mode is used to open file as a  binary
# += read plus write both
# """
#
#
# # reading file
#
# f = open('myfile', 'r') #  r is defualt mode if we dont use thats totally fine
# #print(f)
# text=f.read()
# print(text)
# f.close() # always  use this
#
#
# # writing file
#
# f=open("myfile", "w")
# f.write("i am a good boy") # old content will be remove
# f.close()
#
#
# # appending in the file
#
# f=open("day49part","a")
# f.write("i am doing job in callcenter\n")
# f.close() # jitni baar run karien gein utni baar content add ho jai ga
#
#
# # with keyword
#
# with open("day49part", "a") as f:
#     f.write("hey i am inside with\n")
#
# # Readline and readlines
#
#
# # f=open("sample file", "r")
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # f.close()
# f=open("sample file" ,"r")
# print(f.readlines())
# f.close() # it will return a list



# # practice  i made new file name day49.txt

#
f=open("day49.txt", "r") #"r" is default
#print(f)
text=f.read(5)
print(text)
for line in text:
    print(line) # it showing character by character
f.close()
f=open("day49.txt","r")
text=f.read()
f.close()
for line in text:
    print(line) # it showing character by character
f=open("day49.txt", "r")
for line in f:
    print(line, end= "") # it will work and also here is  a new line character by defualt
f.close()
# f=open("day49.txt","w")
# f.write("\nthis is thomas") # old content will be remove
# f.close()
#
#
# f=open("day49.txt","a")
# f.write("\ni am doing job in callcenter")
# f.close()


# # alternative method to write file without closing
# with open("day49.txt","a") as f:
#     f.write("\n my age is 20 years")

f=open('day49.txt', "r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f=open("day49.txt", "r")
print(f.readlines()) # it will return a list
f.close()


