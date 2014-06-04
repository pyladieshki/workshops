# Have you ever wondered what these things mean:
# @classmethod
# @staticmethod?

# They are also decorators, but we won't cover that here.

import datetime

class Example:

    @staticmethod
    def timeofday():
        print datetime.datetime.now()

# A staticmethod is a method of the class that "doesn't know" about the class,
# it does not get the class as an implicit first argument. Actually, this means that
# you can do this:

Example.timeofday()

# when usually you'd have to do ex = Example(), ex.timeofday()
# You can call a staticmethod both on the class (Example.timeofday() )
# or on an instance (ex.timeofday())

# You don't need an instance of the class to use a static method.
# Why not just use a normal function instead of a staticmethod? Well, the
# function might logically belong to a class, but not need access to its
# internals. For example, a method where the return result is always the
# same regardless of the state of a class instance, could be a staticmethod.

# A classmethod on the other hand gets the class as a first argument.
# It can be called on the class or on an instance.
# For example, classmethods can be used for defining custom constructors.
# Here is an example:

class C:

    number = 0
    
    def __init__(self,arg1):
        self.number = arg1    
    
    @classmethod
    def constructor_that_sums(cls, arg1, arg2): #cls is the class
        obj = cls(arg1 + arg2) #create a new instance of cls
        return obj

one_number = C(1)
another_number = C.constructor_that_sums(1,2) # Call method on the class

print one_number.number
print another_number.number
