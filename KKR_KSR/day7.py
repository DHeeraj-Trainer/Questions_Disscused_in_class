class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def display(self):
        return f"{self.brand} {self.model} {self.year}"



# car1=Car("Benz","Classic",2003)
# print(car1.display())

#INSTANCE METODS:ACCESSER AND MUTATOR METHODS
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def get_brand(self):#Accessor Method
        return self.brand
    def set_brand(self,new_brand):#mutataor Method
        self.brand=new_brand
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year

    def display(self):
        return f"{self.brand} {self.model} {self.year}"

# car1=Car("Benz","Classic",2003)
# print(car1.get_brand())
# print(car1.get_model())
# print(car1.get_year())
# car1.set_brand("BMW")
# print(car1.get_brand())


class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year


# car1=Car("Benz","Classic",2003)
# print(car1.brand)


class Car:

    total_cars=0#class Varible

    def __init__(self,brand,model,year):
        self.brand=brand#Instance varibles
        self.model=model#Instance varibles
        self.year=year#Instance varibles

        Car.total_cars += 1
    #classmethod
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


    def display(self):
         return f"{self.brand} {self.model} {self.year} "

# print(f"Total Cars Created before:{Car.total_cars}")#class Name

# car1=Car("Benz","Classic",2003)
# car2=Car("BMW","X9",2015)
# car3=Car("THAR","ROX",2024)
# car3.total_cars=5
# print(f"Total Cars Created after :{Car.total_cars}")#class Name

# print(f"Total Cars Created after :{car3.total_cars}")#through Object
# print(car1.get_total_cars())


# #static Methods
# class Maths:
#     #static Method
#     @staticmethod
#     def add_numbers(a,b):
#         return a+b

# #calling a static method
# print(Maths.add_numbers(5,10))


# Class Varible
# Instance Varible 
# Instance Method-Accessor Method & mutataor Method
# Class Method
# staticmethod

class Shopping_Cart:
    
    carts_accesd=0

    def initialze_cart(self):
        self.items=[]
    
    def add_item(self,item):
        self.items.append(item)
        print(f"{item} add to the cart.")

    #mutataor Method
    # def set_list(self,new_value):
    #     if new_structure:
    #         self.items.append()

    @classmethod
    def count_cart(cls):
        print(f"The carts COunt: {cls.carts_accesd}")
    def count_items(self,item):
            print(f"{item} has repated {self.items.count(item)}")

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from cart.")
        else:print(f"{item} is not there in cart.")
    
    def view_cart(self):
        if self.items:
            print("Items in your Cart :",",".join(self.items))
            Shopping_Cart.carts_accesd += 1
        else:print("Cart is Empty.")


# cart=Shopping_Cart()
# cart.initialze_cart()
# cart.add_item("Apples")
# cart.add_item("Apples")
# cart.add_item("Apples")
# cart.count_items("Apples")
# cart.add_item("KIWI")
# cart.view_cart()
# # cart.set_list()
# cart.remove_item("Orange")
# cart.remove_item("Apples")
# cart.view_cart()
# print(f"No of time cart has viewed : {Shopping_Cart.carts_accesd}")
# cart.count_cart()


# spl /Dunder methods:__init__,__str__
class Student:
	collage_name="KITS"
	stu_count=0
	def __init__(self,name="",age=0,sec=None):
		self.name=name
		self.age=age
		self.sec=sec
		self.stu_count_incre()
		print(f"{self} is created")
	# def get_details(self):
	# 	return f"name: {self.name} Age: {self.age} SEC: {self.sec}"
	@classmethod
	def change_collage_name(cls,new_name):
		cls.collage_name=new_name
	@classmethod
	def stu_count_incre(cls):
		cls.stu_count+=1
	def __str__(self):        
		return f"name: {self.name} Age: {self.age} SEC: {self.sec} Collage: {self.collage_name}"
	@staticmethod
	def is_adult(age):
		return age>=18
