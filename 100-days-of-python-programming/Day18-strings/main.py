# strings in Python
# 1. Create
# single quotes
a = 'Hello'
print(a)

# double quotes
a = "Hello"
print(a)

# triple quotes(multiline string)
a = '''Hello,
I am Azka'''
print(a)

# use of single and double quotes together
# a= 'It's raining outside'(Syntax error)
a = "It's raining outside" 
print(a)

a = str("Hello") # str does nothing useful here as Hello is already a string
print(a)

# 2. Accessing Substrings from a String
# Indexing
a = "Hello"
print(a[0]) # Positive Indexing
print(a[-1]) # Negative Indexing

# Slicing
a = "Hello World"
print(a[0:6]) # indices 0-5
print(a[3:]) # Starts from index 3 and goes to the end
print(a[:4]) # Assumes that you started slicing from 0-3
print(a[:]) # Assumes you want to print full string
print(a[2:6:2]) # Starts at index 2, stops before 6, step of 2
print(a[0:10:3]) # Starts at 0, stops before 10, step of 3
print(a[0:6:-1])  # Empty because the step is backwards but start < stop
print(a[-5:-1:2]) # Starts at -5, stops before -1, step of 2
print(a[::-1]) # prints starts to end but -1 makes it backwards
print(a[-1:-6:-1]) # -1 to -6 and prints backwards

# 3. Add (Concatenation)
str1 = "Hello"
str2 = "World"
new_str = str1 + " " + str2
print(new_str)

another_str = str1 + ", how are you?"
print(another_str)

# 4. Edit
a = "Hello"
# c[0] = "X" (TypeError because Strings are immutable in Python)

# 5. Deletion
name = "Azka"
del name
#print(name) # NameError

a = "Hello World"
# del a[0] (TypeError because deletion changes string structure but string are immutable)
# del a[:3:2] (TypeError)

# 6. Operations on Strings
# 1. Arithmetic Operations
# Addition(Concatenation)
a = "Hello" + " " + "World"
print(a)
# Multiplication
print("*"*50)
print("Hello"*5)

# 2. Relational
print("Hello" == "World")
print("Hello" != "World")
print("Lahore" > "Karachi") # Lexicographically
print("Lahore" < "Karachi")
print("lahore" < "Lahore")

# 3. Logical
print("Hello" and "World")
print("Hello" or "World")
# ""        ---> False (Empty string is automatically false)
# "Azka" ---> True
print("" and "World")
print("" or "World")
print(not "Hello")
print(not "")

# 4. Loops in strings
a = "Hello World"
for i in a:
    print(i)

for i in a[0:6]:
    print(i)

for i in a[1:11:2]:
    print(i)

for i in a[::-1]:
    print(i)

# 5. Membership
a = "Hello World"
print('H' in a)
print('h' in a)
print("World" in a)
print("World" not in a)

# 7. String Functions
# 1. Common Functions
a = "Azka"
print(len(a))
print(max(a))
print(min(a))
print(sorted(a))
print(sorted(a, reverse = True))

# 2. Capitalize/Title/Upper/Lower/Swapcase
a = "Azka"
print(a.capitalize()) 
print(a) # Original value of (a) remains same
print("it's raining outside".capitalize())
print("it's raining outside".title())
print(a.upper())
print(a.lower())
print(a.swapcase())

# 3. Count
a = "Hello World"
print(a.count("l"))
print(a.count("World"))
print(a.count("h"))

# 4. Find/Index
# find is safer to use as it returns -1 if the value is not present in the string.
# index() raises a ValueError if the value is not found
a = "Hello World"
print(a.find("o"))
print(a.find("ld"))
print(a.find("Hello"))
print(a.find("i"))
print(a.index("llo"))
# print(a.index("A")) # ValueError

# 5. endswith/startswith
c = "My name is Azka"
print(c.startswith("My"))
print(c.endswith("Azka"))
print(c.startswith("Mi"))

# 6. format
info = "Hi, my name is {} and I'm {}".format("Azka", 20)
print(info)
info = "Hi, my name is {1} and I'm {0}".format("Azka", 20)
print(info)
info = "Hi, my name is {name} and I'm {age}".format(name = "Azka",age = 20)
print(info)
info = "Hi, my name is {age} and I'm {name}".format(name = "Azka",age = 20)
print(info)
info = "Hi, my name is {name} and I'm {age}".format(name = "Azka", weight = 56, age = 20)
print(info) # weight argument is never used, Python allows you to write it 

# 7. isalnum/isalpha/isdecimal/isdigit/isidentifier
a = "Azka20".isalnum() # Alphanumeric 
print(a)
a = "Azka20@".isalnum()
print(a)
a = "Azka20".isalpha()
print(a)
print("35".isdecimal())
a = "35".isdigit()
print(a)
a = "Azka35".isdigit()
print(a)
a = "Hello World".isidentifier()
print(a)
a = "Hello_World".isidentifier()
print(a)

# 8. Split
a = "Who invented light Bulb".split()
print(a)
a = "Who invented light Bulb".split("light")
print(a)
a = "Who invented light Bulb".split("i")
print(a)
a = "Who invented light Bulb".split("z")
print(a)

# 9. Join
a = ['Who', 'invented', 'light', 'Bulb']
print(" ".join(a))
a = ['Who', 'invented', 'light', 'Bulb']
print("-".join(a))

# 10. Replace
name = "Hi my name is Azka"
print(name.replace("Hi", "Hello"))

# 11. Strip
name = "                  Azka     "
print("Hi" + name)
print("Hi" + name.strip())