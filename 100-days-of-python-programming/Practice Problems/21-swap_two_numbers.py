# Write a program that will swap two numbers

# First Method [Best for learning the logic]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping num1 = {num1} and num2 = {num2} ")
temp = num1
num1 = num2
num2 = temp

print(f"After swapping num1 = {num1} and num2 = {num2} ")

# Second Method [a little difficult only useful if specifically requested]

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("Your 'a' is: ", a)
print("Your 'b' is: ", b)

# Third Method [Easiest and most Pythonic]

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping num1 = {num1} and num2 = {num2} ")
num1, num2 = num2, num1
print(f"After swapping num1 = {num1} and num2 = {num2} ")