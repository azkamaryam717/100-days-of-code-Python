import math

radius = float(input("Enter the radius of cylinder: "))
height = float(input("Enter the height of cylinder: "))

volume = math.pi * radius**2 * height

print("Volume of Cylinder is: ", volume)

# Determine the cost when the price of 1 liter of milk is 40 Rs

cost = volume/1000 * 40
print("Cost for 1 liter of milk is ", cost)