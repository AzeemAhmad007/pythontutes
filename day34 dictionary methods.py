 # update

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# clear

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

#info.clear()
print(info) # show empty  dict


# pop

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#
# popitem():
# The popitem() method removes the last key-value pair from the dictionary.



info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)



# del

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)   # error because dict is dell