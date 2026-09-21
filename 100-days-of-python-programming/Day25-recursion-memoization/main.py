# Recursion (Function calls itself)
# Iterative Vs Recursive
# Example 1: multiplication without *
# iterative method
def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result
print(multiply(3, 4))

# Recursive Method
# 1. Base Case: Define stopping condition.(stops the recursive calls)
# 2. Recursive case: Reduces the problem by 1.
# 3. Decompose: Break main problem into smaller subproblems until base case is reached.
def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b-1)
print(mul(3, 4))

# Example 2: Factorial via Recursion
def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number - 1)
print(fact(5))

# Example 3: Palindrome
def palindrome(text):
    if len(text) <= 1:
        return "Palindrome"
    else:
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
        else:
            return "Not a Palindrome"
print(palindrome("madam"))
print(palindrome("malayalam"))
print(palindrome("python"))
print(palindrome("abba"))  

# Example 4: The Rabbit Problem: Fibonacci Number

# Scenario ---> 2 newborn rabbits: 1 male + 1 female monthly.
#               Reproduce after 1 month, immortality.
def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m-1) + fib(m-2)
print(fib(12)) # T = O(2^n)
# The naive recursive Fibonacci has exponential time complexity, commonly written as O(2^n).

import time

start = time.time()
print(fib(12))
print(time.time() - start)

start = time.time()
print(fib(24))
print(time.time() - start)

start = time.time()
print(fib(36))
print(time.time() - start)

# As n increases, execution time grows exponentially, so this method is inefficient.

# Solution: This problem can be solved by Memoization
# Memoization refers to remembering method call results based on inputs.
# Memoization stores previously calculated results.
# When the same input occurs again, the stored result is reused.
# It avoids repeated calculations and improves performance.

# Example 5: Fibonacci with Memoization approach
def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m-1, d) + memo(m-2, d)
        return d[m]
d = {0:1, 1:1}
print(memo(12, d))
print(memo(36, d))
print(memo(48, d))
start = time.time()
print(memo(48, d))
print(time.time() - start)

start = time.time()
print(memo(500, d))
print(time.time() - start)

start = time.time()
print(memo(1000, d))
print(time.time() - start)
print(d) # Dictionary stores previously calculated Fibonacci results.
# With memoization, the Fibonacci calculation becomes approximately: Time: O(n), Space: O(n)

# Example 6: Recursive PowerSet Function in Python

# PowerSet: Given set S, return power set P(S) (all subsets of S).
# Input: String
# Output: List of lists containing all subsets
# Example: S = "123", P(S) = ['', '1', '2', '3', '12', '13', '23', '123']

def powerset(xs):
    res = [[]]

    if len(xs) == 1:
        res.append([xs[0]])
        return res
    else:
        z = []
        for i in powerset(xs[1:]):
            z.append(i)
            z.append([xs[0]] + i)
        return z
final = powerset('123')
print(final)
print(len(final))