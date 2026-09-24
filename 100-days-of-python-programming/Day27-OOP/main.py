# OBJECT-ORIENTED PROGRAMMING
# OOP is a programming paradigm using objects & classes
L = [1, 2, 3, 4]
print(L)
# L.upper() # AttributeError: 'list' object has no attribute 'upper'
city = "Lahore"
a = "Karachi"
# city.append('a') # AttributeError

# 1. Class
# Blueprint for objects and Defines object behavior 
# variables are also objects
a = 2
print(type(a))
print(L)
# In Python, Datatype = Class and Variable = Object of Class
# Attributes: Data/Properties
# Methods: Functions/Behavior

# Class Basic Structure
class Car:
    color = "Red" # data
    model = "sports" # data
    def calculate_avg_speed(self, km, time):
        # some code
        print("Average speed in km")

# Object 
# Object is an instance of a Class
# Class is the data type; Object is a variable of a Class
# Object Examples:
wagonr = Car()  # Car ---> WagonR 
# cricket = Sports() # Sports ---> Cricket
# cat = Animals() # Animals ---> Cal

print(L)
L = list()
print(L)
city = str()
print(city)

# Practical Implementation of Class and Object
# Functions inside class are called methods

class Atm():
    __counter = 1
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.sno = Atm.__counter # instance var
        Atm.__counter = Atm.__counter + 1
        print(id(self))
        self.__menu()
    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin Changed")
        else:
            print("Not Allowed")

    def __menu(self):
        user_input = int(input("""
                       Hello, how would you like to proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit  
"""))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            print("Bye")
        else:
            print("Invalid input")

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin set successful")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print("Balance: ", self.__balance)
        else:
            print("Invalid pin")

sbi = Atm()
sbi.deposit()
sbi.check_balance()
sbi.withdraw()
sbi.check_balance()

asdf = Atm()
asdf.deposit()
asdf.check_balance() # balance you entered for asdf object
sbi.check_balance() # balance you previously entered for sbi object

# Magic Methods
# Triggered automatically, not called directly by objects.
# Constructor( __init__() is a special (dunder) method automatically called when an object is initialized.)
#__init__() is an initializer, while __new__() is responsible for creating the object
# Constructor is a magic method invoked during object creation.
# Constructor ---> Special/Magic/Dunder Methods
print(dir(int))

# self
sbi = Atm()
print(id(sbi)) # self refers to the same object as sbi inside its methods(sbi = self)
hdfc = Atm()
print(id(hdfc)) # hdfc = self
print(id(sbi))
# self refers to the current object instance
# sbi → its own balance
# asdf → its own balance
# They don't share __balance.

# But: __counter is a class variable, so it is shared by the class.

# ---EXAMPLE---
# Creating Custom Data Type (Fraction) & Corresponding Methods to Add, Sub, Mul and Divide Fractions

class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den) 

    def __add__(self, other):
        temp_num = self.num * other.den + other.num + self.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

    def __sub__(self, other):
            temp_num = self.num * other.den - other.num + self.den
            temp_den = self.den * other.num
            return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)
    
    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

x = Fraction(4, 5)
print(x)
print(type(x))

y = Fraction(5, 6)
print(y)
print(type(y))

L = [1, 2, 3, 4, x]
print(L)
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Encapsulation
# Instance Variable (Unique value per object)

sbi = Atm()
# sbi.__balance
sbi.deposit()

sbi = Atm()


# Pass By Reference
class Customer:
    def __init__(self, name):
        self.name = name

cust = Customer("Azka")
print(cust.name)

class Customer:
    def __init__(self, name):
        self.name = name 
    def greet(self):
        print("Hello", self.name)

cust = Customer("Azka")
cust.greet()

class Customer:
    def __init__(self, name , gender):
        self.name = name
        self.gender = gender
    def greet(customer):
        if customer.gender == "Male":
            print("Hello ", customer.name, " sir")
        else:
            print("Hello ", customer.name, " ma'am")

cust = Customer("Azka", "Female")
cust.greet()

# In Python, everything including all data types(e.g., int, str, list, dict) are object.
# Custom class instances = objects too.

class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def greet(self):
        if self.gender == "Male":
            print("Hello ", self.name, "Sir")
        else:
            print("Hello ", self.name, "Ma'am")
        cust2 = Customer("Azka", "Female")
        return cust2

cust = Customer("Hadia", "Female")
new_cust = cust.greet()
print(new_cust.name)