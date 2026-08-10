# While loop in Python

# 1. Multiplication table using while loop
number = int(input("Enter a number to print its table: "))
i = 1
while i < 11:
    print(number,"*",i,"=",i*number)
    i += 1

# 2. while loop with else
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print("Limit Crossed!")

# 3. Sum of Digits using while loop
number = int(input("Enter a number: "))
sum_digits = 0
while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10
print(f"Sum of digits of number is {sum_digits}") 

# 4. Average of numbers until 0 using while loop
count = 0
total = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break # break exits the while loop when 0 is entered
    total += number
    count += 1
if count > 0:
    average = total / count
    print(f"Average of Entered numbers: {average}")
else:
    print("No numbers entered")