x1 = int(input("Enter x1 of x-coordinate: "))
y1 = int(input("Enter y1 of y-coordinate: "))

x2 = int(input("Enter x2 of x-coordinate: "))
y2 = int(input("Enter y2 of y-coordinate: "))

euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(euclidean_distance)