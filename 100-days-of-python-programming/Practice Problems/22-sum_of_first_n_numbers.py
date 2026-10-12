# Write a program to find the sum of first n numbers, where n will be provided by the user

# First Method (Using For Loop)

num = int(input("Enter the limit to add numbers upto that: "))
total = 0

for i in range (1, num+1):
    total += i

print(f"Sum of numbers upto {num} is {sum}")

# Second Method (Using Mathematical Formula)

n = int(input("Enter your number: "))
s = n * (n + 1) // 2

print("Your sum is: ", s)