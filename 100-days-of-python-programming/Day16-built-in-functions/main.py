# built in functions in python
# 1. print()
print("Hello World")

# 2. input()
input("Enter your name: ")

# 3. type()
# int
a = 3
print(type(a))

# float
a = 3.5
print(type(a))

# bool
a = True
print(type(a))

# str
a = "Hello World"
print(type(a))

# 4. type conversion functions
# int()
# float()
# list()
# tuple()
print(int(5.5))
print(float("5"))
print(str(5.5))

# 5. abs() 
print(abs(4))
print(abs(-4))

# 6. pow()
print(pow(2, 3))
print(pow(2, -3))

# 7. min()/max()
print(min([1, 2, 3, 5, 4, 0]))
print(max([1, 2, 3, 5, 4, 0]))
print(min("Lahore"))
print(max("Lahore"))

# 8. round()
b = 33/7
print(b)
print(round(b))
print(round(b, 3))

# 9. divmod
print(divmod(7, 2))

# 10. bin/oct/hex
print(bin(4))
print(oct(4))
print(hex(4))

# 11. id
a = 5
print(id(a))

# 12. ord
print(ord("A"))
print(ord("a"))

# 13. len
print(len("Lahore"))
print(len([1, 2, 3]))

# 14. sum
print(sum([1, 2, 3, 4, 5]))
print(sum({1, 2, 3, 4, 5}))

# 15. help
help("print")
help("sum")