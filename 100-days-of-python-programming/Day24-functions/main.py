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

# Parameters vs Arguments
def power(a, b):
    return a**b
print(power(2,3))
# power(3) # invalid requires 2 arguments
# power() # invalid requires 2 arguments
# Default Argument: Function arguments with default values.
def power(a = 1, b = 1):
    return(a**b)
print(power(2, 3))
print(power(2))
print(power())
# Positional Arguments: Values assigned by call order.
print(power(3, 2))
# Keyword Argument: Values assigned to args by name at call time.
# Keyword args will Overrides Positional args.
print(power(b = 2, a = 3))
# Arbitrary Argument: Accepts any number of args.
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
    print(type)
    for i in number:
        product *= i
    print(product)
print(flexi(1, 2, 3, 4, 5))