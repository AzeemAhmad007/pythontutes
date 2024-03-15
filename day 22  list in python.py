# list  is ordered collection of data. commas and enclosed within square brackets [].
#Lists are changeable  also used to store multiple items in a single variable.
listoflanguages=["c","jave","python","html","php"]
print(listoflanguages)
print(listoflanguages[0])
print(listoflanguages[1])
print(listoflanguages[2])
print(listoflanguages[3])
print(listoflanguages[4])

print(len(listoflanguages))

mixlist=[1,2,3,4,5,"a","b","c","d",True,False,77.00,12.23]
print(mixlist)


# Negative Indexing:
listoflanguages=["c","jave","python","html","php"]
print(listoflanguages[-2])
print(listoflanguages[len(listoflanguages)-2])
print(listoflanguages[5-2])

if "c" in listoflanguages:
    print('present')
else:
    print("absent")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes'
print(len(animals))

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes



animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes   skip 1 index
print(animals[-8:-1:2])	#using negative indexes .skip 1 index



animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3]) # skip 2  index

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists,
# tuples, dictionaries, sets, and even in arrays and strings.


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameslen = [item for item in names if (len(item) > 4)]
print(nameslen)