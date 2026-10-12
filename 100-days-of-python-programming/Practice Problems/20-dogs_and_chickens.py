# Write a program that will tell the number of dogs and chicken are there 
# when the user will provide the value of total heads and legs.

heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

dogs = (legs - 2 * heads) // 2
chickens = heads - dogs

if dogs >= 0 and chickens >= 0 and legs % 2 == 0 and 4 * dogs + 2 * chickens == legs:
    print("Number of dogs:", dogs)
    print("Number of chickens:", chickens)
else:
    print("Invalid input. No possible solution.")