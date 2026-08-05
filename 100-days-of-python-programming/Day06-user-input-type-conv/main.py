# Taking user input
input('Enter Email')
# Storing user input in a variable for future use
age=input("Enter your age: ")

# input() returns a string
first_num=input("Enter first number: ")
second_num=input("Enter second number: ")

print(first_num)
print(second_num)

# Strings are concatenated, not added mathematically.
result = first_num + second_num
print(result)

# type() function
print(type(8))
print(type(4.5))
print(type(first_num))

# Automatic type conversion (implicit)
print(5+5.6) # int + float=float
print(type(5),type(5.6))
print(8+5+7j) # int + complex=complex
print(5.3+2+8j) # float + int + complex=complex

# Type error occurs for the following line
# print(4+"4")

# Explicit type conversion (type casting)
print(int("4")) # str to int
print(str(5)) # int to str
print(float(4)) # int to float
print(bool(1)) # int to bool
print(complex(4)) # int to complex
print(list("Hello")) # str to list
print(set("Hello")) # str to set
print(tuple("Hello")) # str to tuple


# Explicit type conversion does not change the original variable.
a=4.5
print(int(a)) # prints 4
print(a) # prints 4.5

first_num=input("Enter first number: ")
second_num=input("Enter second number: ")
result = int(first_num) + int(second_num)
print(result)

first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
result = first_num + second_num
print(result)