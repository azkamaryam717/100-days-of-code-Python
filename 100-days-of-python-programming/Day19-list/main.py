# Python Lists
# A list stores references to objects, rather than storing the objects themselves directly.
# proof --->
L = [1, 2, 3]
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))

# 1. Create
# Empty
L = []
print(L)
# 1D ---> Homogeneous list
L1 = [1, 2, 3, 4, 5]
print(L1)
# Hetrogenous list
L2 = ["Hello", 4, 5, 6, True, (5+6j)]
print(L2)
# Multidimentional list:
# 2D
L3 = [1, 2, 3, [4,5]]
print(L3)
# 3D
L4 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(L4)
# Using Type Conversion
name = list("Azka")
print(name)
L5 = list()
print(L5)

# 2. Access
print(L1)
print(L1[0])
print(L1[-1])
print(L1[1:4]) # Slicing
print(L1[::-1])
print(L3)
print(L3[0])
print(L3[-1])
x = L3[-1]
print(x)
print(x[0])
print(L3[-1][0])
print(L3[-1][-1])
print(L4)
print(L4[-1][-1][0])
print(L4[-1][0][1])

# 3. Edit
# Lists in Python are Mutable
print(L1)
# Editing With Indexing
L1[0] = 100
print(L1)
L1[-1] = 500
print(L1)
# Editing With Slicing
L1[1:4] = [200, 300, 400]
print(L1)

# 4. Add
# append() adds only one element at the end of list
# extend() adds one or more elements to the end of list
# insert() can insert element at a specific position
print(L1)
print(L1.append("Azka"))
print(L1.extend([600, 700, 800]))
print(L1.append([5, 6]))
print(L1.extend("Hello"))
print(L1.insert(-1, "World"))

# Delete 
# del deletes an item from a list or deletes the variable itself
# .remove() deletes a specific element
# .pop() deletes the last element
# clear() removes all elements from the list; it returns None
print(L2)
del L2
# print(L2) # NameError because we deleted L2 before
del L1[0]
print(L1)
del L1[-6]
print(L1)
del L1[-5:]
print(L1.remove(400))
print(L1)
print(L1.remove("Azka"))
print(L1.pop())
print(L1.clear())
print(L1)

# 6. Operations
# 1. Arithmetic
L = [1, 2 ,3 , 4]
L1 = [5, 6, 7, 8]
# Concatenation/Merge
L2 = L + L1
print(L2)
# Original List still remains same
print(L)
print(L1)
print(L * 3)
# 2. Membership
print(L3)
print(4 in L3)
print([4, 5] in L3)
# 3. Loop
for i in L:
    print(i)
for i in L3:
    print(i)

# 7. Functions
print(L)
# len()
print(len(L))
# min()
print(min(L))
# max()
print(max(L))
# sorted()
print(sorted(L))
print(sorted(L, reverse = True)) # Temporary sort
print(L1) # still remains same
# sort()
print(L.sort(reverse = True)) # Permanent sort
print(L)
print(L.sort())
# count()
L = [1, 2, 1, 3, 3, 4, 1, 5, 2, 1]
print(L.count(1))
# index
L = [1, 2, 3, 4]
print(L.index(2))
# reverse
# permanently reverses the list
L = [2, 1, 4, 7, 0, 9]
print(L.reverse())

# sort (vs sorted)
L = [2, 1, 4, 7, 0, 9]
print(sorted(L)) # New sorted list
print(L) # Original list (unchanged)
print(L.sort()) # Original list (sorted)

# copy ---> shallow
L = [2, 1, 5, 7, 0]
print(L)
print(id(L))
L1 = L.copy() # makes a shallow copy of L but original L remains unchanged
print(L1)
print(id(L1))

# title()
print("hi, my name is azka".title())

# Title Case a String Without title()
sample = "Hi, how are you?"
sample.split()
L = []
for i in sample.split():
    L.append(i.capitalize())
print(L)
print(" ".join(L))

# Extract Username from an Email
sample_mail = "azka@gmail.com"
print(sample_mail[:sample_mail.find("@")])

