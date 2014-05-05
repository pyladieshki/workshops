def receive_mutable(mutable):
    mutable += [4] 
    print "inside of function the id:", id(mutable)

l = [1, 2, 3]
print l
print id(l)
receive_mutable(l)
print l


def receive_immutable(immutable):
    immutable += " & dog"
    print "inside of function:", immutable
    print "inside of function the id:", id(immutable)

str1 = "cat"
print str1
print id(str1)
receive_immutable(str1)
print str1

# ---> immutable objects are passed as copies to functions
# ---> mutable objects are passed as references to functions

