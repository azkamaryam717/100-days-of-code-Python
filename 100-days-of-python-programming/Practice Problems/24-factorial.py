# Write a program that can find the factorial of a given number provided by the user

num = int(input("Enter a number to calculate it's factorial: "))
fact = 1

if num < 0:
    print("Factorial not possible")
else:
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")

# Second Method

num = int(input("Enter your number: "))
i = 1

if num >= 0:
    while num >= 1:
        i = i * num
        num = num - 1
    print("Factorial of the given number is: ", i)
else:
    print("Factorial not possible")