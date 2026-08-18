# strings in Python
# single quotes
a = 'Hello'
print(a)

# double quotes
a = "Hello"
print(a)

# triple quotes(multiline string)
a = '''Hello,
I am Azka'''
print(a)

# use of single and double quotes together
# a= 'It's raining outside'(Syntax error)
a = "It's raining outside" 
print(a)

a = str("Hello") # str does nothing useful here as Hello is already a string
print(a)

# Accessing Substrings from a String
# Indexing
a = "Hello"
print(a[0]) # Positive Indexing
print(a[-1]) # Negative Indexing

# Slicing
a = "Hello World"
print(a[0:6]) # indices 0-5
print(a[3:]) # Starts from index 3 and goes to the end
print(a[:4]) # Assumes that you started slicing from 0-3
print(a[:]) # Assumes you want to print full string
print(a[2:6:2]) # 2-6 but skips one element after printing one
print(a[0:10:3]) # 0-10 but skips two elements after printing one
print(a[0:6:-1])  # Empty because the step is backwards but start < stop
print(a[-5:-1:2]) # -5 to -1 with skipping sfter printing one
print(a[::-1]) # prints starts to end but -1 makes it backwards
print(a[-1:-6:-1]) # -1 to -6 and prints backwards