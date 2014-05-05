#On mutability of Python objects

# Built-in data types:
# - numbers
# - strings
# - lists
# - dictionaries
# - sets
# - tuples
# - files
# - others (e.g., None)


# Numbers are immutable
num = 2
#print id(num)
num = 3
#print id(num) #id function shows identity of an object
# We say that object1 and object2 are the same if id(object1) == id(object2)

# Strings are immutable too
str1 = "Hello"
#print id(str1)
str2 = "Hey"
#print id(str2)
str2 = "Hi"
#str2[0] = "M" # -> error
#print id(str2)
str2 = "Hello"
#print id(str2)

# Lists, however, are mutable
l = [1, 2, 3] # a list
print l
print id(l)
l[0] = l[0] * 2
print l 
print id(l)

# Dictionaries are mutable too
d = {"name": "Ada", "lastname": "Lovelace"}
print d
print id(d)
d["name"] = "Grace"
d["lastname"] = "Hopper"
print d
print id(d)

# Tuples are immutable
t = (1, 2, 3)
print t
print id(t)
t = t + (2, 3)
print t
print id(t)

