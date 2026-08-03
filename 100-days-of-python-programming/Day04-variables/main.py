# No prior declaration needed
# Assign a value directly. Python auto-creates the variable

name="Azka"
print(name)

name="Aira"  # Reassigning a new value
print(name)


# Python supports Dynamic Typing.
# A variable can store different data types during execution.
name=4 # int
print(name)

name=True # bool
print(name)

# Python uses Dynamic Binding
# A variable can be rebound to different objects during execution.
a=8   # Bound to an integer object.
print(a)

a="Azka" # Rebound to a string object.
print(a)


# Special Variable Assignment Syntax

a=5; b=6; c=7
print(a)
print(b)
print(c)

# Multiple assignment
a, b, c= 4,5,6
print(a)
print(b)
print(c)
# OR
print(a,b,c)

# Assign the same value to multiple variables
a=b=c=8
print(a,b,c)