# Distinct Elements From a list
L1 = [1, 1, 2, 2, 3, 3, 4, 4]
# Output: L1 = [1, 2, 3, 4]
L = []
for i in L1:
    if i not in L:
        L.append(i)
print(L)

# 8. List Comprehension
L = [1, 2, 3, 4, 5, 6, 7]
L1 = [item * 2 for item in L]
print(L1)
L2 = [i ** 2 for i in range(10)]
print(L2)
L3 = [i ** 2 for i in range(10) if i%2 != 0]
print(L3)
fruits = ['Apple', 'Orange', 'Mango', 'Guava', 'Banana']
L4 = [fruit for fruit in fruits if fruit[0] == "O"]
print(L4)
# Add 1-10 to list
# Normal method
L = []
for i in range(1, 11):
    L.append(i)
print(L)
# With List Comprehension
L = [i for i in range(1, 11)]
print(L)

# Scalar Multiplication
v = [2, 3, 4] # Vector
s = -3 # Scalar
L = [s*i for i in v]
print(L)

# Add Squares
L = [1, 2 ,3 ,4 ,5]
L1 = [i**2 for i in L]
print(L1)

# Print nums divisible by 5 from 1 to 50
L = [i for i in range(1,51) if i%5 == 0]
print(L)

# Languages starting with 'p'
languages = ['java', 'python', 'php', 'c', 'javascript']
L = [language for language in languages if language.startswith("p")]
print(L)

# Nested If with List Comprehension
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
L = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a') ]
print(L)

# 3x3 Matrix via Nested List Comprehension
L = [[i*j for j in range(1,4)] for i in range(1,4)]
print(L)

# Cartesian Products ---> List Comprehension on 2 lists together
# Multiply every combination of elements from 2 lists
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L = [[i*j] for i in L1 for j in L2]
print(L)

# 9. List Traversal
# Itemwise
L = [1, 2, 3, 4]
for i in L:
    print(i)
# Indexwise
L = [1, 2, 3, 4]
for i in range(0, len(L)):
    print(L[i])

# 10. Zip()
# Add items of 2 lists indexwise
L1 = [1, 2, 3, 4]
L2 = [-1, -2, -3, -4]
L = list(zip(L1, L2))
L3 = [i+j for i, j in L]
print(L3)

# List Programs
# 1. Split list into odd and even
L = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = [i for i in L if i%2 != 0]
even_numbers = [i for i in L if i%2 == 0]
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

# 2. List Input from User
# 1. Prompt input
input_string = input("Enter the list elements separated by spaces: ")
# 2. Split string
string_list = input_string.split()
# 3. Convert to integers
integer_list = [int(item) for item in string_list]
# 4. Output
print("The input list is: ", integer_list)

# 3. Merge 2 Lists Without + Operator
# 1. Using `extend()` Method
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
# Merge L2 into L1
L1.extend(L2)
print("Merged list:", L1)
# 2. Using for Loop
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
for element in L2:
    L1.append(element)
print("Merged list:", L1)

# 4. Replace item in list
L = [1, 2, 3, 4, 5, 3]
old_item = 3
new_item = 300
for i in range(len(L)):
    if L[i] ==  old_item:
        L[i] = new_item
print("Updated list:", L)

# 5. Convert 2D to 1D List
# Define 2D list
L2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Initialize 1D list
L1D = []
# Flatten 2D to 1D
for i in L2D:
    for j in i:
        L1D.append(j)
print("1D list:", L1D)

# 6. Remove Duplicates from List
L = [1, 2, 1, 2, 3, 4, 5, 3, 4]

# Convert to set ---> Removes duplicates; Convert back to list.
L_unique = list(set(L))
print("List with duplicates removed:", L_unique)

# 7. Check if list is ascending
def is_ascending(L):
    for i in range (len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True

# Test
L1 = [1, 2, 3, 4, 5]
L2 = [1, 3, 2, 4, 5]
print("L1 is in ascending order:", is_ascending(L1))
print("L2 is in ascending order:", is_ascending(L2))