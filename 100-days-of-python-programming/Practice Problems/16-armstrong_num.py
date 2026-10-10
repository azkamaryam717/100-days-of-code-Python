# Write a program that will check whether the number is armstrong number or not
# For length 3
user_input = int(input("Enter a three digit number: "))
num = user_input
arm = 0

while num != 0:
    rem = num % 10
    arm += rem ** 3 # or simply=> arm += rem * rem * rem
    num = num // 10

if arm == user_input:
    print("Armstrong") 
else:
    print("Not Armstrong")


# Second Method

user_input = int(input("Enter your number: "))
num = user_input

a = num % 10
num = num // 10
b = num % 10
c = num // 10

if (a**3) + (b**3) + (c**3) == user_input:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# For any length of numbers

user_input = int(input("Enter your number: "))
num = user_input
digits = len(str(user_input))
total = 0

while num != 0:
    rem = num % 10
    total += rem ** digits
    num = num // 10

if total == user_input:
    print("Armstrong number")
else:
    print("Not an Armstrong number")