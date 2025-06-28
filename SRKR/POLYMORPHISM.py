# POLYMORPHISM 
# Same method name behaves diffrently depending on the object
class Bird:
    def sound(self):print("CHrip")
class Dog:
    def sound(self):print("Woof")


for animal in (Bird(), Dog()):
    animal.sound()


# Behavior Matters more than class
def call_sound(animal):
    animal.sound()

call_sound(Dog())
call_sound(Bird())




# 🔹 **Problem 14 – Method Overriding with get_details()**

# 🔹 Problem Statement:
# Create a base class `Person` with a method `get_details()`.
# Derive `Student` from `Person` and override `get_details()`.

# 🧪 Test Case:
# p = Person("Alex")
# p.get_details() ➞ "Person: Alex"
# s = Student("John", "Math")
# s.get_details() ➞ "Student: John, Major: Math"


class Person:
    def __init__(self,name):
        self.name = name
    
    def get_details(self):
        return f"Name: {self.name}"

class Student(Person):
    def __init__(self,name,major):
        Person.__init__(self,name)
        # super().__init__(name)
        self.major = major

    def get_details(self):
        return f"Name: {self.name} Major: {self.major}"


p = Person("Alex")
print(p.get_details())
s = Student("John", "Math")
print(s.get_details() )









# 🔹 **Problem 15 – Shape Drawing with Overridden draw()**

# 🔹 Problem Statement:
# Create a base class `Shape` with a method `draw()`.
# Override it in `Square`, `Triangle`, and `Circle` classes.

# 🧪 Test Case:
# shapes = [Square(), Triangle(), Circle()]
# for shape in shapes: shape.draw()

# ✅ Output:
# Drawing Square
# Drawing Triangle
# Drawing Circle




# 🔹 **Problem 16 – Method Overloading Using Default Arguments**

# 🔹 Problem Statement:
# Simulate method overloading using default arguments in a class `Calculator`.

# 🧪 Test Case:
# c = Calculator()
# c.add(5, 3) ➞ 8
# c.add(5) ➞ 5



# 🔹 **Problem 17 – Duck Typing with speak()**

# 🔹 Problem Statement:
# Use duck typing to show polymorphism with `Cat`, `Dog` classes, each having `speak()` method.
# Create a function that calls `speak()` on any object.

# 🧪 Test Case:
# make_animal_speak(Cat()) ➞ "Meow"
# make_animal_speak(Dog()) ➞ "Woof"



# 🔹 Problem Statement:
# Create classes `Cat`, `Dog`, and `Parrot`, each with method `speak()`.
# Demonstrate polymorphism by calling `speak()` on a list of animal objects.

# 🧪 Test Case:
# animals = [Cat(), Dog(), Parrot()]
# for a in animals: a.speak()

# ✅ Output:
# Meow
# Woof
# Squawk




# 🔹 Problem Statement:
# Create base class `Vehicle` with method `drive()`.
# Override `drive()` in `Car` and `Bike`. Call `drive()` polymorphically.

# 🧪 Test Case:
# for v in [Car(), Bike()]: v.drive()

# ✅ Output:
# Driving a car
# Riding a bike



# 🔹 Problem Statement:
# Create a base class `Notification` with method `send()`.
# Override it in `Email`, `SMS`, and `PushNotification` classes.

# 🧪 Test Case:
# notifs = [Email(), SMS(), PushNotification()]
# for n in notifs: n.send()

# ✅ Output:
# Sending Email
# Sending SMS
# Sending Push Notification




# 🔹 Problem Statement:
# Create an abstract base class `FormField` with method `validate()`.
# Implement subclasses: `TextField`, `EmailField`, `NumberField`, each with custom validation.

# 🧪 Test Case:
# fields = [TextField("hello"), EmailField("test@x.com"), NumberField("123")]
# for f in fields: print(f.validate())

# ✅ Output:
# Valid Text
# Valid Email
# Valid Number





# 🔹 Problem Statement:
# Create a base class `Animal` with abstract methods `move()`, `eat()`, `sleep()`.
# Implement subclasses: `Bird`, `Fish`, `Lion` with custom behaviors.

# 🧪 Test Case:
# animals = [Bird(), Fish(), Lion()]
# for a in animals:
#     a.move()
#     a.eat()
#     a.sleep()

# ✅ Output:
# Bird is flying
# Bird eats seeds
# Bird sleeps in nest
# Fish is swimming
# Fish eats algae
# Fish sleeps with eyes open
# Lion is running
# Lion eats meat
# Lion sleeps in den




# 🔹 Problem Statement:
# Implement the Strategy design pattern using polymorphism for payment:
# Create `PaymentStrategy` interface with method `pay()`.  
# Implement `CardPayment`, `UPIPayment`, and `NetBankingPayment`.
# Use a `PaymentContext` class to switch strategies dynamically.

# 🧪 Test Case:
# ctx = PaymentContext(CardPayment())
# ctx.execute(500) ➞ "Paid 500 using Card"
# ctx.set_strategy(UPIPayment())
# ctx.execute(300) ➞ "Paid 300 using UPI"




