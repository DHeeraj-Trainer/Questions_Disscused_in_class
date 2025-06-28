# https://github.com/DHeeraj-Trainer/Questions_Disscused_in_class
'''
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def display(self):
        return f"{self.brand} {self.model} {self.year}"



car1=Car("Benz","Classic",2003)
print(car1.display())

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

car1=Car("Benz","Classic",2003)
print(car1.get_brand())
print(car1.get_model())
print(car1.get_year())
car1.set_brand("BMW")
print(car1.get_brand())


class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year


car1=Car("Benz","Classic",2003)
print(car1.brand)


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

print(f"Total Cars Created before:{Car.total_cars}")#class Name

car1=Car("Benz","Classic",2003)
car2=Car("BMW","X9",2015)
car3=Car("THAR","ROX",2024)
car3.total_cars=5
print(f"Total Cars Created after :{Car.total_cars}")#class Name

print(f"Total Cars Created after :{car3.total_cars}")#through Object
print(car1.get_total_cars())


#static Methods
class Maths:
    #static Method
    @staticmethod
    def add_numbers(a,b):
        return a+b

#calling a static method
print(Maths.add_numbers(5,10))


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


cart=Shopping_Cart()
cart.initialze_cart()
cart.add_item("Apples")
cart.add_item("Apples")
cart.add_item("Apples")
cart.count_items("Apples")
cart.add_item("KIWI")
cart.view_cart()
# cart.set_list()
cart.remove_item("Orange")
cart.remove_item("Apples")
cart.view_cart()
print(f"No of time cart has viewed : {Shopping_Cart.carts_accesd}")
cart.count_cart()



# Single Inheritance 

#parent Class
class Animal:
    def gen(self):
        return "My class is Animal"
# Child Class
class Dog(Animal):
    def speak(self):
        return 'my sound: Woof'

Genric_animal=Animal()
dog=Dog()
# print("child object to child method:",dog.speak(),"child object to parent method:",dog.gen())
# print("Parent object to parent method:",Genric_animal.gen(),"Parent object to child method:",Genric_animal.speak())




class Car:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        return f"Parrent :{self.brand}"
class Benz(Car):
    def __init__(self,brand,model,year):
        self.brand='Benz'
        self.model=model
        self.year=year    
    def display(self):
        return f"CHild:{self.brand} {self.model} {self.year}"
car1=Car("Benz2")
Benz1=Benz("Benz1","Classic1",2020)
print(car1.display())
print(Benz1.display())


#Multi-level Inheritance 

class Vehicle:#parent class
    def describe1(self):
        return "I am in Vehical Class"
class Car(Vehicle): #child Class
    def describe2(self):
        return "I am in Car Class"
class Ele_car(Car): #grandchild class
        def describe3(self):
            return "I am In ELE_Car Class"

Ele_car1=Ele_car()
car2=Car()
Vehicle1=Vehicle()
print("child to parent :",car2.describe1())
print("Grand child to parent :",Ele_car1.describe1())
print("Grand child to child  :",Ele_car1.describe2())



#Multiple Inheritance

class P1:
    def greet(self):
        return "Hello, P1"
class P2:
    def greet(self):
        return "Hello, P2"
class C1(P1,P2):
    def greet(self):
        return super().greet()
        # return "Hello ,C1"
        # return P2.greet(self)

class GS(C1):
    def greet(self):
        # return P1.greet(self)
        # return P2.greet(self)
        return C1.greet(self)

child=C1()
print(child.greet())
Gs=GS()
print(Gs.greet())




Part 1: Single Inheritance
Problem Statement:
You are tasked with designing a simple system to manage employees. Create a base class Employee that stores basic details such as name and ID. Extend this class with a derived class Manager to include the department the manager oversees. Demonstrate how the Manager class can reuse and extend the functionality of the Employee class.

Part 2: Multilevel Inheritance
Problem Statement:
Building upon the Manager class, create another class TeamLead that represents a manager who also leads a team. Extend the Manager class to include the size of the team. Demonstrate how the TeamLead class can inherit functionality from both Manager and Employee classes.

Part 3: Hierarchical Inheritance
Problem Statement:
In your employee management system, you need to manage both managers and developers. Extend the Employee class to create a Developer class that includes the programming language the developer specializes in. Demonstrate how the Developer class and Manager class can inherit from the same parent class (Employee), forming a hierarchical structure.

Part 4: Multiple Inheritance
Problem Statement:
You need to manage interns in your system, who might have characteristics of both developers and managers. Create a class Intern that inherits from both Developer and Manager. Add a stipend attribute specific to interns and demonstrate how Intern can combine the features of both parent classes.

# Part 1: Single Inheritance

class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id

    def display_details(self):
        return f"Name : {self.name}, emp_id: {self.emp_id}"

class Manager(Employee):
    def __init__(self,name,emp_id,department):
    # def deppt(self,department)
        super().__init__(name,emp_id)
        self.department=department

    def display_details(self):
        return f"{super().display_details()},Department:{self.department}"
        return f"Name : {emp.name}, emp_id: {emp.emp_id} ,Department:{self.department}"

# emp=Employee("Dheeraj","M001")
# manager=Manager("Dheeraj","M001","Trainer & HR")
# print(manager.display_details())

# Part 2: Multilevel Inheritance

class TeamLead(Manager):
    def __init__(self,name,emp_id,department,team_size):
        super().__init__(name,emp_id,department)
        self.team_size=team_size
    def display_details(self):
        return f"{super().display_details()},Team Size: {self.team_size}"


# Team_Lead=TeamLead("Sai","TL001","ENg",23)
# print(Team_Lead.display_details())



#Part 3: Hierarchical Inheritance
class Developer(Employee):
    def __init__(self,name,emp_id,programming_lang):
        Employee.__init__(self,name,emp_id)
        self.programming_lang=programming_lang
    def display_details(self):
        return f"{Employee.display_details(self)},programming_lang:{self.programming_lang}"


developer=Developer("Rajesh","D0001","Python")
print(developer.display_details())




# Part 4: Multiple Inheritance

class Intern(Developer,Manager):
    def __init__(self,name,emp_id,programming_lang,department,stipend):
        Developer.__init__(self,name,emp_id,programming_lang)
        self.department=department
        # Department.__init__(self,name,emp_id,Department)
        # self.programming_lang=programming_lang
        self.stipend=stipend
    
    def display_details(self):
        return f"{Developer.display_details(self)},Department:{self.department},Stipend:{self.stipend}"


intern=Intern("Ramesh","I001","Java","IT",10000)
print(intern.display_details())
'''