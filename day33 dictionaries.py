# dictionaries are keyvalue pairs.seprate by comma enclosed with {}.
# dictionaries are ordered collection of data items
dic={"car":"Vehical","python":"language","usa":"country"}
print(dic["python"])
# print(dic["python2"])   # through error
print(dic.get("python2"))  # returns none
print(dic.keys())  # return all the keys
print(dic.values()) # return all the values

for value in dic.values():
    print(value)
print(dic.items())   # it will return keyvalue pairs+