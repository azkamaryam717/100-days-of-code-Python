num = int(input("Enter a 4 digit number: "))
while num != 0:
    rem = num % 10
    num = num//10
    print(rem, end='')
print()
    
# Second Method
num=int(input("Enter a 4 digit number: "))
print(str(num)[::-1])

# Third Method
user_input = int(input("Enter the four digit number: "))
num = user_input

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
d = num // 10

reverse = 1000*a + 100*b + 10*c + d

print("original number: ", user_input)
print("reverse number: ", reverse)