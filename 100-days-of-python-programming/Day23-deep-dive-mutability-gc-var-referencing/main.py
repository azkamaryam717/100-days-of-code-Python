# Variable and Memory References
# In Python, a variable is actually a name that refers to an object.
# Call by Object Reference
# Variable Assignment
a = 4 # 'a' is a name/reference that points to the integer object 4.
print(id(a))
print(hex(id(a)))
print(id(4))

# 1. Aliasing
a = 5
b = a # Both names refer to the same object 5
print(id(a))
print(id(b)) # a & b reference the same memory address.
c = b  # a, b and c all refer to the same object
print(id(c)) 
del(a)
print(b)
print(c)
# del(a) removes the name 'a', not the object itself.
# The object remains alive because 'b' and 'c' still reference it.
a = 5
b = a
a = 6
print(a)
print(b)
# Initially, a and b both refer to 5.
# a = 6 makes 'a' refer to a different object.
# 'b' still refers to 5.

# 2. Reference Counting
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
print(sys.getrefcount(a))  # getrefcount() temporarily creates an additional reference
# to the object while checking its reference count.

a = "abcdef"
b = a
c = b
print(sys.getrefcount(a))

# 3. Garbage collection is the process of automatically reclaiming memory
# from objects that are no longer reachable.

# 4. Wierd Stuff
# Python's Wierd Behaviour/Oddities:
# 1. Ref Count Anomaly/Getrefcount Anomaly 
a = 2
b = a
c = b
print(sys.getrefcount(a))
# Reference counts can be affected by other references created internally
# by Python, so exact values are implementation-dependent.
# a = 2 ---> a points to 2's existing memory location, no new 2 created.
a = 63
b = a
c = b
print(sys.getrefcount(a))

a = 717
b = a
c = b
print(sys.getrefcount(a))

a = 717 # 'a' is assigned to an integer object containing 717.'
print(sys.getrefcount(a))
d = c # Aliasing: 'd' and 'c' refer to the same object
print(sys.getrefcount(a))
# 2. Small integer caching
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

# 3. Variable IDs in Python
# CPython commonly caches small integers from -5 to 256.
# Therefore, variables assigned these values often share the same object.
# Integer identity outside this range is not guaranteed.
a = "Azka"
b = "Azka"
print(id(a))
print(id(b))
a = "I am Azka"
b = "I am Azka"
print(id(a))
print(id(b))
a = "I_am_Azka"
b = "I_am_Azka"
print(id(a))
print(id(b))
# Valid Identifiers yield Same IDs.
# Invalid Identifiers creates Different IDs.

# 5. Mutability
L = [1, 2, 3]
print(id(L))
print(id(1))
print(id(L[0]))
print(id(2))
print(id(3))
L[2] = 1
print(L)
print(id(L[2])) # same id as 1 at L[0]

a = "Hello"
print(id(a))
a = a + "World"
print(a)
print(id(a)) # diff from previous (a)
# Strings are immutable, so concatenation creates a new string object.
# 'a' is then updated to reference the new object.

T = (1, 2, 3)
print(id(T))
T = T + (5, 6)
print(T)
print(id(T))
L = [1, 2, 3]
print(id(L))
L.append(4)
print(L)
print(id(L))
# Immutable objects cannot be changed in place.
# Operations that appear to modify them usually create a new object.

# Mutable objects can be modified in place.
# Some operations modify the existing object, while others create a new object.

# 6. Side Effects of Mutation
# Aliasing can cause unexpected side effects when a mutable object is modified.
L = [1, 2, 3]
L1 = L
print(id(L))
print(id(L1))
L1.append(4)
print(id(L1))
print(L1)
print(L)

# Cloning
print(L)
L1 = L[:] # Slicing creates a shallow copy of the list.
print(id(L))
print(id(L1))
L1.append(5)
print(L1)
print(L)
# In cloning we create a copy of the list at a different memory address

a = (1, 2, 3, [4, 5])
print(a)
a[-1][-1] = 500
print(a)
# The tuple is immutable, but it contains a mutable list.
# We cannot replace an element of the tuple, but we can modify the list inside it.

a = [1, 2, 3, (4, 5)]
print(a)
# a(-1)(-1) = 500 # SyntaxError
a = [1, 2]
b = [3, 4]
c = (a, b)
print(c)
print(id(a))
print(id(b))
print(id(c))
c[0][0] = 100
print(c)
print(id(a))
print(id(c))
L = [1, 2, 3]
L = L + [4, 5]
print(L)
# append, edit, insert, extend modifies list in place (mutable); same memory address.
# Concatenation creates new list; different memory address.
print(c)
# c[0] = c[0] + [5, 6] # TypeError
print(c)
print(a)
a = a + [5, 6]
print(a)
print(c)

# == vs is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True: same values
print(a is b) # False: different list objects
c = a
print(a == c)  # True
print(a is c)  # True: same object