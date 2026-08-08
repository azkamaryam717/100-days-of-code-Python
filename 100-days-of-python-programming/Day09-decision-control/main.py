# Conditional Statements: if-elif-else
# Nested if else

# Exercise 1: Email and Password Validation

correct_email = "azka@gmail.com"
correct_password = "1234"

email = input("Enter your Email: ")
if "@" in email:
    password = input("Enter your Password: ")
    if email == correct_email and password == correct_password:
        print("Welcome")
    elif email == correct_email and password != correct_password:
        print("Incorrect password!")
        password = input("Enter password again: ")
        if password == correct_password:
            print("Welcome")
        else: 
            print("Wrong password 2 times in a row! Access denied!!")
    else: print("Incorrect credentials")
else:
    print("Incorrect Email")


# Exercise 2 - Smallest of 3 Numbers

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
third_num = int(input("Enter third number: "))

if first_num <= second_num and first_num <= third_num:
    print("Smallest number is: ",first_num)
elif second_num <= first_num and second_num <= third_num:
    print("Smallest number is: ",second_num)
else:
    print("Smallest number is: ",third_num)


# Exercise 3 - Simple Menu Driven Program

menu = input("""
Hi! how can I help you.
1. Enter 1 for PIN change.
2. Enter 2 for balance check.
3. Enter 3 for withdrawal.
4. Enter 4 for exit.
""")
if menu == "1":
    print("You chose PIN change")
elif menu == "2":
    print("You chose balance check")
elif menu == "3":
    print("You chose withdrawal")
elif menu == "4":
    print("Thanks for using! Exiting.....")
else:
    print("Incorrect input")