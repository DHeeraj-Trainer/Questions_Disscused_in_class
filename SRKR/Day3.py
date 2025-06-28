# Write a program using only if and else to determine the ticket price for a person based on their age:

# If the person is below 12 years old, the ticket costs $10.
# If the person is between 12 and 60 years old, the ticket costs $15.
# If the person is above 60 years old, the ticket costs $12.
# list_of_ages=[15,65,19,68]

# for i in range(len(list_of_ages)):
# print(i)
# list_of_ages=[15,65,19,68]

# if list_of_ages[i]<=100 and list_of_ages[i]>=1:
#     if list_of_ages[i]>12 and list_of_ages[i]<60:
#         print("the price is $15")
#     else:print("the price is $12")
# else:print("enter the age between 1 to 100")
# for i in range(len(list_of_ages)):
#     print(list_of_ages[i],end=',')

# ages=[10,40,70]
# total_prices=0
# for i in range(len(ages)):
#     if ages[i]<12:
#         print("the amount is 10$")
#         total_prices+=10
#     elif ages[i]>=12 and ages[i]<60:
#         print("the amount is $15")
#         total_prices+=15
#     elif ages[i]>60:
#         print("the amount is $12")
#         total_prices+=12
# print(f"the total prices is: {total_prices}")


# i = 0
# while True:
#     i+=1
#     print(i)
#     if(i == 5):
#         break
# print("Rest of the Code")


# Modify the loan eligibility program to check the eligibility of multiple applicants.
# • Continue taking input until the user decides to stop.
# • For each applicant:
# 	• The person must be at least 21 years old.
# 	• The person must have a monthly income of $25,000 or more.
# Display whether the person is eligible or not.
# while True:
#     print("*******____Loan Eligibility Check_______******")
#     age=int(input("Enter the age :"))
#     salary=int(input("Enter the Salary(in $) :"))
#     if age>21 :
#         if salary>=25000:
#             print("Person is Eligble for loan")
#     else:print("Person is not ELigible for loan")
#     choice=input("Do you want to Continue...? (Yes or No)")
#     if choice=='Yes':continue
#     else:break

# n=int(input("enter the num :"))

# print even numbers
# for i in range(0,n+1):
#     if i%2==0:
#         print(i)
# for i in range(0,n+1,2):
#     print(i)
# print 5 to n  numbers
# for i in range(5,n+1):
#     print(i)
# print multiplication table of a given number
# n=int(input("enter the num :"))
# print("upto 10")
# for i in range(1,11):
#     print(f"{n} x {i} ={n*i}")
# .print multiplication tables upto n
# upto=int(input("Upto which value the table should be  :"))
# print(f"upto {n}")
# for i in range(1,upto+1):
#     print(f"{n} x {i} ={n*i}")
# .sum of even 
# n=int(input("Enter the number :"))
# sum=0
# for i in range(n+1):
#     if i%2==0:
#         sum+=i
# print(sum)
# Reverse the given Number
# n = input() #12345
# a=""
# for i in n:
#     a=i+a 
# print(a)
# count number of digits in a number
# factorial
# n*(n-1).....1
# def fact(n):
#     if n==0:return 1
#     else:return n*fact(n-1)
# n=int(input("Enter a num :"))
# print(f"the {n} fact value is : {fact(n)}")
# check number is pallindrome or not
# def pallindrome():
#     n = input("Enter the Value :") 
#     a=""
#     for i in n:
#         a=i+a 
#     if a==n:print(f"{n} is a pallindrome ")
#     else: print(f"{n} is not a pallindrome ")
# pallindrome()
# .count even and odd numbers present in the list
# list1=[5,8,9,6,3,66,8993,6332,5622,-9]
# even_count=odd_count=0
# for i in list1:
#     if i%2==0:
#         even_count+=1
#     else:odd_count+=1
# print("Even Count: ",even_count,"Odd_count :",odd_count)

# Python Program to check whether the given input is alphabet, number or special character
# Input:  123%t
# output:
# 1-number
# 2-number
# 3-number
# %-spl_char
# t-Alphabet

# str_= input("Enter the String :")
# for i in str_:
#     if '0' <= i <='9' :print(f"{i}- Number")
#     elif 'A'<=i<='Z' or 'a'<=i<='z': print(f"{i}- Alphabet")
#     else:print(f"{i}- Spl_Char")




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



# *
# **
# ***
# ****
# *****
# n=int(input("Enter the num :"))
# for i in range(1,n+1):
#     print('*'*i)
# 1
# 22
# 333
# 4444
# 55555
# n=int(input("Enter the num :"))
# for i in range(1,n+1):
#     print(str(i)*i)
    
#     * 
#   **
#   ***
#  ****
# *****
# n=int(input("Enter the num :"))
# for i in range(1,n+1):
#     spaces=" "*(n-i)
#     print(spaces+'*'*i)
    
# 2
# 4 4
# 6 6 6
# 8 8 8 8
# 10 10 10 10 10


# 2
# 4 4
# 8 8 8
# 16 16 16 16
base=int(input("Enter the base :"))
power=int(input("enter the power :"))
for i in range(1,power+1):
    print(f"{base} "*i)
    base*=base


# Scenario: Pizza Shop Ordering System
# Problem:
# Write a program to simulate a pizza shop ordering system.
# • The shop offers three sizes of pizza: Small ($10), Medium ($15), and Large ($20).
# • Customers can also add extra toppings:
# • Cheese ($2)
# Pepperoni ($3)
# • The program calculates the total cost of the order and allows customers to place multiple orders until they decide to exit.






# Level 2: Pizza Shop Ordering System with Multiple Pizzas and Delivery Option
# Problem:
# Expand the pizza shop system to include the following features:
# 1. The customer can order multiple pizzas in one order.
# 2. Add a delivery option:
# Delivery charge is $5 for orders under $50
# • Free delivery for orders of $50 or more.
# 3. Display the final receipt with a breakdown of all pizzas ordered, toppings, and the delivery charge.