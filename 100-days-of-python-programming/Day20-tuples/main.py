# Tuples in Python
# 1. Create
# Empty
T1 = ()
print(T1)
# Homogeneous
T2 = (1, 2, 3, 4, 5)
print(T2)
# Heterogeneous
T3 = ("Hello", 4, 5, 6)
print(T3)
# Like list tuples also allow 1D, 2D, 3D tuples
T4 = (1, 2, 3, (4, 5))
print(T4)
# A single-element tuple requires a comma
T5 = (1)
print(type(T5)) # int
T6 = ("Hello")
print(type(T6)) # str
T5 = ("Azka",)
print(type(T5)) # tuple

# Type Conversion 
T6 = tuple("Azka")
print(T6)

T6 = tuple([1, 2, 3, 4])
print(T6)

# 2. Access
print(T2)
print(T2[0])
print(T2[-1])
print(T2[:4])
print(T4)
print(T4[-1][0])

# 3. Edit
L = [1, 2, 3, 4, 5]
L[0] = 100
print(L)
T = (1, 2, 3, 4, 5)
# T[0] = 100  # TypeError because tuples are immutable
# del T2[-1]  # TypeError because tuples are immutable

# 4. Add

# not possible
# Tuples: immutable

# 5. Delete
T1 = (1, 2)
del T1
# print(T1) # NameError because T1 no longer exists
# del T2[-1] # TypeError because tuples are immutable

# 6. Operations
T2 = (1, 2, 3, 4, 5)
T3 = ('Hello', 4, 5, 6)
# 1. Arithmetic 
T = T2 + T3
print(T)
T = T2 * 3
print(T)
# 2. iteration
for i in T2:
    print(i)
# 3. membership
print(1 in T2)
print(10 not in T3)

# 7. Functions
print(len(T2))
print(min(T2))
print(max(T2))
print(sum(T2))
print(sorted(T2))
print(sorted(T2, reverse = True))
print(T2.count(4))
print(T2.index(3))

# Differences between List and Tuple
# Lists: Mutable (can be changed)
# Tuples: Immutable (cannot be changed)
# 1. Tuples can be slightly faster than lists for some operations
import time
L = list(range(1000))
T = tuple(range(1000))
# List timing
start = time.time()
for i in L:
    i * 5
print("List time ",time.time()-start)
# Tuple timing
start = time.time()
for i in T:
    i * 5
print("Tuple time ",time.time()-start)

# 2. Tuples take less storage than lists (space efficient)
import sys
L = list(range(1000))
T = tuple(range(1000))
print("List size ",sys.getsizeof(L))
print("Tuple size ",sys.getsizeof(T))

# Adding an element to List vs Tuple
# List
a = [1 ,2 ,3]
b = a
a.append(4)
print(a)
print(b)

# Tuple
a = (1 ,2 ,3)
b = a
a = a + (4,)
print(a)
print(b)

# Special Syntax
# tuple unpacking
a, b, c = (1, 2, 3)
print(a, b, c)
# a, b = (1, 2, 3)
# print(a, b) ValueError 

a = 1
b = 2
a, b = b, a
print(a, b)

# *others collects the remaining values into a list
a, b, *others = (1, 2, 3, 4)
print(a, b)
print(others)

# zip() with tuples
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
print(tuple(zip(a, b)))