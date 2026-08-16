# Python Modules
help('modules')

# keyword Module
import keyword
print(keyword.kwlist) # Reserved keywords in Python

# math module
import math
print(math.pi) # value of pi
print(math.e) # value of e
print(math.factorial(4)) 
print(math.ceil(5.9))
print(math.floor(5.9))

# random Module
import random
print(random.randint(1,10)) # random integer b/w 1 & 10

a = [1, 2, 3, 4, 5]
random.shuffle(a) # shuffles the items in the list
print(a)

# time Module
import time
print(time.time()) # Current time (seconds)
print(time.ctime()) # Current time (string)

print("Hello")
time.sleep(1) # Delay for 1 second
print("World")

# datetime Module
import datetime
print(datetime.datetime.now()) # Current date/time

# os Module
import os
print(os.getcwd())    # Current working directory
print(os.listdir())   # Files/folders in current directory