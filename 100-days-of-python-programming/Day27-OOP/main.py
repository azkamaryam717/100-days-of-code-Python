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
    # getter and setters are used to access an modify private data members
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
sbi.__balance = "asdfgh"
sbi.deposit()

# Class Data Encapsulation:
# Python ---> Use `__` prefix (e.g., `self.__pin`, `self.__balance`) for data hiding.
obj = Atm()
obj.__balance = "asdfghg"
obj.deposit()
obj.check_balance() # no error
obj._Atm__balance = "wertw"
# obj.deposit() # code crash

# Python Variable Privacy:

# `__balance` ---> Name-mangled to `_Atm__balance`.
# _Truly private_ is not a concept in Python.
# `__balance` is _pseudo-private_, but accessible via `_Atm__balance` if known.
# getters and setters 
obj.get_pin()
obj.set_pin(1234)

# let's set a Rule ---> PIN must be a String
obj.set_pin(5.6) # Output: Not allowed, because we used a rule for pin in set_pin method(Encapsulation)
sbi.get_pin()


# Reference Varialble
Atm() # Object created but is unusable because we never stored it in variable
# whenever creating object, write this code:
obj = Atm() # obj is reference variable and Atm() is object


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

class Customer:
    def __init__(self, name):
        self.name = name
    def greet(customer):
        customer.name = "Azka"
        print(customer.name)

cust = Customer("Hadia")
cust.greet()

class Customer:
    def __init__(self, name):
        self.name = name
    def greet(customer):
        customer.name = "Azka"
        print(customer.name)

cust = Customer("Hadia")
cust.greet()
print(cust.name)

# Object Mutation in Functions:
# Passing obj to func ---> func modifies obj ---> Original obj reflects changes.

class Customer:
    def __init__(self, name):
        self.name = name
    def greet(customer):
        print(id(customer))
        customer.name = "Azka"
        print(customer.name)
        print(id(customer))

cust = Customer("Hadia")
print(id(cust))
print(cust)
print(cust.name)

# class objects are mutable like lists, dict, sets.
def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1, 2, 3, 4]
print(id(L1))
print(L1)
change(L1)
print(L1)

L1 = [1, 2, 3, 4]
print(id(L1))
print(L1)
change(L1[:]) # Cloning
print(L1) 
# Avoid passing original list; inter operations may alter the original list.
# Use "cloning" to prevent external changes

# Collection of Objects
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cust1 = Customer("Azka", 20)
cust2 = Customer("Hadia", 34)
cust3 = Customer("AbdulAhad", 29)

L = [cust1, cust2, cust3]
for i in L:
    print(i) # this will only print object references

# To print actual object data
for i in L:
    print(i.name, i.age)

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am ",self.name,"and I am ", self.age)

cust1 = Customer("Azka", 20)
cust2 = Customer("Hadia", 34)
cust3 = Customer("AbdulAhad", 29)

L = [cust1 , cust2, cust3]

for i in L:
    i.intro()

# Looping & Objects:
# Object Collection: Lists, tuples, dicts can store custom class objects
# Loop + List ---> treat list as object; compatible with looping.
# Dict/Tuple  ---> compatible with loops, same approach as lists in loops.
# Sets        ---> immutable data types only; incompatible with mutable objects in loops.

# Static Variables and Methods

# Back to ATM Code Enhancement
# Like adding unique serial number for each user.

c1 = Atm()
c2 = Atm()
c3 = Atm()

c1.sno
c2.sno
c3.sno
# Problem:   `self.sno` resets on each object creation.

# Variable Types
# 1. Instance Variable: Unique per object (e.g., pin, balance, GPA).
# 2. Static/Class Variable: Same across objects (e.g., IFSC code, Degree no.)

# Now for this ATM Code we will create a Static Variable
# Note ---> Static Variable is Defined outside constructor.
#           Instance Variable is Defined inside constructor.

c1 = Atm()
c2 = Atm()
c3 = Atm()

c1.sno
c2.sno
c3.sno

c3.__counter # counter value in memory = 4
c2.__counter
c1.__counter
Atm.__counter

# Class Relationship
# --- 1. Aggregation ---

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

add = Address("Lahore", 234512, "Punjab")
cust = Customer("Azka", "Female", add)
print(cust.address)
print(cust.address.city)
print(cust.address.pincode)

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_state)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

add = Address("Lahore", 22334, "Punjab")
cust = Customer("Azka", "Female", add)
cust.edit_profile("Maryam", "Karachi", 876556, "Sindh")
print(cust.address.pincode)

# --- 2. Inheritance ---
# Code Reusability (Saves Time; Concise, Optimized Code; Effective)

class User:
    def login(self):
        print("login")

    def register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

stu1 = Student()
stu1.enroll()
stu1.review()
stu1.login()
stu1.register()
u = User()
# u.enroll() # AttributeError because reverse is not possible

# Ex 1 - Inheriting Constructer
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(200000, "Apple", 13)
print(s.brand)


# Ex 2 - Inheiting Private Members
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
    
class SmartPhone(Phone):
    pass
    
