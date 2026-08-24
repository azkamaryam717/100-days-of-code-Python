# Sets in Python
# 1. Create
# empty
s1 = {}
print(s1)
print(type(s1)) # dict
s1 = set()
print(type(s1)) # set
# 1D & 2D Sets
# Regular sets cannot contain other sets; frozenset can be used for nested sets
s1 = {1, 2, 3, 4, 5} # 1D Set
print(s1)
# s2 = {1, 2, 3, {4, 5}} # 2D Set not allowed
# print(s2)
# homo and hetro
s2 = {"Hello", 1, 4.5, True}
print(s2)
# Type Conversion
s4 = set([1, 2, 3])
print(s4)
# duplicates are not allowed
s3 = {1, 1, 1, 2, 2, 3}
print(s3)

#s4 = {[1, 2, 3], 4, 5, "Hello"}
# print(s4) #TypeError because Sets cannot contain unhashable objects such as lists and sets
# because set can't have mutable items
# s6 = {1, 2, [3, 4]}
# print(s6)

# Sets have no indexing
# Sets have Hashing
# s5 = {{1}, {2}}
# print(s5) # TypeError: unhashable type: 'set'

s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2)

# 2. Access
s1 = {1, 2, 3, 4, 5}
# print(s1[0])
# print(s1[-1])
# print(s1[0:3]) 
# All will give TypeError because sets do not allow indexing or slicing

# 3. Edit
s1 = {1, 2, 3, 4, 5}
# s1[2] = 100 # TypeError: 'set' object does not support item assignment
print(id(s1))
L = list(s1)
print(L)
L[2] = 100
print(L) # allowed index 2 will be 100 now
s1 = set(L) # convert again to set
print(s1)
print(id(s1))
# Note that both ids are diff as edit directly is not allowed
# We copied set elements to the list and then creted a new set to cpoy those elements again
# 4. Add
s1 = {1, 2, 100, 5, 4}
s1.add(6)
print(s1)
print(id(s1))
s1.add(7)
print(s1)
print(id(s1))
s1.update([5, 6, 7])
print(s1)

# 5. Delete
print(s2)
del s2
# print(s2) # NameError as s2 no longer exist
# del s1[0] # TypeError because sets don't support indexing
s1.remove(100)
print(s1)
s1.pop()
print(s1)
s1.discard(7)
print(s1)
s1.clear()
print(s1)

# 6. Operations
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
# Arithmetic operations are not allowed
# s1 + s2 # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# S1 * 3 # TypeError: unsupported operand type(s) for *: 'set' and 'int'

# Iteration 
for i in s1:
    print(i)

# Membership
print(1 in s1)
print(2 not in s1)

# Union (|)
print(s1 | s2)

# Intersection (&)
print(s1 & s2)

# Difference
print(s1 - s2)

# Symmetric Difference
print(s1 ^ s2)

# 7. Functions
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sorted(s1, reverse=True))
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
# copy
s1 = {1, 2, 3}
s2 = s1.copy()
print(s1)
print(s2)

# 8. Frozen set
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
print(fs1 | fs2)
# what works and what does not
# Works       ---> all read functions
# Doesn't Work ---> write operations

# When to use
# 2D sets
# Regular sets cannot directly contain other sets because sets are unhashable
# frozenset can be used when a set-like object needs to be nested
fs = frozenset([1, 2, frozenset([3, 4])])
print(fs)

# 9. Set Comprehension
# 1. Squares with a condition
s1 = {i ** 2 for i in range(1, 11) if i>5}
print(s1)
# 2. Even numbers
s3 = {i for i in range(1, 21) if i % 2 == 0}
print(s3)

# 3. Odd numbers
s4 = {i for i in range(1, 21) if i % 2 != 0}
print(s4)

# 4. demonstration of set keeping unique chars from string with duplicate elements 
s = "programming"
result = {char for char in s}
print(result)

# 5. Convert strings to uppercase
words = ["hello", "python", "world", "code"]
s7 = {word.upper() for word in words}
print(s7)

# 6. Words starting with 'p'
languages = ["python", "java", "php", "c", "javascript"]
s8 = {language for language in languages if language.startswith("p")}
print(s8)

# 7. Lengths of words
words = ["apple", "banana", "cat", "dog"]
s9 = {len(word) for word in words}
print(s9)