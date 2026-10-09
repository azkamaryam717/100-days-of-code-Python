num = int(input("Enter a number: "))

if num % 3 == 0 and num % 6 == 0:
    print(num, "is divisible by both 3 and 6")
else:
    print(num, "is not divisible by both 3 and 6")

# Every number divisible by 6 is automatically divisible by 3, 
# So you you only need to check divisibility by 6

num = int(input("Enter a number: "))

if num % 6 == 0:
    print(num, "is divisible by both 3 and 6")
else:
    print(num, "is not divisible by both 3 and 6")