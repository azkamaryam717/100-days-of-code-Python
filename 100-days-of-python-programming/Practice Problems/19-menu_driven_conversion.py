# Write a menu-driven program with the following options:

# 1. cm to ft
# 2. cm to inches
# 3. km to miles
# 4. USD to PKR
# 5. Exit

choice = int(input("""
Hi! Welcome to my page.

What would you like to do?

1. cm to ft
2. cm to inches
3. km to miles
4. USD to PKR
5. Exit

Enter your choice: """))

if choice == 1:
    user_input = float(input("Enter length in cm: "))
    conversion = user_input / 30.48
    print(user_input, "cm to ft is", round(conversion, 2), "ft")

elif choice == 2:
    user_input = float(input("Enter length in cm: "))
    conversion = user_input / 2.54
    print(user_input, "cm to inches is", round(conversion, 2), "inches")

elif choice == 3:
    user_input = float(input("Enter length in km: "))
    conversion = user_input * 0.621371
    print(user_input, "km to miles is", round(conversion, 2), "miles")

elif choice == 4:
    user_input = float(input("Enter amount in USD: $"))
    conversion = user_input * 277.01
    print(user_input, "USD in PKR is Rs.", round(conversion, 2))

elif choice == 5:
    print("Exiting...")

else:
    print("Invalid input")