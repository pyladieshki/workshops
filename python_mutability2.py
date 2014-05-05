def receive_mutable(mutable):
    print "inside of function object id:", id(mutable)
    mutable += [4] 
    print "inside of function object id after modification:", id(mutable)

l = [1, 2, 3]
print "original list:", l
print "original object id:", id(l)
receive_mutable(l)
print "list after function call:", l


def receive_immutable(immutable):
    print "inside of function object id:", id(immutable)
    immutable += " & dog"
    print "object after concatenation:", immutable
    print "object id after concatenation:", id(immutable)

str1 = "cat"
print "original string:", str1
print "original object id:", id(str1)
receive_immutable(str1)
print "string after passing it to the function:", str1

# objects are passed as a reference in Python
