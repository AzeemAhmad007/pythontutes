# os module :: is builtin and used to intrect with operatingsystem like
#creating files, folders opening files,removing files,changing paths

import os
#os.mkdir("os module") #  we already make file thats why its throughing error

# os.mkdir is used to  create directory

#If the directory already exists, FileExistsError is raised
# if (not os.path.exists("this is lec 26 file")):
#     os.mkdir("this is lec 26 file")
# if (not os.path.exists("os module")) :
#     os.mkdir("os module")
# # for i in range(1,10):
# #     os.mkdir(f"os module/day {i}")
# for i in range(1,3):
#     os.mkdir(f"this is lec 26 file/lec46mkdir files {i}")

print(os.getcwd())  # C:\Users\Azeem Ahmad\PycharmProjects\pythonProject2


# rename  and list functions also part of this lec  [os.list ,os.rename]


# remove directry

# os.mkdir("harry")
# if not os.path.exists("harry"):
#     os.mkdir("harry")
#
# for i  in range (1,6):
#     os.makedirs(f"harry/game{i}")


#os.rmdir("harry") # so it will delete the directory if empty
#
# if not os.path.exists("harry"):
#     os.remove("harry")

#print(os.listdir("D://")) # we can check any drive and get all folders in  the form of list
#
# print(os.listdir("C://"))
# print(os.listdir("D://"))
# print(os.listdir("E://"))

# all imp functions of os module

"""os.getcwd(): Returns the current working directory.
os.chdir(path): Changes the current working directory to the specified path.
os.listdir(path='.'): Returns a list of all files and directories in the specified directory.
os.mkdir(path): Creates a new directory.
os.makedirs(path): Creates a new directory and any necessary parent directories.
os.remove(path): Removes a file.
os.rmdir(path): Removes an empty directory.
os.rename(src, dst): Renames a file or directory from src to dst.
os.path.exists(path): Checks whether a path exists."""

#(os.rename("os modules" , "os module"))


#os.remove(f"harry/makedirs/removedirectory.py")
#os.makedirs("harry/makedirs")

#os.mkdir("python")
#os.rmdir("python")
print(not os.path.exists("harry"))