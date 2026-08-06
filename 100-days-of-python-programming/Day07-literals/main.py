# Numerical Literals
#   a. Integer literals
a = 0b10010 # Binary (starts with 0b followed by the binary number)
b = 500 # Decimal
c= 0o310  # Octal(starts with 0o followed by the octal number)
d = 0x14c # Hexadecimal (starts with 0x followed by the hex number)

#   b. Float literals
f1 = 15.5  # Decimal floating-point
# 'e' represents the power of 10.
f2 = 1.5e2 # Scientific notation (1.5 × 10² = 150.0)
f3 = 1.5e-3 # Scientific notation (1.5 × 10⁻³ = 0.0015)

#   c. Complex literal
x = 10 + 4.14j

print(a, b, c, d)
print(f1, f2, f3)
# .imag returns the imaginary part and .real returns the real part
print(x, x.imag, x.real) 


# 2. String literals
# Strings can be written using single or double quotes. 
# Both are treated the same by Python.
string1 = 'This is Python' 
string2 = "This is Python"

 # Python has no separate char type, a single character is still a string
char = "C"
multiline_string = """This is line 1.
This is line 2.
This is line 3."""

# 'u' is optional in Python 3 because strings are Unicode by default.
unicode = u"\U0001f600\U0001F606\U0001F923" 

# Raw strings(starts with r) treat backslashes literally.
# Escape sequences like \n and \t are not interpreted.
raw_string = r"raw \n string" 

print(string1)
print(string2)
print(char)
print(multiline_string)
print(unicode)
print(raw_string)


# 3. Boolean literals
# In Python, True behaves like 1 and False behaves like 0.
# Python performs implicit type conversion when used with integers.
a = True + 5 
b = False + 5
print("a:",a)
print("b:",b)


# 4. Special literals
# None represents the absence of a value.
# It is often used to initialize variables that will be assigned later.
k = None 
print(k)