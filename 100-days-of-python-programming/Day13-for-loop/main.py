# range() function
range(1, 11)
print(list(range(1, 11)))
print(list(range(5)))
print(list(range(1, 11, 2)))
print(list(range(1, 11, 3)))
print(list(range(10, 0, -1)))

# for loop can be used with range() function or sequence
# range()
for i in range(1, 11): # range between 1 to 10
    print(i)

for i in range(1, 11, 2): # 1 to 10 with a step of 2
    print(i)

for i in range(10, 0, -1): # 10 to 1(backwards)
    print(i)

# Sequence
for i in "Lahore": # String  
    print(i)

for i in [1, 2, 3, 4, 5]: # List 
    print(i)

for i in (1, 2, 3, 4, 5): # Tuple 
    print(i)

for i in {1, 2, 3, 4, 5}: # Set 
    print(i)


# 1. Population Growth Calculation

# Current Population: 10000
# Growth Rate: 10% annually
# Duration: 10 years
# Calculate previous population for each year.

curr_population = 10000
for i in range(10 , 0, -1):
    print(i,curr_population)
    curr_population /= 1.1


# 2. Sequence Sum
# Formula: 1/1! + 2/2! + 3/3! + ...

num = int(input("Enter a number: "))
result = 0
fact = 1
for i in range(1, num+1):
    fact *= i
    result += i/fact
print(result)


# 3. Factorial
number = int(input("Enter a number: "))
fact = 1
if number == 0 or number == 1:
    print(fact)
else:
    for i in range(1, number+1):
        fact *= i
    print(fact)