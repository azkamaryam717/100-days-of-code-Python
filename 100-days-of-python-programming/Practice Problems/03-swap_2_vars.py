# Swap 2 variables using a third variable
a = 1
b = 2
print(f"Befor swapping: a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")

# Method 2 (Using user input)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num1
num1 = num2
num2 = temp

print("Value of num1: ", num1)
print("Value of num2: ", num2)