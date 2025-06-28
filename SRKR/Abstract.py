'''
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod:
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car STarted"
    
    def stop(self):
        return "Car Stoped"


class Bike(Vehicle):
    def start(self):
        return "Bike Started"
    
    def stop(self):
        return "Bike Stooped"

vehicles=[Car(),Bike()]
for vehicle in vehicles:
    print(vehicle.start())
    print(vehicle.stop())


from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    pass
bike=Bike()
print(bike.start())

class Vehicle:
    def start(self):
        pass

class Bike(Vehicle):
    pass

bike=Bike()
print(bike.start())
'''

### Problem Statement: Payment Gateway System

You are tasked with designing a payment gateway system that supports 
multiple payment methods. Each payment method must follow a common 
interface for processing transactions. 

The system should:

1. Define a base class `Payment` with abstract methods:
   - `initiate_payment(amount)`: Initiates the payment for the specified amount.
   - `validate_payment()`: Validates the payment.

2. Implement two derived classes:
   - `CreditCard`: Represents payments made using a credit card.
   - `PayPal`: Represents payments made using PayPal.

3. For each payment method:
   - Customize the `initiate_payment()` method to include details about the 
        payment type.
   - Customize the `validate_payment()` method to simulate payment validation.

4. Create a function `process_payment(payment_method, amount)` that:
   - Accepts an object of type `Payment` (e.g., `CreditCard` or `PayPal`) and 
        the payment amount.
   - Prints the payment initiation and validation messages.

5. Test the system with both `CreditCard` and `PayPal` payment methods for 
        different amounts.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass

    @abstractmethod
    def validate_payment(self):
        pass

class CreditCard(Payment):
    def initiate_payment(self, amount):
        return f"Initiating credit card payment of ${amount:.2f}"

    def validate_payment(self):
        return "Credit card payment validated successfully."

class PayPal(Payment):
    def initiate_payment(self, amount):
        return f"Initiating PayPal payment of ${amount:.2f}"

    def validate_payment(self):
        return "PayPal payment validated successfully."


def process_payment(payment_method, amount):
    print(payment_method.initiate_payment(amount))
    print(payment_method.validate_payment())

credit_card = CreditCard()
paypal = PayPal()

print("Using Credit Card:")
process_payment(credit_card, 150.75)

print("\nUsing PayPal:")
process_payment(paypal, 200.50)
