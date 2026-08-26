# Dictionary in Python
# 1. Create
# Empty Dictionary
D = {}
print(D)

# 1D Dictionary
D = {"Name":"Azka", "Gender":"Female"}
print(D)

# D1 = {[1, 2, 3]:"Azka"} # TypeError: unhashable type: 'list'
# with mixed keys
D1 = {(1, 2, 3):"Azka"}
print(D1)
# Duplicate keys are not allowed; the last value replaces the previous one
D2 = {"Name":"Azka", "Name":"Mairah"}
print(D2)
D3 = {"Name":"Azka", "College":"LUMS", "Marks":{"DB":99, "DS":95, "Eng":97}}
print(D3)
# Nested dictionary
d = {
    'name':'Azka',
    'university':"LUMS",
    'sem':5,
    'subjects':{
        'DSA':89,
        'Algebra':88,
        'Database':85
    }
}
print(d)
# Immutable objects can be used as dictionary keys
D4 = {'name': 'Azka', (1, 2, 3): 2}
print(D4)
# using sequence and dict function
D5 = dict([('name', 'Azka'), ('age', 21), (3, 3)])
print(D5)

# 2. Access
print(D)
# D[0] # KeyError
print(D3)
print(D3["Marks"]["DS"])
print(D["Name"])
print(D.get("Name"))
print(D["Gender"])
print(D.get("Gender"))
# .get() safely accesses a key without raising KeyError if the key doesn't exist
print(D.get("Age")) # None if key doesn't exist
print(D.get("Age", 0)) # 0 if key doesn't exist

# 3. Edit
print(D)
D["Name"] = "Hannah"
print(D)
D3["Marks"]["DS"] = 91
print(D3)

# 4. Add
print(D)
D["Age"] = 21
print(D)
D3["Marks"]["Algebra"] = 96

# 5. Delete
D5 = {}
print(D5)
del D5
# print(D5) # NameError because D5 no longer exist
print(D.pop('Name')) # pop() removes a specified key and returns its value
print(D.popitem()) # popitem() removes and returns the last inserted key-value pair
print(D)
del D["Gender"]
print(D)
D.clear()
print(D)

# 6. Operations
# 1. Arithmetic operations are not allowed
print(D3)
print(D4)
# D3 + D4 # TypeError 
# D3 * 3 # TypeError

# 2. Iteration
for i in D3:
    print(i)
for i in D3:
    print(i, D3[i])

# 3. Membership
# The 'in' operator checks dictionary keys, not values
print("Azka" in D3) # False
print("Name" in D3) # True
print("Azka" in D3.values()) # True if Azka is a value

# 7. Functions
print(len(D3))
print(min(D3))
print(max(D3))
print(sorted(D3))
print(sorted(D3, reverse=True))
print(D3.items())
print(D3.keys())
print(D3.values())

# update
d1 = {1:2, 3:4, 4:5}
d2 = {4:7, 6:8}
d1.update(d2)
print(d1)

# 8. Dictionary Comprehension
# 1. Calculate squares
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

# 2. Using if condition
D1 = {key:value for key, value in D.items() if len(key)>3}
print(D1)

# 3. Squares of List items
L = [1, 2, 3, 4, 5, 6, 7, 8]
D2 = {item : item ** 2 for item in L}
print(D2)

# 4. Squares of Even items in list
L = [1, 2, 3, 4, 5, 6, 7, 8]
D2 = {item : item ** 2 for item in L if item % 2 == 0}
print(D2)

# 5. Print 1st 10 nums & squares
D = {i : i ** 2 for i in range(1, 11)}
print(D)

# 6. Print items in dict
distances = {'Lahore':1000, 'Rawalpindi':2000, 'Karachi': 3000}
print(distances.items())

# 7. Change distances in an existing dict
distances = {'Lahore':1000, 'Rawalpindi':2000, 'Karachi': 3000}
D = {key: value*0.62 for(key, value) in distances.items()}
print(D)

# 8. Zip() in Dictionary
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 34.9, 31.2, 29.0, 30.2, 28.9]
D = {i:j for(i, j) in zip(days, temp_C)}
print(D)

# 9. Nested Comprehension
# Print multiplication tables for 2 to 4
D = {i:{j:i*j for j in range(1, 11)} for i in range(2,5)}
print(D)

# 10. Convert list of words to their lengths
words = ["Python", "Java", "C++", "SQL"]
D = {word: len(word) for word in words}
print(D)

# 11. Convert temperatures from Celsius to Fahrenheit
temperatures = [0, 10, 20, 30, 40]
D = {c: (c * 9/5) + 32 for c in temperatures}
print(D)