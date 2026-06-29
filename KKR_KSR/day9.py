# try:
#     #code
# except:
#     #handling code

# try: 
#     pizzas=int(input("Pizzas:"))
#     frnds=int(input("FRNDS:"))
#     print(pizzas/frnds)
# except Exception as e:
#     print("Error",e)
# except ZeroDivisionError:
    # print("Cannot divide pizzas among zero friends")
# except ValueError:
    # print("Enter the numbers")

# try:
#     pass

# except Error1:
#     pass

# except Error2:
#     pass
# except (Error1, Error2):  
# Generic Exception (Exception)

# Used when you want to 
# catch all standard exceptions.
# try:
#     print(5+6)
#     print(5/0)
# except Exception as e:
#     print("Error",Exception,e)
# # print(5/0)

# else & finally block:

# try: 
#     pizzas=int(input("Pizzas:"))
#     frnds=int(input("FRNDS:"))
#     res=(pizzas/frnds)
# except Exception as e:
#     print("Error",e)
# else:print(res)
# finally:print("Done!!!!!!!!")



# raising error(raise)
# try:
#     age=int(input("Enter age:"))
#     if age<18:
#         # print("Not eligible")
#         raise ValueError("Not eligible")
# except Exception as e:print("Error",e)
# else:print("Eligible")
# finally:print("Done")

# try :
#     amount=int(input("amount:"))
#     if amount<=100:
#         raise Exception("Min order is 100")
# except Exception as e:print("Error:",e)
# else:print("Order Done")
# Creating Custom Exceptions
# Custom exceptions help 
# create business-specific errors.
# class MinOrderException(Exception):
#     pass
# try :
#     amount=int(input("amount:"))
#     if amount<=100:
#         raise MinOrderException("Min order is 100")
# except Exception as e:print("Error:",e)
# else:print("Order Done")


# def add():return 5
# print(add(5))



class InvalidPinError(Exception):pass
class InsufficientFundsError(Exception):pass
balance=10000
pin=1234
try:
    entered_pin=int(input("PIN:"))
    amount=int(input("Enter amount to withdraw:"))
    if pin!=entered_pin:
        raise InvalidPinError("Invalid PIN")
    if amount>balance:
        raise InsufficientFundsError("Insufficient Funds")
    balance-=amount
    print("Done,Final balance:",balance)
except Exception as e:
    print("Error:",e)