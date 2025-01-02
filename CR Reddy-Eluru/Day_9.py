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

'''
#statci Methods
class Maths:
    #static Method
    @staticmethod
    def add_numbers(a,b):
        return a+b

print(Maths.add_numbers(5,10))
'''


class Shopping_Cart:
    def initialze_cart(self):
        self.items=[]
    
    def add_item(self,item):
        self.items.append(item)
        print(f"{item} add to the cart.")
    
    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from cart.")
        else:print(f"{item} is not there in cart.")
    
    def view_cart(self):
        if self.items:
            print("Items in your Cart :",",".join(self.items))
        else:print("Cart is Empty.")


cart=Shopping_Cart()
cart.initialze_cart()
cart.add_item("Apples")
cart.add_item("KIWI")
cart.view_cart()
cart.remove_item("Orange")
cart.remove_item("Apples")
cart.view_cart()
'''

