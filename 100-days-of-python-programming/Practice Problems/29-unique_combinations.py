# Write a program to print all the unique combinations of 1, 2, 3, and 4.

# First Method

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a, b, c, d)


# Second Method (unique two-number combinations)
for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            print(i, j)