# try:
#     num=int(input("Enter the num: "))
#     res=10/num
#     print(res)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("Invalid Input! enter integer inputs only")



# class UnderAgeError(Exception):
#     pass

# try:
#     age=int(input("Enter the your age"))
#     if age<18:
#         raise UnderAgeError("Your must be at lesat 18 years old")
#     else:print("access Granted") 
# except UnderAgeError as e:
#     print("Access Denied :",e)
# # except ValueError:
# #     print("Invalid Input,Enter only integers")


# lis1=[1,2,3,4,5,5]
# try:
#     index=int(input("ENter the index: "))
# except ValueError:
#     print("Enter valid integer")
# except IndexError:
#     print("Index out of range")
# else:
#     print("",lis1[index])




# def calc(a,b,op):
#     try:
#         if op=='+':
#             return a+b
#         elif op=='-':
#             return a-b
#         elif op=="/":
#             return a/b
#         elif op=="*":
#             return a*b
#         else:print("Valid Input")
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# try :
#     x=int(input("Enter the num1: "))
#     y=int(input("Enter the num2: "))
#     Op=input("ENter the Operator(+,-,*,/): ")
# except ValueError:
#     print("Invalid Number")
# else:print(calc(x,y,Op))



# Demonstrate nested try-except blocks. Divide two numbers inside a nested block and handle all types of errors.


# try :
#     a=int(input("ENter a Number: "))
#     b=int(input("ENter a Number: "))
#     try:
#         res=a/b
#     except ZeroDivisionError:
#         print("Zero cant be divided")
#     else:
#         print(res)
# except ValueError:
#     print("ENter valid Value")



import numpy as np

# 1. array() function
# Creates a NumPy array from a regular Python list or tuple.
arr1 = np.array([1, 2, 3, 4, 5])
print("array():", arr1)

# 2. linspace() function
# Returns evenly spaced numbers over a specified interval.
# Arguments: start, stop, number of samples
arr2 = np.linspace(0, 10, 5)
print("linspace():", arr2)

# 3. logspace() function
# Returns numbers spaced evenly on a log scale.
# Arguments: start exponent, stop exponent, number of samples
# 10^1 to 10^3 (i.e., 10 to 1000)
arr3 = np.logspace(1, 3, 3)
print("logspace():", arr3)

# 4. arange() function
# Returns evenly spaced values within a given interval.
# Arguments: start, stop (exclusive), step
arr4 = np.arange(1, 10, 2)
print("arange():", arr4)

# 5. zeros() function
# Returns a new array of given shape and type, filled with zeros.
# Argument: tuple for shape
arr5 = np.zeros((2, 3))
print("zeros():\n", arr5)

# 6. ones() function
# Returns a new array of given shape and type, filled with ones.
# Argument: tuple for shape
arr6 = np.ones((2, 3))
print("ones():\n", arr6)
