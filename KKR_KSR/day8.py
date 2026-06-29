class P1:
	def greet(self):
		return "Hello,P1"
class P2:
	def greet(self):
		return "Hello,P2"
class C1(P1,P2):
	def greet(self):
		print("Hello,C1")
		return (super().greet(),P2.greet(self))

# c=C1()
# print(c.greet())
# class GS(C1):pass
	# def greet(self):
		# return "Hello,GS"
# g=GS()
# print(C1.greet(g))
# print(g.greet())

# print(GS.mro())



# You are tasked with designing a simple system to manage employees. Create a base class Employee that stores basic details such as name and ID. Extend this class with a derived class Manager to include the department the manager oversees. Demonstrate how the Manager class can reuse and extend the functionality of the Employee class.
class EMP:
    def __init__(self, name="", id=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id

    def __str__(self):
        return f"Name: {self.name} | Id: {self.id}"


class Manager(EMP):
    def __init__(self, dept, **kwargs):
        super().__init__(**kwargs)
        self.dept = dept

    def __str__(self):
        return f"{super().__str__()} | Dept: {self.dept}"


class Team_lead(Manager):
    def __init__(self, size, **kwargs):
        super().__init__(**kwargs)
        self.size = size

    def __str__(self):
        return f"TeamLead -> {super().__str__()} | Team Size: {self.size}"


class Developer(EMP):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.PL = programming_language

    def __str__(self):
        return f"{super().__str__()} | Programming Language: {self.PL}"


class Intern(Developer, Manager):
    def __init__(self, stipend, **kwargs):
        super().__init__(**kwargs)
        self.stipend = stipend

    def __str__(self):
        return f"Intern -> {super().__str__()} | Stipend: {self.stipend}"


# # Objects (NO extra print spacing)
# IN1 = Intern(name="Ravi", id="789", dept="IT", programming_language="Java", stipend=5000)
# print(IN1)

# M1 = Manager(name="Dheeraj", id="123", dept="IT")
# print(M1)

# TL1 = Team_lead(name="Ramya", id="101", dept="HR", size=5)
# print(TL1)

# D1 = Developer(name="Suresh", id="456", programming_language="Python")
# print(D1)

# print("\nMRO of Intern:", Intern.mro())

class Base:
    def common(self):
        print("Common from Base")

class A(Base):
    def common(self):
        print("Common from A")
        super().common()


class B(Base):
    def common(self):
        print("Common from B")
        super().common()


class C(A, B):
    def __init__(self):
         self.__age = 18 #------> Private Variable
    def common(self):
        print("Common from C")
        super().common()


c = C()
# c.common()
# print(C.mro()) 
# print(C.__mro__)
# print(dir(c))
# print(hasattr(c, 'common'))  # True
# print(getattr(c, 'common1', None) ) # Returns None if 'common1' does not exist
# method()  # Calls c.common()

# Function / Attribute    Purpose
# ------------------------------------------------------------
# mro()                  -> Method lookup order
# __mro__                -> Internal MRO tuple
# isinstance()           -> Object belongs to class
# issubclass()           -> Class inheritance check
# super()                -> Call parent method
# dir()                  -> List attributes
# hasattr()              -> Check existence
# getattr()              -> Safe attribute access
# callable()             -> Is object/method callable
# type()                 -> Object type
# ------------------------------------------------------------





class A:
	def work(self): return "A working"
class B(A):
	def work(self): return "B working"
class C(A):
	def work(self): return "C working"
# cls=[A(),B(),C()]
# for obj in cls:print(obj.work())




class EMP:
	def caculate_salary(self):
		#pass 
		return 0
class FTEMP(EMP):
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def caculate_salary(self):
		return self.salary
class CTEMP(EMP):
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def caculate_salary(self):
		return self.salary
class PTEMP(EMP):
	def __init__(self,name,rate,hours):
		self.name=name
		self.rate=rate
		self.hours=hours
		self.salary=self.rate*self.hours
	def caculate_salary(self):
		return self.salary

# employees = [
#     FTEMP("John", 50000),
#     PTEMP("Alice", 20, 80),
#     CTEMP("Bob", 40000)
# ]

# for emp in employees:
# 	print(type(emp).__name__,emp.caculate_salary())



from abc import ABC, abstractmethod
class EMP(ABC):
	@abstractmethod
	def caculate_salary(self):
		#pass 
		return 0
class FTEMP(EMP):
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def caculate_salary(self):
		return self.salary
class CTEMP(EMP):
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def caculate_salary(self):
		return self.salary
class PTEMP(EMP):
	def __init__(self,name,rate,hours):
		self.name=name
		self.rate=rate
		self.hours=hours
		self.salary=self.rate*self.hours
	def caculate_salary(self):
		return self.salary

# employees = [
#     FTEMP("John", 50000),
#     PTEMP("Alice", 20, 80),
#     CTEMP("Bob", 40000)
# ]

# for emp in employees:
# 	print(type(emp).__name__,emp.caculate_salary())



from abc import ABC, abstractmethod
class Student(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def get_result(self):pass
    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age})"
