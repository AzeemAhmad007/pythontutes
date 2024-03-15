# fstring The f-string offers a convenient way to
# embed Python expression inside string literals for formatting.# we can add veriable in string
name="azeem"
country="pakistan"
print(f"my name is {name} and i am from {country}")

print(type(f"{2 * 30})"))

# now if we need fsrting as it is not  replace veriable fstring will be retain as it is


name="azeem"
age="20"
print(f"my name is {name} and i am {age} year old")
print(f"my name is {{name}} and i am {{age}} year old")
