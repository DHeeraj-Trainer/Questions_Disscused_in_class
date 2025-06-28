'''
class Animal:
    def sound(self):
        return "Some Genric animal Sound"
    
class Dog(Animal):
    def sound(self):
        return "Woof Woof"
    
class Cat(Animal):
    def sound(self):
        return "Meow Meow"

animals=[Dog(),Cat(),Animal()]
for animal in animals:
    print(animal.sound())


'''
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must overide this method")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*(self.radius**2)
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5*self.base*self.height

shapes=[
    Circle(7),
    Rectangle(10,5),                                        
    Triangle(6,8)
]
for shape in shapes:
    print(f"{type(shape).__name__} Area:{shape.area():.2f}")