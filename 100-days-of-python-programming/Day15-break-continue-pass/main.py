# break ends the loop immediately when the condition is true
# Example 1
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Example 2 
# Print prime numbers in a given range
lower = int(input("Lower: "))
upper = int(input("Upper: "))
for i in range(lower, upper+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

# continue skips to next iteration when the condition is true
# Example 1
for i in range(1,11):
    if i == 5:
      continue
    print(i)

# Example 2
for i in range(1,11):
    if i == 5:
      continue
    print(i)
    print("Hi")

# pass is a placeholder; it does nothing and allows an empty block
for i in range(1,11):
   pass