# s1=Student("Dheeraj",16,10)
# # print(s1.get_details())
# s1.name="Dheeraj Kumar"
# Student.change_collage_name("KITS College")
# print(s1)
# print("count:",Student.stu_count)
# s2=Student("Rohit",17,11)
# print(s2)
# print("count:",Student.stu_count)
# students=[s1,s2]
# for stu in students:
#     print(Student.is_adult(stu.age))

# Encapsulation means:

# "Wrapping data (variables) and methods together inside a class and controlling access to the data."

# Bank Account

# Balance should not be changed directly by anyone.
# Users should use methods like deposit() and withdraw().


# Types of Variables in Python OOP

class Student:
    def __init__(self):
        self.name = "Ravi"  #------>Public Variable
# s=Student()
# print(s.name)
# s.name="B Ravi"

# Accessible/Modify inside class
# Accessible/Modify  outside class
# Can be accessed from anywhere.



class Student:
    def __init__(self):
        self.name = "Ravi"  #------>Public Variable
        self._age = 18 #------> Protected Variable
# s=Student()
# print(s.name)
# s.name="B Ravi"
# print(s._age)
# s._age=20
# print(s._age)
# Accessible/Modify inside class


# Private Variables
# Convention:__variable
# Example:
class Student:
    def __init__(self):
        self.__age = 18 #------> Private Variable
    def modify_age(self,new_age):
        if new_age >= 18:
            self.__age = new_age
        else:
            print("Age must be 18 or above.")
    def get_age(self):
            return f"Student Age: {self.__age}"
#Access:
# s = Student()
# print(s._age)
# s._age = 20 #Modifying the protected variable
# print(s._age)
# s.modify_age(25) #Using the method to modify the protected variable
# print(s.get_age()) #Using the method to access the protected variable



# class Account:
# 	def __init__(self,pin,name,num):
# 		self.__pin=pin
# 		self._num=num
# 		self.name=name
# # a1=Account("1234","Raju",123456789)
# # print(a1.name)
# # print(a1._num)
# # # print(a1.__pin)
# # print(a1._Account__pin) #objectname._Classname__variblename
# # #python:# self.__pin   to self._classname__pin``

#  Variable Type     Inside Class  Outside Class  Child Class 
#  ----------------  ------------  -------------  ----------- 
#  Public            ✅             ✅              ✅           
#  Protected (_var)  ✅             ⚠️ Possible    ✅           
#  Private (__var)   ✅             ❌              ❌           



# Inheritance allows one class to acquire the properties and methods of another class.
# The existing class is called:
# Parent Class / Base Class / Super Class
# The new class is called:
# Child Class / Derived Class / Sub Class

# 		 Human(name,eat(),sleep())
# 		   |
#               |    |          |
#     (work()) Emp    student  parent(taking_care()) 
#                     (study())


class Human(object):
	def __init__(self):
		self.name="Human"
	def eat(self):
		return "eating"
	def sleep(self):
		return "Zzzzzz"
class Emp(Human):
	def work(self):return "Working"
class Student(Human):
	def study(self):return "Studying"
class Parent(Human):
	def care(self):return "Careing"
     
print(Emp.__mro__)
# emp=Emp()
# emp.name="Dheeraj"
# print(emp.age)
# print(emp.eat())
# print(emp.work())
# print(emp.study())


class Father:
    def __init__(self):
          self.money = 2000
          self.car = "BMW"
          print("Father Class Constructor")
    def disp(self):
            print("Father Class Instance Method:", self.money,self.car)
class Son(Father):
     def __init__(self):
        super().__init__()#Calling the parent class constructor
        self.money = 5000
        
        print("Son Class Constructor")
        # super().__init__()#Calling the parent class constructor
     def disp(self):
          super().disp()#Calling the parent class method
          print("Son Class Instance Method:", self.money)
# s = Son()
# # s.disp()
# print(Son.__mro__)
# print(Father.mro())


