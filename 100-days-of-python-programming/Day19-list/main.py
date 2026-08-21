# Python Lists
# Stores references/pointers to elements, not the values
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
# 1D ---> Homo
L1 = [1, 2, 3, 4, 5]
print(L1)
# Hetrogenous
L2 = ["Hello", 4, 5, 6, True, 5+6j]
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
print(L1)
L1[0] = 100
print(L1)
L1[-1] = 500
print(L1)
L1[1:4] = [200, 300, 400]
print(L1)