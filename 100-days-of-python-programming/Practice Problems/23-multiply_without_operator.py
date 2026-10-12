# Write a program that can multiply 2 numbers provided by the user without using the * operator

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
mul = 0
for i in range (1, second_num + 1):
    mul += first_num

print(mul)