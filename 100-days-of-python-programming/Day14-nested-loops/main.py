# Nested Loops in Python

# 1. Unique Pairs Example
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)

# 2. Pattern/Sequence of asterisks
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    for j in range(0, i):
        print("*", end=" ")
    print()

# 3. Pattern/Sequence of numbers
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    print()