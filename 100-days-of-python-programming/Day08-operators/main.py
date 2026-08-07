# Arithmetic Operators
x = 5
y = 2
print(x + y) # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # True Division(returns float)
print(x % y) # Modulo
print(x ** y) # Exponent(x raised to the power y)
print(x // y) # Floor Division

# Comparison Operators
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

# Logical Operators
x = True
y = False
print(x or y)
print(x and y)
print(not x)
print(not y)

# Bitwise Operators
x = 2
y = 3
print(x & y) # AND
print(x | y) # OR
print(2 ^ 3) # XOR
print(x >> 2) # Right Shift
print(y << 3) # Left Shift
print(~x) # NOT

# Assignment Operators
a = 3
print(a)
a += 3 # a = a + 3
print(a)
a -= 3 # a = a - 3
print(a)
a *= 3 # a = a * 3
print(a)
a /= 3 # a = a / 3
print(a)
# Python doesn't allow a++ or ++a format
# You can either use a = a + 1 or a += 1

# Identity Operators
# is and is not (return bool)
# Checks if two variables refer to the same object
a = 3
b = 3
print(a is b) 
a = "Hello"
b = "Hello"
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  → same values
print(a is b) # False → different objects

a = "Hello-World"
b = "Hello-World"
print(a is b)
print(a is not b)

# Membership Operators
# in and not in (return bool)
# Checks if certain thing is present in a collection
x = "Lahore"
print("L" in x)
print("L" not in x)

# List
x = [1, 2, 3]
print(1 in x)
print(5 in x)

# Tuple
x = (1, 2, 3)
print(1 in x)
print(5 in x)

# Set
x = {1, 2, 3}
print(1 in x)
print(5 in x)