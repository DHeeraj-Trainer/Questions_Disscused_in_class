
#  🟦 1. Encapsulation – Hospital Management System

# 📝 Problem Statement
# Build a `Patient` class to store sensitive health data. Use encapsulation to protect attributes like medical history and billing.

# 📋 Requirements

# * Private attributes: `__name`, `__age`, `__medical_history`, `__bill_amount`
# * Public methods: `add_medical_record()`, `get_medical_history()`, `add_bill()`, `pay_bill()`, `get_bill()`

# 🧪 Test Case


# p = Patient("John", 30)
# p.add_medical_record("Flu")
# p.add_bill(200)
# p.pay_bill(50)
# print(p.get_medical_history())   ['Flu']
# print(p.get_bill())              150

class Patient:
    def __init__(self, name,age):
        self.__name = name
        self.__age = age
        self.__medical_history=[]
        self.__bill_amount=0

    def add_medical_record(self,record):
        self.__medical_history.append(record)
    def get_medical_history(self):
        return self.__medical_history.copy()
    def add_bill(self,amount):
        self.__bill_amount += amount
    def pay_bill(self,amount):
        self.__bill_amount -= amount
    def get_bill(self):
        return self.__bill_amount

# p = Patient("John", 30)
# p.add_medical_record("Flu")
# p.add_bill(200)
# p.pay_bill(50)
# print(p.get_medical_history())
# print(p.get_bill())    
















#  🟨 2. Abstraction – Plugin-Based Drawing App

# 📝 Problem Statement
# Create an abstract base class `Shape` with `draw()` and `resize()` methods. Implement `Circle` and `Rectangle` with specific behaviors.

# 📋 Requirements

# * Abstract class: `Shape` with `draw()` and `resize()`
# * Concrete classes: `Circle`, `Rectangle`

# 🧪 Test Case


# shapes = [Circle(), Rectangle()]
# for shape in shapes:
#     shape.draw()
#     shape.resize()
# ```





from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):pass
    @abstractmethod
    def resize(self):pass
class Circle(Shape):
    def draw(self):print("Circle")
    def resize(self):print("Circle Resized")

class Rectangle(Shape):
    def draw(self):print("Rectangle")

    def resize(self):print("Rectangle Resized")

shapes = [Circle(), Rectangle()]
# for shape in shapes:
#     shape.draw()
#     shape.resize()





#  🟩 3. Inheritance – Online Learning Platform

# 📝 Problem Statement
# Build a base class `User` with subclasses: `Student`, `Instructor`, `Admin`. Demonstrate method overriding and role-specific actions.

# 📋 Requirements

# * Common method: `login()`
# * Role-specific methods:

#   * `Student`: `view_courses()`
#   * `Instructor`: `upload_material()`
#   * `Admin`: `manage_users()`

# 🧪 Test Case


# s = Student("Alice", "alice@example.com")
# s.login()
# s.view_courses()

# a = Admin("Bob", "bob@example.com")
# a.login()
# a.manage_users()



class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
    def login(self):
        print(f"{self.name} login Done.")

class Admin(User):
    def manage_users(self):
        print(f"{self.name} Managing users")
class Student(User):
    def view_courses(self):
        print(f"{self.name} Viewing courses")
class Instructor(User):
    def uploading_material(self):
        print(f"{self.name} Uplaoding course")

s = Student("Alice", "alice@example.com")
s.login()
s.view_courses()

a = Admin("Bob", "bob@example.com")
a.login()
a.manage_users()






















#  🟥 4. Polymorphism – Notification System

# 📝 Problem Statement
# Create a `Notification` class and override the `send()` method in `EmailNotification`, `SMSNotification`, and `PushNotification`.

# 📋 Requirements

# * All subclasses override `send()`
# * Call `send()` polymorphically on a list

# 🧪 Test Case


# notifications = [EmailNotification(), SMSNotification(), PushNotification()]
# for n in notifications:
#     n.send()
# ```

#  🌐 5. All Pillars – E-Commerce Checkout System

# 📝 Problem Statement
# Design a mini e-commerce checkout system that uses:

# * Encapsulation: private `Product` attributes
# * Abstraction: `PaymentStrategy` interface
# * Inheritance: `User → Buyer`, `Seller`
# * Polymorphism: dynamic payment methods

# 📋 Requirements

# * Use `Checkout` to switch payment strategy dynamically

# 🧪 Test Case


# product = Product("Shoes", 1200)
# buyer = Buyer("Alice")

# checkout = Checkout(CardPayment())
# checkout.pay_now(product.get_price())

# checkout.set_strategy(UPIPayment())
# checkout.pay_now(500)
# ```





from abc import ABC,abstractmethod

class Product:
    def __init__(self, name,price):
        self.__name = name
        self.__price = price

    def get_price(self):return self.__price
    def get_name(self):return self.__name

class User:
    def __init__(self,name):
        self.name = name

class Buyer(User):pass
class Seller(User):pass
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"paymet done:{amount} using card payemt")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"paymet done:{amount} using UPIPayment")

class Checkout(object):
    def __init__(self, strategy:PaymentStrategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy:PaymentStrategy):
        self.strategy = strategy

    def pay_now(self,amount):
        self.strategy.pay(amount)



product = Product("Shoes", 1200)
buyer = Buyer("Alice")

checkout = Checkout(CardPayment())
checkout.pay_now(product.get_price())

checkout.set_strategy(UPIPayment())
checkout.pay_now(500)