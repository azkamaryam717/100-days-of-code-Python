# Functions in Python
# Check if number is even/odd
def is_even(number):
    """
    This function tells if a given number is odd or even
    Input - any valid integer
    Output - odd/even
    Created By - Azka
    Last edited - 29 Aug 2026
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

for i in range(1,11):
    print(is_even(i))
print(is_even.__doc__)
print(print.__doc__)
print(type.__doc__)

# Functions: 2 Perspectives 
# Creator's perspective and user perspective
import func_demo

even_or_odd = func_demo.is_even(34)
print(even_or_odd)
# func_demo.is_even("Hello") # func_demo.is_even("Hello") # TypeError because % 2 cannot be performed on a string

import func_demo2 as fd
even_or_odd = fd.is_even("Hello")
print(even_or_odd)

# Parameters vs Arguments
def power(a, b):
    return a**b
print(power(2,3))
# power(3) # invalid requires 2 arguments
# power() # invalid requires 2 arguments
# 1. Default arguments: parameters with predefined values.
def power(a = 1, b = 1):
    return(a**b)
print(power(2, 3))
print(power(2))
print(power())
# 2. Positional Arguments: Values assigned by call order.
print(power(3, 2))
# 3. Keyword Argument: Values assigned to args by name at call time.
# Keyword args will Overrides Positional args.
print(power(b = 2, a = 3))
# 4. Arbitrary Argument: Accepts any number of args.
# Useful when the number of arguments is unknown.
def flexi(*number):
    product = 1
    for i in number:
        product *= i
    print(product)
print(flexi(1))
print(flexi(1, 2))
print(flexi(1, 2, 3))
print(flexi(1, 2, 3, 4, 5, 6, 7, 8, 9))

def flexi(*number): # Flexible inputs ---> tuple
    product = 1
    print(number)
    print(type(number)) # *number collects arguments into a tuple
    for i in number:
        product *= i
    print(product)
print(flexi(1, 2, 3, 4, 5))

# *args and **kwargs
# *args
# Pass variable non-keyword args to function
# *args collects any number of positional arguments into a tuple.
def multiply(*args):
  product = 1
  for i in args:
    product *= i
  print(args)
  return product
print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12))

# **kwargs
# Pass any no. of keyword args (key-value pairs)
# **kwargs collects any number of keyword arguments into a dictionary.
# Acts like a dict.
# kwargs is just a conventional name. Python doesn't require that exact name.
def display(**Azka): # You can also use kwargs in place of Azka
  for (key, value) in Azka.items():
    print(key, '->', value)

print(display(srilanka='colombo', nepal='kathmandu', pakistan='islamabad'))

# Global Var and Local Var
# Variable scope & function behavior
# Example 1
def f(y):
    x = 1 # Local x
    x += 1
    print(x)
x = 5  # Global x
print(f(x))  # Calls f(x)
print(x)
# Functions have local scope. Global vars coexist but are not affected.

# Example 2
def g(y):
    print(x)  # x (global) used in g()
    print(x + 1) # x (global) remains 5; new int (6) created, x unchanged
x = 5
print(g(x))
print(x)   # x = 5 remains unchanged

# Example 3
# def h(y):
#     x += 1 # Error: needs "global x" to modify x
# x = 5
# print(h(x))
# print(x) 

# Rules: Global vars: accessed but not modified in functions unless you use global keyword.
# Concept 1: Globals exist outside funcs, accessed by any func.
# Concept 2: Funcs without local vars can use globals.
# Concept 3: Locals access globals but can't modify.

# Example 4
# EXPLICITLY Modifying Global Variables Locally
def h(y):
    global x # Note: Python allows Modifying global vars but is discouraged
    x += 1
x = 5
print(h(x))
print(x)

# Example 5
# Complicated Scope
def f(x):
    x += 1
    print("in f(x): x = ",x)
    return x
x = 3
z = f(x)
print("in main program scope: z = ",z)
print("in main program scope x = ",x)

# Functions as Arguments
def func_a():
    print("inside func_a: ")
    # A function with no return statement automatically returns None.
def func_b(y):
    print("inside func_b: ")
    return y
def func_c(z):
    print("inside func_c: ")
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))

# Nested Functions
def f():
    print("Inside f")
    def g():
        print("Inside g")
    g()
print(f())

# g() # NameError because # g() # NameError because g() is defined inside f() and is local to f()
# Nested Function stays Abstracted/Hidden from main program

# def f():
#     print("Inside f")
#     def g():
#         print("Inside g")
#         f()
#     g()                    # Infinite recursion ---> Code will Crash ---> Kernel Dead
# print(f())

# Harder Scope
def g(x):
    def h():
        x = "abc"
    x += 1
    print("in g(x): x =", x)
    h()
    return x
x = 3
z = g(x)
print(z)

# Complicated Scope
def g(x):
    def h(x):
        x += 1
        print("in h(x): x =", x)
    x += 1
    print("in g(x): x =", x)
    h(x)
    return x
x = 3
z = g(x)
print("in main proram scope: x =", x)
print("in main program scope: z =", z)


# Everything in Python an Object
# Functions too

# Functions as Objects
def f(num):
    return num ** 2
print(f(2))
print(f(4))

x = f # aliasing
# since functions are objects just like int, str,
print(x(2))
print(x(4))
del f # Del functions in Python
# f(2) # NameError because function f() no longer exist

print(x(3)) # # x refers to the same function object previously named f (Call by Object Reference)
print(type(x))
L = [1, 2, 3, 4]
print(L)
L = [1, 2, 3, 4, x]
print(L)
L[-1](3) # L[-1] is x and (3) is value passed to it for sqr
L = [1, 2, 3, 4, x(5)]
print(L)

# In Python, Functions behave like any other Data type.
# Can be assigned, passed, and returned.

# Functions are objects, so they can be:
# 1. Renamed/reassigned: new_name = old_name
# 2. Deleted: del func_name
# 3. Stored in a variable: func_var = func_name
# 4. Passed as an argument: outer(func_name)
# 5. Returned from another function: return func_name

# Function as argument/input
def func_a():
    print("inside func_a")
def func_c(z):
    print("inside func_c")
    return z()
print(func_c(func_a))

# Returning a Function + Nested Calling
def f():
    def x(a, b):
        return a + b
    return x
val = f()(3, 4) # f() returns the function x, then (3, 4) calls that returned function.
print(val)

# Functions are First-Class Citizens in Python.
# type & id
def square(num):
    return num ** 2
print(type(square))
print(id(square))

# reassign
x = square
print(id(x))
print(x(3))

# Deleting Function
del square
# square(3) # NameError

# Sorting
L = [1, 2, 3, 4, x]
print(L[-1](3))

s ={x} # A function object can be stored in a set
print(s)