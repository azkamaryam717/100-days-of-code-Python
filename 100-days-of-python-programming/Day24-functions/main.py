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