s = SmartPhone(200000, "Apple", 13)
# print(s.__brand) # AttributeError because hidden parent members are not accessible by chile

# POLYMORPHISM
# Ex 3 - Polymorphism
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
    
s = SmartPhone(200000, "Apple", 13)
s.buy() # Method Overriding

# Polymorphism
# Method Overriding
# Method Overloading:
# Operator Overloading

# Ex - Class Parent
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def show(self):
        print("This is in child class")

son = Child(100)
print(son.get_num())
son.show()

# Ex 2
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, val, num):
        self.__val = val

    def get_val(self):
        return self.__val
    
son = Child(100, 10)
# print("Parent: Num:", son.get_num()) # AttributeError 
print("Child: Val", son.get_val())

# No Child Constructor      ---> Parent Constructor invoked automatically.
# Child Constructor present ---> Parent Constructor not called.
# Hence parent num was not assigned any values as the constructoe was never invoked

# Example 3
class A:
    def __init__(self):
        self.var = 100

    def display(self, var):
        print("Class A: ", self.var)

class B(A):
    def display2(self, var):
        p("Class B: ",self.var)

obj = B()
obj.display(200)

# --- Use of super() Keyword ---
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        super().buy() # Call Parent's buy() method

s = SmartPhone(200000, "Apple", 13)
s.buy()

# Example - Super with Constructor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os , ram):
        print("Inside smartphone constructor")
        super().__init__(price, brand , camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone constructor")
    def buy(self):
        print ("Buying a smartphone")
        super().buy() # Call Parent's buy() method

s = SmartPhone(200000, "Apple", 13)
print(s.os)
print(s.brand)

# Example - super()

class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, val, num):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val
    
son = Child(100, 10) 
print(son.get_num())
print(son.get_val())

class Parent:
    def __init__(self):
        self.num = 1000

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 2000

    def show(self):
        print(self.num)
        print(self.var)

son = Child()
son.show()

class Parent:
    def __init__(self):
        self.__num = 1000
    def show(self):
        print("Parent:", self.__num)
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var = 2000

    def show(self):
        print("Child:", self.var)

son = Child()
son.show()

# --- Types of Inheritance ---
# 1. Single level Inheritance
# 2. Multi level Inheritance
# 3. Hierarchical Inheritance
# 4. Multiple Inheritance (Diamond Problem)
# 5. Hybrid Inheritance

# Ex - Single level Inheritence
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000, "Apple", "13px").buy()

# Ex - Multilevel level Inheritence
class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(20000, "Apple", 13)
p = Phone(100000, "Samsung", 1)

s.buy()
s.review()
p.review()

# Ex - Hierarchical Inheritence
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000, "Apple", "13px").buy()

# Ex - Multiple Inheritence

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")

class Produnct:
    def review(self):
        print("Customer review")

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000, "Apple", 12)

s.buy()
s.review()

# --- MRO - Method Resolution Order ---
# MRO => Order of inheritance determines priority.
# In conflict, methods from first-inherited classes execute
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# MRO: Product ---> Phone ( fist priority for same name method is Product as its written first)
class SmartPhone(Product, Phone):
    pass

s = SmartPhone(20000, "Apple", 12)
s.buy()

# Ex - Multilevel Inheritence

class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1() + obj3.m1() + obj3.m2())

class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        val = super().m1() + 30
        return val

class C(B):
    def m1(self):
        val = self.m1() + 20
        # return val # This code will causes infinite recursion

obj = C()
print(obj.m1())

# Method Overloading and Operator Overloading
# --- Polymorphism ---
# 1. Method Overriding
# 2. Method Overloading
# 3. Operator Overloading

# --- Method Overloading ---
class Geometry:
    def area(self, radius):
        return 3.14 * radius * radius
    def area(sef, l, b):
        return l * b

obj = Geometry()
# print(obj.area(4)) # TypeError missing 1 argument

# Method Overloading in Java   ---> Multiple methods, same name, different inputs.
#                    in Python ---> No true traditional method overloading.
#                                   Same method name = last definition overrides previous.

# Multiple methods with same name not allowed.
# Workaround: 
# Use default paramseters or variable args for simulated overloading.

def area(self, a, b = 0):
    if b == 0:
        print("Circle ", 3.14 * a * a)
    else:
        print("Rectangle ", a * b)

obj = Geometry()
obj.area(4)
obj.area(4, 5)

# "Operator Overloading" ---> Customize default operator behavior.
#                             (e.g., `+` for addition[built-in] beyond that 1. string concatenation, 2. custom class Fraction Addition etc.) 

print("Hello " + "World") # String class designer redefined `+` operator for concatenation

x = Fraction(3, 4)
y = Fraction(5, 6)

print(x + y) # Fraction addition, where `+` is redefined

print(4 + 5) # built-in

L = [1, 2, 3] + [4, 5] # List Concatenation
print(L)


# --- ABSTRACTION ---
# Hides implementation details; focuses on functionality.

# --- Abstract Class ---
# 1. Abstract Class: Contains at least 1 Abstract Method 2. Abstract Method: No implementation/code.

# 2 Method Types:
# 1. Abstract: No code 2. Concrete: Contains code.