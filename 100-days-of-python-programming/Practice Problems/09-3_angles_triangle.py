a = int(input("Enter length of side a: "))
b = int(input("Enter length of side b: "))
c = int(input("Enter length of side c: "))

if (a + b + c == 180 and a > 0 and b > 0 and c > 0):
    print("These sides form a triangle")
else:
    print("These sides does not form a triangle")