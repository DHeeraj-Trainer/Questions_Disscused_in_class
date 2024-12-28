# Scenario: ATM Withdrawal System
# Problem:
# Write a program to simulate an ATM withdrawal system.
# The user has an initial account balance of $10,000.
# The program should:
# 1. Ask the user how much they want to withdraw.
# 2. Check if the amount is a multiple of 100.
# 3. Ensure the withdrawal amount does not exceed the account balance.
# 4. Deduct the amount if valid and display the remaining balance.
# 5. Allow multiple withdrawals until the user decides to exit or the balance is insufficient.

# balance = 10000
# while True:
#     print("\n--- ATM Withdrawal System ---")
#     print(f"Current Balance: ${balance}")
#     withdrawal = int(input("Enter the amount to withdraw (multiple of 100): "))
#     if withdrawal % 100 != 0:
#         print("Invalid amount! Please enter a multiple of 100.")
#     elif withdrawal > balance:
#         print("Insufficient balance!")
#     else:
#         balance -= withdrawal
#         print(f"Withdrawal successful! Remaining balance: ${balance}")
#     if balance == 0:
#         print("Your balance is zero. No further withdrawals possible.")
#         break
#     another = input("Do you want to make another withdrawal? (yes/no): ").lower()
#     if another != "yes":
#         print("Thank you for using the ATM. Goodbye!")
#         break



# Problem: We will enhance the ATM withdrawal system by adding the following new features:
# 1. PIN Validation: Before the user can perform any transaction, they must enter a valid PIN.
# 2. Deposit Functionality: Users can deposit money into their account in addition to withdrawing.
# 3. Transaction History: Keep track of withdrawals and deposits and display the transaction history.
# 4. Balance Inquiry: Let users check their current balance without making a withdrawal.
# 5. Exit Option: Allow the user to exit the system anytime.


# balance = 10000
# pin = "1234"
# transaction_history = []

# def check_pin():
#     entered_pin = input("Enter your PIN: ")
#     if entered_pin != pin:
#         print("Incorrect PIN! Please try again.")
#         return False
#     return True

# def display_transaction_history():
#     if transaction_history:
#         print("\n--- Transaction History ---")
#         for transaction in transaction_history:
#             print(transaction)
#     else:
#         print("No transactions yet.")

# while True:
#     print("\n--- ATM System ---")

#     if not check_pin():
#         continue

#     print("\nATM Menu:")
#     print("1. Withdraw")
#     print("2. Deposit")
#     print("3. Balance Inquiry")
#     print("4. View Transaction History")
#     print("5. Exit")

#     choice = input("Choose an option (1/2/3/4/5): ")

#     if choice == "1":
#         print(f"Current Balance: ${balance}")
#         withdrawal = int(input("Enter the amount to withdraw (multiple of 100): "))
        
#         if withdrawal % 100 != 0:
#             print("Invalid amount! Please enter a multiple of 100.")
#         elif withdrawal > balance:
#             print("Insufficient balance!")
#         else:
#             balance -= withdrawal
#             transaction_history.append(f"Withdrawal: ${withdrawal}")
#             print(f"Withdrawal successful! Remaining balance: ${balance}")
    
#     elif choice == "2":
#         deposit = int(input("Enter the amount to deposit: "))
#         balance += deposit
#         transaction_history.append(f"Deposit: ${deposit}")
#         print(f"Deposit successful! New balance: ${balance}")

#     elif choice == "3":
#         print(f"Your current balance is: ${balance}")
    
#     elif choice == "4":
#         display_transaction_history()

#     elif choice == "5":
#         print("Thank you for using the ATM. Goodbye!")
#         break
    
#     else:
#         print("Invalid choice! Please try again.")


# Scenario: Pizza Shop Ordering System
# Problem:
# Write a program to simulate a pizza shop ordering system.
# • The shop offers three sizes of pizza: Small ($10), Medium ($15), and Large ($20).
# • Customers can also add extra toppings:
# • Cheese ($2)
# Pepperoni ($3)
# • The program calculates the total cost of the order 
# and allows customers to place multiple orders until they decide to exit.




# Level 2: Pizza Shop Ordering System with Multiple Pizzas and Delivery Option
# Problem:
# Expand the pizza shop system to include the following features:
# 1. The customer can order multiple pizzas in one order.
# 2. Add a delivery option:
# Delivery charge is $5 for orders under $50
# • Free delivery for orders of $50 or more.
# 3. Display the final receipt with a breakdown of all pizzas ordered, toppings, and the delivery charge.



# while True:
#     print("\n--- Welcome to Pizza Shop ---")
#     order = []
#     total_cost = 0

#     while True:
#         print("\nChoose your pizza size:")
#         print("1. Small Pizza ($10)")
#         print("2. Medium Pizza ($15)")
#         print("3. Large Pizza ($20)")

#         size = int(input("Choose your pizza size (1/2/3): "))
#         if size == 1:
#             pizza_cost = 10
#             pizza_size = "Small Pizza"
#         elif size == 2:
#             pizza_cost = 15
#             pizza_size = "Medium Pizza"
#         elif size == 3:
#             pizza_cost = 20
#             pizza_size = "Large Pizza"
#         else:
#             print("Invalid choice! Please try again.")
#             continue

#         print("\nDo you want to add extra toppings?")
#         print("1. Cheese ($2)")
#         print("2. Pepperoni ($3)")
#         print("3. Both Cheese and Pepperoni ($5)")
#         print("4. No extra toppings")

