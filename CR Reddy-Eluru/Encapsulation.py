# Encapsulation
# write BankAccount class with a private attributes:
#     __account_number:read-only
#     _balance:read and write property 


# create an account with __account_number of 2341244 and intial balance 
# is 500


# display this values
# after this add the 100 rs to balance 
'''

class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    @property
    def account_number(self):
        return f"Account Number :{self.__account_number}"
    @property
    def balance(self):
        return f"Balance Amount:{self.__balance}"
    @balance.setter
    def balance(self,Amount):
        if Amount<0:
            # return  "Amount should be above 0"
            raise ValueError ("Amount should be above 0")
        self.__balance+=Amount
    # def set_balance(self,Amount):
    #     if Amount<0:
    #         # return  "Amount should be above 0"
    #         raise ValueError ("Amount should be above 0")
    #     self.__balance=Amount

account=BankAccount(1234,500)
print(account.account_number)
print(account.balance)
# account.set_balance(100)
account.balance = 600
print(account.account_number)
print(account.balance)




# Student class 
# private attributes-Grade
# add setter and getter setter for grades
# the validation grade should be 0 to 100
# else it should raise an ValueError  
class Student:
    def __init__(self):
        self.__Grade=0
    @property
    def grade(self):
        return f"Grade : {self.__Grade}"
    @grade.setter
    def grade(self,value):
        if not (0<=value<=100):
            raise ValueError ("Grade Must Be in 0 to 100")
        self.__Grade=value
    
student=Student()
student.grade=85
print(student.grade)
# student.grade=155
# print(student.grade)
try :
    student.grade=150
except ValueError as v:
    print(v)
'''
# Rectangle class 
# private attributes:  length and width
# get and set methods for length and width (should be postive only)
# write a method calculate the area 


class Rectangle:
    def __init__(self):
        self.__length=0
        self.__width=0
    @property
    def length(self):
        return f"Length:{self.__length}"
    @length.setter
    def length(self,value):
        if value<=0:
            raise ValueError ("Length must be above 0")
        self.__length=value
    @property
    def width(self):
        return f"Width: {self.__width}"
    @width.setter
    def width(self,value):
        if value<=0:
            raise ValueError ("Length must be above 0")
        self.__width=value
    @property
    def area(self):
        return f"Area: {self.__length*self.__width}"
rectangle=Rectangle()
rectangle.length=15
rectangle.width=55
print(rectangle.length)
print(rectangle.width)
print(rectangle.area)

# rectangle=Rectangle()
# rectangle.length_width(12,55)
# print(rectangle.length_width)

