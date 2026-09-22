# Lambda Functions
x = lambda x : x**2
print(x(5))
a = lambda x,y : x+y
print(a(4, 5))
print(type(a))

b = lambda x : x[0] == 'a'
print(b('apple'))
print(b('banana'))

c = lambda x : 'Even' if x % 2 == 0 else 'Odd'
print(c(3))
print(c(8))
# Lambda functions are Anonymous functions ---> `lambda args: expr`,
# ideal for Higher-order functions, offers Concise function writing without naming.

# Higher order functions
# Normal Function to calculate sum
L = [11, 14, 27, 21, 23, 56, 78, 39, 45, 29, 28, 30]

# Even Sum
# Odd Sum
# Div3 Sum

def return_sum(L):
    even_sum = 0
    odd_sum = 0
    div3_sum = 0
    for i in L:
        if i%2 == 0:
            even_sum += i
    for i in L:
        if i%2 != 0:
            odd_sum += i
    for i in L:
        if i%3 == 0:
            div3_sum += i
    return(even_sum, odd_sum, div3_sum)
print(return_sum(L))

# Higher order function to calculate sum
def return_sum2(func, L):
    result = 0
    for i in L:
        if func(i):
            result += i
    return result
x = lambda x: x % 2 == 0  # Even Sum
y = lambda x: x % 2 != 0  # Odd Sum
z = lambda x: x % 3 == 0  # Divisible by 3 Sum
print(return_sum2(x, L))
print(return_sum2(y, L))
print(return_sum2(z, L))

# Built-in Higher Order Functions
# 1. Map (Applies a function to each item in iterable.)
L = [1, 2, 3, 4, 5, 6, 7, 8]
print(L)
print(map(lambda x : x * 2, L))
print(list(map(lambda x : x * 2, L)))
print(list(map(lambda x : x % 2 == 0, L)))

students = [
    {
        "name" : "Jacob Martin",
        "Father name" : "Ros Martin",
        "Address" : "123 Hills Street",
    },{
        "name" : "Angela Stevens",
        "Father name" : "Robert Stevens",
        "Address" : "3 Upper Street London",
    },{
        "name" : "Ricky Smart",
        "Father name" : "William Smart",
        "Address" : "Unknown",
    }    
]
print(list(map(lambda student : student['name'], students)))

# 2. Filter (Applies a function to sequence)
# Keeps items for which the function returns True
print(L)
print(list(filter(lambda x : x > 4, L)))

fruits = ["Apple", "Orange", "Mango", "Guava"]
print(list(filter(lambda fruit : 'e' in fruit, fruits)))

# 3. Reduce(Reduces an iterable to a single value)
# Combines all items into a single value
import functools
print(L)
print(functools.reduce(lambda x, y : x + y , L))

L1 = [12, 34, 56, 11, 21, 58]
print(L1)
print(functools.reduce(lambda x, y : x if x>y else y, L1))
print(functools.reduce(lambda x, y : x if x<y else y, L1))
