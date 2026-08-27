# Variable and Memory References
# In Python, a variable is actually a name that refers to an object.
# Call by Object Reference
# Variable Assignment
a = 5 # a refers to the object 5 stored somewhere in memory
print(id(a))
print(hex(id(a)))
print(id(4))
# Aliasing
a = 5
b = a # Both names refer to the same object 5
print(id(a))
print(id(b)) # a & b reference the same memory address.
c = b  # a, b and c all refer to the same object
print(id(c)) 
del(a)
print(b)
print(c)
# removing reference, not actual value/name. original value remains intact.
a = 5
b = a
a = 6
print(a)
print(b)
# Initially, a and b both refer to 5.
# a = 6 makes 'a' refer to a different object.
# 'b' still refers to 5.

# Reference Counting
# Reference Counting tracks variables referencing a memory address.
a = 'safyttxyz'
b = a
c = b
print(id(a))
print(id(b))
print(id(c))
print(a)
print(b)
print(c)

import sys
print(sys.getrefcount(a))  # Usually shows one extra reference because
 # getrefcount() temporarily references the object.

a = "abcdef"
b = a
c = b
print(sys.getrefcount(a))

# Garbage collection is the process of automatically reclaiming memory
# from objects that are no longer reachable.

# Wierd Stuff
# Python's Wierd Behaviour/Oddities:
# 1. Ref Count Anomaly/Getrefcount Anomaly 
a = 2
b = a
c = b
print(sys.getrefcount(a))
# System vars often use 2.
# a = 2 ---> a points to 2's existing memory location, no new 2 created.
a = 63
b = a
c = b
print(sys.getrefcount(a))

a = 717
b = a
c = b
print(sys.getrefcount(a))

a = 717 # Creates/references an integer object and assigns it to 'a'
print(sys.getrefcount(a))
d = c # Aliasing: 'd' and 'c' refer to the same object
print(sys.getrefcount(a))
a = 4
b = 4
print(id(a))
print(id(b))
a = 256
b = 256
print(id(a))
print(id(b))
a = 257
b = 257
print(id(a))
print(id(b))
a = -5
b = -5
# -5 is usually within Python's small-integer cache.
# Therefore, a and b usually refer to the same object.
print(id(a))
print(id(b))
a = -6
b = -6
# -6 is outside the commonly cached range,
# so the same id is not guaranteed.
print(id(a))
print(id(b))