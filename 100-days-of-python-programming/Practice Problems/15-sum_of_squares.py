# Write a program that will take three digits from the user and add the square of each digit.

num = int(input("Enter the number: "))
total_sum = 0

while num != 0:
    a = num % 10
    num = num // 10
    total_sum += a**2

print("Sum is", total_sum)