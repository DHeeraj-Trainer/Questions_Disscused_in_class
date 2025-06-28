class Student:
    def __init__(self, name,id):
        self.name = name
        self.id = id
    def read(self):
        return f"{self.name} is reading"
    def info(self):
        return f"Name: {self.name} and id :{self.id}"

student1=Student("Raju","HX67885")
# print(student1.read())
# print(student1.info())




class Sum:
    @staticmethod
    def add(a,b):
        return a+b

# sum=Sum()
# print(sum.add(5,3))
# print(Sum.add(5,5))


class Prodcut:
    tax=0.18  #class varible
    @classmethod
    def change_tax(cls,new_tax):
        cls.tax=new_tax

prodcut=Prodcut()
# print(prodcut.change_tax(15))
# print(Prodcut.tax)




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
a._balance=1000000000
print(a.balance_enq())
a.__pin=12563
print(a.balance_enq())
a._Account__pin=125336
print(a.balance_enq())






# ----------------------------
# 🟦 Problem 0.1 - Car Class
# ----------------------------
# 🔹 Problem Statement:
# Create a class called `Car` that has attributes: make, model, 
# and year.
# Add a method `display_info()` that prints all car details.

# 🧪 Test Case:
# c = Car("Toyota", "Camry", 2020)
# c.display_info() ➞ "Make: Toyota, Model: Camry, Year: 2020"

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"Make: {self.make} Model: {self.model} and Year:{self.year}" 
c = Car("Toyota", "Camry", 2020)
# print(c.display_info())











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
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w

rectangle=Rectangle(5,3)
# print(rectangle.area())






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

class Counter:
    def __init__(self,count=0):
        self.count = count
    def increment(self):
        self.count+=1
    def get_count(self):
        return self.count

c = Counter()
c.increment()
c.increment()
# print(c.get_count())







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


