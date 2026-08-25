# Dictionary in Python
# Create
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
# Arithmetic operations are not allowed
print(D3)
print(D4)
# D3 + D4 # TypeError 
# D3 * 3 # TypeError

# Iteration
for i in D3:
    print(i)

for i in D3:
    print(i, D3[i])

# Membership
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