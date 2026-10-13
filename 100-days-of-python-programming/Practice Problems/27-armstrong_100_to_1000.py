# Print all the armstrong numbers in the range of 100 to 1000
# First Method
# First Method

for i in range(100, 1001):
    temp = i
    arm = 0

    while temp != 0:
        rem = temp % 10
        arm += rem ** 3
        temp = temp // 10

    if arm == i:
        print(i)

# Second Method

for num in range(100, 1000):
    i = num
    a = num % 10
    num = num // 10
    b = num % 10
    c = num // 10
    if (a**3) + (b**3) + (c**3) == i:
        print(i)