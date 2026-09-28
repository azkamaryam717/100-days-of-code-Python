age1 = int(input("Enter age 1: "))
age2 = int(input("Enter age 2: "))
age3 = int(input("Enter age 3: "))

max_age = age1

if max_age <= age2:
    max_age = age2

if max_age <= age3:
    max_age = age3

print("Maximum age is ", max_age)

# Solution by using a for loop and list for input and storing ages for larger number of inputs

age = []
for i in range(1, 4):
    n = int(input("Enter Age: "))
    age.append(n)

if age[0] >= age[1] and age[0] >= age[2]:
    print("Maximum age is ", age[0])

elif age[1] >= age[0] and age[1] >= age[2]:
    print("Maximum age is ", age[1])

else:
    print("Maximum age is ", age[2])