#         toppings = int(input("Choose your option (1/2/3/4): "))
#         if toppings == 1:
#             topping_cost = 2
#             topping_desc = "Cheese"
#         elif toppings == 2:
#             topping_cost = 3
#             topping_desc = "Pepperoni"
#         elif toppings == 3:
#             topping_cost = 5
#             topping_desc = "Cheese and Pepperoni"
#         elif toppings == 4:
#             topping_cost = 0
#             topping_desc = "No Toppings"
#         else:
#             print("Invalid choice! No toppings added.")
#             topping_cost = 0
#             topping_desc = "No Toppings"

#         pizza_total = pizza_cost + topping_cost
#         total_cost += pizza_total

#         order.append((pizza_size, topping_desc, pizza_total))
#         print(f"\n{pizza_size} with {topping_desc} added to the order. Cost: ${pizza_total}")

#         another_pizza = input("\nDo you want to add another pizza? (yes/no): ").lower()
#         if another_pizza != "yes":
#             break

#     print("\nDo you want the order delivered?")
#     delivery = input("Enter 'yes' for delivery or 'no' for pickup: ").lower()
#     if delivery == "yes":
#         if total_cost < 50:
#             delivery_charge = 5
#             print("Delivery charge: $5 (Orders under $50)")
#         else:
#             delivery_charge = 0
#             print("Free delivery (Orders of $50 or more)")
#     else:
#         delivery_charge = 0
#         print("No delivery charge (Pickup)")

#     final_total = total_cost + delivery_charge

#     print("\n--- Final Receipt ---")
#     for pizza, toppings, cost in order:
#         print(f"{pizza} with {toppings} - ${cost}")
    
#     if delivery_charge > 0:
#         print(f"Delivery Charge: ${delivery_charge}")
    
#     print(f"Total Amount: ${final_total}")
    
#     another_order = input("\nDo you want to place another order? (yes/no): ").lower()
#     if another_order != "yes":
#         print("Thank you for ordering from Pizza Shop! Goodbye!")
#         break








# a=[1,2,35,6,8,6,5,8,99,0,66]
# # append-5,insert-(2,85),remove-2
# # pop ,pop(n)-0
# # index-85,count-2,sort,reverse,slice-(2-3),ext-slice,
# # append-sumof list values,add the max value again
# # find the final length,and index of 0,max and min value of list

# a.append(5)
# a.insert(2,85)
# a.remove(2)
# a.pop()
# a.pop(0)
# print("index of 85:",a.index(85))
# print("COunt of 2:",a.count(2))
# print("list before sort: ",a)
# a.sort()
# print("list after sort: ",a)
# a.reverse()
# print("list after reverse: ",a)
# b=a[2:3]
# a.extend(b)
# print("list after extend: ",a)
# a.append(sum(a))
# print("list after sum-append: ",a)
# a.append(max(a))
# print("list after max append: ",a)
# print("Length Of List a :",len(a))
# print("Index of 0 :",a.index(0))
# print("max Of List a :",max(a))
# print("min Of List a :",min(a))


# list1=[-9,8,9,8,6,5,3,823,9333,522,-93,85.3,85,69]
# find out the count of even numbers and odd numbers and print even list and odd numbers list 
# even=[num for num in list1 if num%2==0 ]
# odd=[i for i in list1 if i%2 !=0]
# print(even,"Length of even :",len(even))
# print(odd,"Length of odd :",len(odd))





# list=[1,5,8,9,6,3,7,52,69,55,1,4,5,2,3,6,9,555,125,145]
# 1.Find the Second Largest Number in a List
# 2.Calculate the Average of Numbers in a Given List
# 3.Print Sum of Negative Numbers, Positive Even Numbers 
# 	and Positive Odd numbers in a List Print Largest Even 
# 	and Largest Odd Number in a List
# 4.Get the Position of Max Value in a List
# 5.Add Number to each Element in a List
# 	gven_lst = [2,4,6,8,10]
# 	numbr = 5
# 6.get the First Element of each list in a List wirte using loops
#  	gvn__lst = [[1, 2], [3, 4]]




# Create a Python program called Shopping List Manager 
# that performs the following functions:

# 	Allows the user to add items to a shopping list.
# 	Allows the user to remove specific items from the list.
# 	Provides an option to sort the items in the shopping 
# 	list alphabetically.
# 	Displays the final list of items after the user 
# 	finishes their operations.
# 	The program should be interactive and user-friendly, 
# 	prompting the user for actions and providing clear outputs.

# Sample Input and Output:
# Consider the following sequence of operations performed by the user:
# 	Add the items: "Milk", "Eggs", "Bread", "Butter", "Apples".
# 	Remove the item: "Butter".
# 	Sort the list alphabetically.
# 	Display the final list.



def display_menu():
    print("\n____________Welcome to Mart___________")
    print("1.Add item")
    print("2.Remove Item")
    print("3.Sort List")
    print("4.Display the List")
    print("5.Exit")

def add_item(shop_list):
    item=input("Enter the item u want add :")
    shop_list.append(item)
    print(f"{item}.Has been added to list.")
    print(shop_list)

def remove_item(shop_list):
    item=input("Enter the item u want to remove :")
    if item in shop_list:
        shop_list.remove(item)
        print(f"{item} has been removed")
        print(shop_list)
    else:
        print(f"{item} is not in the list")
def sort_list(shop_list):
    shop_list.sort()
    print("Sorted List :",shop_list)
def display_finallist(shop_list):
    if shop_list:
        print("\n Final Shopping List")
        for item in shop_list:
            print(item)
    else:print("No items in List")

def list_manager():
    shop_list=[]
    while True:
        display_menu()
        choice=input("Enter Your Choice :")
        if choice=='1':
            add_item(shop_list)
        elif choice=='2':
            remove_item(shop_list)
        elif choice=='3':
            sort_list(shop_list)
        elif choice=='4':
            display_finallist(shop_list)
        elif choice=='5':
            print("Thank You")
            break
        else:
            print("Invalid CHoice,Plese Try Again")
        

list_manager()