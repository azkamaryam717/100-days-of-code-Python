# The current population of a town is 10,000.
# The population of the town is increasing at a rate of 10% per year.
# You have to write a program to find out the population at the end of each of the last 10 years.

# For example, if the current population is 10,000, the output should be like this:
# 10th year - 10,000
# 9th year - 9,000
# 8th year - 8,100, and so on.

# First Method

population = 10000

for year in range(10, 0, -1):
    print(year, "year -", round(population))
    population = population * 0.9


# Second method
flag = 0
a = 10000

print(a)

while True:
    b = (a) - ((10*a)/100) 
    a = b
    print(int(b))
    flag = flag + 1
    if flag == 9:
        break