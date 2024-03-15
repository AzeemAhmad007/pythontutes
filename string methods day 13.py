# strings are immutable
#when we do operations on string it return new string exicting string will be remains same.

#upper method is used to convert  the whole string in upper case.

str1="my name is azeem"
print(str1.upper())

# lower method convert the whole string in lower case.
str2="AZEEM IS GOOD BOY"
print(str2.lower())

# strip method is used to  remove  whitespaces before and after string
str1="  my name is azeem   "
print(str1.strip())

#rstrip method is used to remove only trailing ending characters.
str="this is me&&&&"
print(str.rstrip("&"))

str="&&&&this is me&&&&"
print(str.rstrip("&"))  # &&&&this is me

# replace method is used to  replace all occurances  of the string to anthor  one.
n="this is danial.this  pakage is deliverd to danial"
print(n.replace("danial","azeem"))

# split method is used to split string but  whitespaces is necessary and  gives  list.
str1="my name is azeem"
print(str1.split(" "))

#capitalize is used to convert first character in upper case and others in lower case.
str1="my name is azeem"
print(str1.capitalize())
str2="AZEEM IS GOOD BOY"
print(str2.capitalize()) # rest of first character will be in lower case

#count method return  number of times the given value occure  in string.
n="this is danial.this  pakage is deliverd to danial"
print(n.count("danial"))
print(n.count("Danial")) #0

#endswith give true if string ends with the given value. result in boolean.
str1="my name is azeem"
print(str1.endswith("azeem"))
print(str1.endswith("is"))

#find method research for the first occurence of the given value and returns
#the index where it is located.if given  value absent it return ""-1"".

n="this is danial.this  pakage is deliverd to danial"
print(n.find("danial"))
print(n.find("azeem"))

#index method research for the first occurence of the given value and returns
#the index where it is located.if given  value absent it return "error".

n="this is danial.this  pakage is deliverd to danial"
#print(n.index("azeem"))

# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
new="Python is high level language"
print(new.isalnum()) # due to spaces  it showing false
new="Pythonishighlevel###language@@@@"
print(new.isalnum())
print("without spaces")
new="Pythonishighlevellanguage"
print(new.isalnum())

#  isalpha  method returns True only if the entire string only consists of A-Z, a-z only

str1="my name is azeem"
print(str1.isalpha())   #due to white spaces
str1="mynameisazeem"
print(str1.isalpha())
str13="m##my name is $$azeem"
print(str13.isalpha())

# The islower() method returns True if all the characters in the string are lower case,
# else it returns False.
print(str1.islower()) # true
str1="My name is azeem"
print(str1.islower())

#The isprintable() method returns True if all the values within the given string are printable,
# if not, then return False.

k="This is important"
j="This is important\n"
print(k.isprintable())
print(j.isprintable()) #\n is not printable

# The isspace() method returns True only and only if the string contains white spaces,
# else returns False.
str1="My name is azeem"
print(str1.isspace())  #false
whitepaces="       "
print(whitepaces.isspace()) # only true when only and only spaces.

# The istitile() returns True only if the first letter of each word of the string is capitalized,
# else it returns False.

str1="My name is azeem"
print(str1.istitle()) #false
str3="My Name Is Azeem"
print(str3.istitle()) # true

# The isupper() method returns True if all the characters in the string are upper case,
# else it returns False.

str1="My name is azeem"
print(str1.isupper()) #false

str2="AZEEM IS GOOD BOY"
print(str2.isupper()) # true

# The startwith() method checks if the string starts with a given value.
# If yes then return True, else return False.

str2="AZEEM IS GOOD BOY"
print(str2.startswith("AZEEM")) # true

#swapecase convert the whole string  in upper to lower and lower to upper case.

str2="AZEEM IS GOOD BOY"
print(str2.swapcase())
str1="my name is azeem"
print(str1.swapcase())

# title case capitalize the first character of each word in the string.

str1="my name is azeem"
print(str1.title())

