# for loops
name="Python"
for char in name:
    print(char)
    if char=="t":
        print("spectial digit")

list=["comments","constant","tags"]
for elements in list:
    print(elements)
    for char in elements:
        print(char)

colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)

# Range function

for i in range(5):
    print(i)  # 0 to 4
for i in range(5):
    print(i+1)  # 1 to 5
print("range function")
for i in range(1,5):
    print(i+1)  # 2 to 5

# nested for loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