class SchoolStudent(Student):
	def get_result(self):pass
class CollegeStudent(Student):pass
# ss=SchoolStudent("Ravi", 18)
# print(ss)
# s=Student("Ravi", 18)


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, driver_name):
        self.vehicle_id = vehicle_id
        self.driver_name = driver_name
        self.__ride_history = []

    @abstractmethod
    def calculate_fare(self, distance):pass

    @abstractmethod
    def display_details(self):pass

    def add_ride(self, distance, fare):
        self.__ride_history.append({
            "distance": distance,
            "fare": fare
        })

    def view_ride_history(self):
        if not self.__ride_history:
            print("No rides found.")
            return

        for i, ride in enumerate(self.__ride_history, start=1):
            print(f"Ride {i}: {ride['distance']} KM - ₹{ride['fare']}")

class Car(Vehicle):
    BASE_FARE = 50
    PER_KM = 12
    def calculate_fare(self, distance):
        return self.BASE_FARE + (distance * self.PER_KM)
    def display_details(self):
        print(f"Car | ID: {self.vehicle_id} | Driver: {self.driver_name}")

class Bike(Vehicle):
    BASE_FARE = 20
    PER_KM = 8
    def calculate_fare(self, distance):
        return self.BASE_FARE + (distance * self.PER_KM)
    def display_details(self):
        print(f"Bike | ID: {self.vehicle_id} | Driver: {self.driver_name}")

class Auto(Vehicle):
    BASE_FARE = 30
    PER_KM = 10
    def calculate_fare(self, distance):
        return self.BASE_FARE + (distance * self.PER_KM)
    def display_details(self):
        print(f"Auto | ID: {self.vehicle_id} | Driver: {self.driver_name}")

vehicles = [
    Car("C101", "Rahul"),
    Bike("B101", "Kiran"),
    Auto("A101", "Ravi")
]

while True:
    print("\n1. Book Ride")
    print("2. View Vehicle Details")
    print("3. View Ride History")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print("\n1. Car")
        print("2. Bike")
        print("3. Auto")

        vehicle_choice = int(input("Select Vehicle: "))
        distance = float(input("Enter Distance (KM): "))

        vehicle = vehicles[vehicle_choice - 1]

        fare = vehicle.calculate_fare(distance)
        vehicle.add_ride(distance, fare)

        print("\nRide Booked Successfully")
        vehicle.display_details()
        print(f"Distance: {distance} KM")
        print(f"Fare: ₹{fare}")

    elif choice == "2":
        for vehicle in vehicles:
            vehicle.display_details()

    elif choice == "3":
        print("\n1. Car")
        print("2. Bike")
        print("3. Auto")

        vehicle_choice = int(input("Select Vehicle: "))
        vehicles[vehicle_choice - 1].view_ride_history()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")