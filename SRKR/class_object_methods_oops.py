class Parrot:

    # class attribute
    name = ""
    age = 0

# create parrot1 object
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# create another object parrot2
parrot2 = Parrot()
parrot2.name = "Woo"
parrot2.age = 15

# access attributes
# print(f"{parrot1.name} is {parrot1.age} years old")
# print(f"{parrot2.name} is {parrot2.age} years old")


#method parameters
class Student:
    def __init__(self, name,roll):
        self.name = name
        # self.age = age
        self.roll = roll
    def display(self,age):
        self.age = age
        print(f"{self.name} is {self.age} years old and my roll no is {self.roll} ")

# name=input("Enter name:")
# s1=Student(name,"420")
# s1.display(52)


# Types of Methods
# -->Instance Method
# works with the indivial object data
# -->local variable or  instance variable which created inside of Constructor


class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def greet(self,time):
        if time==6 or self.age==18:
            return f"Hi {self.name} good morning"
        else: return f"Hi {self.name} good evening"

person = Person("Raju",18)
# print(person.greet(0))
# print(person.greet(6))


# @classmethod
class Product:
    tax=0.18 #class varible
    # @classmethod
    def changetax(cls,new_tax):
        cls.tax=new_tax
        return cls.tax

# product=Product()
# print(product.changetax(5))


# @staticmethod
class Calu:
    @staticmethod
    def add(a,b):
        return a+b
print(Calu.add(5,2))
# calu=Calu()
# print(calu.add(5, 2))


#Class vs Object
# role: class:blueprint or structure   Object:instance created from class 
# memory: class:no memory usage object:takes memor when created
# access:class cant acess or cant perform directly the actions
# object: can acces the class and methods and data memebers



# instance varible vs class varible
# instance:inside constructer(self,)
# class:inside class and outside constructer
# acess :object(obj.var)  vs class or object
# value for varible in object will be diffent for instance
# value for varible in object will be same for class

# methods       firstarg   used for                             decorators
# instancemethod:  self      object level data                   none
# classmethod:     cls        class level data                    none or @classmethod
# staticmethod:   none        irrespective or utility methods     @staticmethod


# Four pillars:
# Encapsulation 
# Inheritance
# Abstraction 
# Polymorphism 

# Encapsulation

# Access levels:
# Type            syntax       Access Scope
# Public          self.name       Anywhere
# Protected       self._name      class or inside or subclass
# Private         self.__name     with in the class only

# binidng the data members and methods into one unit of code 
# and restricting access to some levels/components
# -->Protects Data
# -->Achived using Access Modifiers




class Account:
    def __init__(self,name,balance,pin):
        self.name = name
        self._balance = balance
        self.__pin = pin
    
    def deposit(self,amount):
        self._balance += amount
        return f"{amount} deposited"

    def balance_enq(self):
        return f"Balance: {self._balance},pin:{self.__pin}"



a=Account("Raju",10000,1234)
a.deposit(5000)
print(a.balance_enq())





a._balance=10000000
a.__pin=12355
print(a.balance_enq())

# print(a.__pin)
print(a._balance)
print(a._Account__pin)







# ----------------------------
# 🟦 Problem 0.1 - Car Class
# ----------------------------
# 🔹 Problem Statement:
# Create a class called `Car` that has attributes: make, model, and year.
# Add a method `display_info()` that prints all car details.

# 🧪 Test Case:
# c = Car("Toyota", "Camry", 2020)
# c.display_info() ➞ "Make: Toyota, Model: Camry, Year: 2020"

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make :{self.make},Model: {self.model},Year: {self.year}")



# Object
c=Car("Toyota", "Camry", 2020)
c1=Car("BMW","XR",2025)
# c.display()
# c1.display()


# ----------------------------
# 🟦 Problem 0.2 - Rectangle Area
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Rectangle` with attributes: length and width.
# Add a method `area()` to return the area of the rectangle.

# 🧪 Test Case:
# r = Rectangle(5, 3)
# r.area() ➞ 15

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width

shape1=Rectangle(5,3)
# print(shape1.area())


# ----------------------------
# 🟦 Problem 0.3 - Counter
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Counter` with a method `increment()` that increases a count by 1,
# and a method `get_count()` that returns the count.

# 🧪 Test Case:
# c = Counter()
# c.increment()
# c.increment()
# c.get_count() ➞ 2



# ----------------------------
# 🟦 Problem 0.4 - Book Info
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Book` with attributes title, author, and pages. Include a method `summary()`.

# 🧪 Test Case:
# b = Book("1984", "George Orwell", 328)
# b.summary() ➞ "'1984' by George Orwell, 328 pages."



# ----------------------------
# 🟦 Problem 0.5 - Simple Calculator
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Calculator` with methods `add`, `subtract`, `multiply`, `divide`.

# 🧪 Test Case:
# calc = Calculator()
# calc.add(4, 5) ➞ 9


# ----------------------------
# 🟦 Problem 0.6 - Employee Payroll
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Employee` with attributes name, hourly_wage. Add a method `weekly_pay(hours)`.

# 🧪 Test Case:
# e = Employee("John", 20)
# e.weekly_pay(40) ➞ 800



# ----------------------------
# 🟦 Problem 0.7 - Circle Circumference
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Circle` with a radius. Add method `circumference()` and `area()`.

# 🧪 Test Case:
# c = Circle(7)
# c.circumference() ➞ 43.96



# ----------------------------
# 🟦 Problem 0.8 - Student Grade Checker
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Student` with name and marks. Add method `is_pass()` (pass >= 40).

# 🧪 Test Case:
# s = Student("Emma", 45)
# s.is_pass() ➞ True



# ----------------------------
# 🟦 Problem 0.9 - Temperature Converter
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Temperature` with method to convert Celsius to Fahrenheit.

# 🧪 Test Case:
# t = Temperature()
# t.celsius_to_fahrenheit(0) ➞ 32.0


# ----------------------------
# 🟦 Problem 0.10 - Person Info
# ----------------------------
# 🔹 Problem Statement:
# Create a class `Person` with name and age. Add method `greet()` to say hello with name.

# 🧪 Test Case:
# p = Person("Alex", 30)
# p.greet() ➞ "Hello, my name is Alex."

