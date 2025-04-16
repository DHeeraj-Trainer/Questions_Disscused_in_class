'''

# check valid password or not 
# conditions:
#     no-of charcters:min 8 and max 15
#     only @,_ spl charcter are allowed
#     atleast one spl should be there

# passwords=["Pass@123","Pass123","pass_123","@85285296399999999"]

def valid_pass(password):
    if not (8<=len(password)<=15):
        return "Invaid Password Length"

    spl_char=["@","_"]
    has_spl_char=False
    count=0

    for char in password:
        if char.isalnum():
            continue
        elif char in spl_char:
            has_spl_char=True
            count=+1
        else:
            return "Invalid :doesnt contain spl_char"
    
    if not has_spl_char and count==1:
        return "Invalid : Only one Spl Char is Allowed "
    return "Valid Password"

passwords=["Pass@123","Pass123","pass_123","@85285296399999999"]

for pwd in passwords:
    print(f"password:{pwd} -{valid_pass(pwd)}")


# 🟢 Electricity Bill Calculation – A Neighborhood Challenge  

# 🏡 In the quiet town of GreenVille, the local electricity board has introduced a tiered pricing system for electricity consumption:  

# 🔹 0 - 100 units → ₹5 per unit  
# 🔹 101 - 200 units → ₹7 per unit  
# 🔹 201+ units → ₹10 per unit  

# 📌 Scenario:  
# Mr. Ravi, a shop owner, wants to automate his electricity bill calculation to help himself and his neighbors. Can you write a Python program to calculate the total bill based on the number of units consumed?  


# ✅ Example Calculations:  
# 📌 90 units → ₹450 (90 × ₹5)  
# 📌 150 units → ₹535 (100 × ₹5 + 50 × ₹7)  
# 📌 250 units → ₹1700 (100 × ₹5 + 100 × ₹7 + 50 × ₹10)  

# Can you help Ravi by building this Electricity Bill Calculator? ⚡️

# units=int(input("ENter the No of Units:"))
# def Electricity_Bill(Units):
#     if (0<units<101):
#         return (units*5)
#     elif(units<201):
#         return (100*5+(units-100)*7)
#     else:
#         return(100*5+100*7+(units-200)*10)

# print(f"Total ammount for {Units}: {Electricity_Bill(units)}")

A loan eligibility program to check the eligibility of multiple applicants.
• Continue taking input until the user decides to stop.
• For each applicant:
	• The person must be at least 21 years old.
	• The person must have a monthly income of $25,000 or more.
Display whether the person is eligible or not.

while True:
    age=int(input("Enter the Age:"))
    income=int(input("Enter the income:"))
    if age>=21 and income>=25000:
        print("Eligible for loan")
    else:print("Not Elgible")
    choice=input("Do u want continue?(yes or no):").strip().lower()
    if choice!='yes':
        break




Scenario: ATM Withdrawal System
Problem:
Write a program to simulate an ATM withdrawal system.
The user has an initial account balance of Rs: 10,000.
The program should:
1. Ask the user how much they want to withdraw.
2. Check if the amount is a multiple of 100.
3. Ensure the withdrawal amount does not exceed the account balance.
4. Deduct the amount if valid and display the remaining balance.
5. Allow multiple withdrawals until the user decides to exit 
or the balance is insufficient.

balance = 10000
while True:
    print("\n--- ATM Withdrawal System ---")
    print(f"Current Balance: ${balance}")
    withdrawal = int(input("Enter the amount to withdraw (multiple of 100): "))
    if withdrawal % 100 != 0:
        print("Invalid amount! Please enter a multiple of 100.")
    elif withdrawal > balance:
        print("Insufficient balance!")
    else:
        balance -= withdrawal
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    if balance == 0:
        print("Your balance is zero. No further withdrawals possible.")
        break
    another = input("Do you want to make another withdrawal? (yes/no): ").lower()
    if another != "yes":
        print("Thank you for using the ATM. Goodbye!")
        break

Scenario: Pizza Shop Ordering System
Problem:
Write a program to simulate a pizza shop ordering system.
• The shop offers three sizes of pizza: Small ($10), Medium ($15), and Large ($20).
• Customers can also add extra toppings:
    •Cheese ($2)
    •Pepperoni ($3)
• The program calculates the total cost of the order and allows customers 
to place multiple orders until they decide to exit.

while True:
    pizza=input("Choose the pizza(small/medium/large):")
    total_price=0

    if pizza=="small":total_price +=10
    elif pizza=="medium":total_price +=15
    elif pizza=="large":total_price +=20
    else:print("enter the valid size")

    cheese=input("Do u want to add ? (yes/no):")
    if cheese=='yes':total_price +=2

    pepperoni=input("Do u want to add ? (yes/no):")
    if pepperoni=='yes':total_price +=3

    print("Total price:",total_price)

    another_order=input("Do u want place another order: ")
    if another_order !='yes'
        print("Thank You")
        break



# Level 2: Pizza Shop Ordering System with Multiple Pizzas and Delivery Option
# Problem:
# Expand the pizza shop system to include the following features:
# 1. The customer can order multiple pizzas in one order.
# 2. Add a delivery option:
# Delivery charge is $5 for orders under $50
# • Free delivery for orders of $50 or more.
# 3. Display the final receipt with a breakdown of all pizzas ordered, toppings, and the delivery charge.

'''





'''





Stock Price Analysis:
stock_prices = [120, 135, 128, 140, 138, 150, 160]

Given a list of daily stock prices, find the highest profit 
and highest loss stock prices.
Calculate the average stock price.
Find the day on which the highest stock price occurred.










    max_price = max(stock_prices)
    min_price = min(stock_prices)

    average_price = sum(stock_prices) / len(stock_prices)

    max_price_day = stock_prices.index(max_price) + 1

    print("Max Stock Price:", max_price)
    print("Min Stock Price:", min_price)
    print("Average Price:", average_price)
    print("Day of Max Price:", max_price_day)




Online Shopping Cart:

Create a list of products in a shopping cart.
Remove a product from the cart.
Find the total cost of the items in the cart.
Sort the cart based on price.

shopping_cart = [
    {"product": "Laptop", "price": 800},
    {"product": "Headphones", "price": 50},
    {"product": "Mouse", "price": 25},
    {"product": "Keyboard", "price": 40},
    {"product": "Monitor", "price": 200}
]
def sort_cart(cart):
    n=len(cart)
    for i in range(n):
        for j in range(0,n-i-1):
            if cart[j]["price"]>cart[j+1]["price"]:
                cart[j],cart[j+1]=cart[j+1],cart[j]
        return cart 






for item in cart :
    print(item)
def rem_pro(cart,product_name):
    return [item for item in cart if item["product"].lower()!=product_name]











def remove_product(cart, product_name):
    return [item for item in cart if item["product"].lower() != product_name.lower()]

def calculate_total(cart):
    return sum(item["price"] for item in cart)

def sort_cart(cart):
    return sorted(cart, key=lambda x: x["price"])

shopping_cart = remove_product(shopping_cart, "Mouse")

total_cost = calculate_total(shopping_cart)

sorted_cart = sort_cart(shopping_cart)

print("Updated Shopping Cart:", shopping_cart)
print("Total Cost:", total_cost)
print("Sorted Cart by Price:", sorted_cart)




Student Grades Tracker:

A school is keeping track of student grades in a dictionary, 
where keys are student names and values are lists of their marks.
1.Implement a function to calculate each student's average marks 
and find the student with the highest average.
2.Add a new student's marks and update an existing student's marks.
Find students who scored below a given threshold.

grades = {
    "Ramu": [85, 90, 78],
    "Naresh": [76, 80, 72],
    "Charan": [90, 88, 95]
}







average_marks = {student: sum(marks)/len(marks) for student, marks in grades.items()}

top_student = max(average_marks, key=average_marks.get)

grades["David"] = [88, 92, 80]

grades["Alice"].append(95)
grades["Alice"]

threshold = 75
below_threshold = {k: v for k, v in average_marks.items() if v < threshold}

print("Average Marks:", average_marks)
print("Top Student:", top_student)
print("Updated Grades:", grades)
print("Students Below Threshold:", below_threshold)



Movie Review Analyzer:

Given a string containing a movie review, count the occurrences of each word.
Remove all punctuation and convert the review to lowercase before counting.
Find the longest and shortest word in the review.


"""
The translate() method replaces or removes characters 
based on a translation table created by str.maketrans().
The str.maketrans('', '', string.punctuation) part creates a
table that maps all punctuation characters to None (removes them).
string.punctuation is a predefined set containing all 
common punctuation characters (!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`).
"""


import string

review = "This movie was fantastic! The actors did an amazing job."






clean_review = review.lower().translate(str.maketrans('', '', string.punctuation))

word_count = {}
for word in clean_review.split():
    word_count[word] = word_count.get(word, 0) + 1

words = clean_review.split()
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

print("Word Frequency:", word_count)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)






Library Book Management:

Create two sets: one with books available in the library and 
another with books borrowed by students.
Find the books that are still available in the library.
Check if a specific book is currently borrowed.
Find books that are borrowed by multiple students.

available_books = {"Harry Potter", "1984", "Pride and Prejudice", "To Kill a Mockingbird"}
borrowed_books = {"1984", "Pride and Prejudice"}


remaining_books = available_books - borrowed_books

book_to_check = "1984"
is_borrowed = book_to_check in borrowed_books

student1_books = {"1984", "The Great Gatsby"}
student2_books = {"1984", "Moby Dick"}
common_borrowed = student1_books & student2_books

print("Available Books:", remaining_books)
print(f"Is '{book_to_check}' borrowed?", is_borrowed)
print("Books borrowed by multiple students:", common_borrowed)





Unique Visitors Tracker:

Given multiple sets representing website visitors for different days, find:
The total unique visitors over all days.
Visitors who came on all days.
Visitors who came only on one specific day.


day1_visitors = {"Amit", "Rohan", "Priya", "Sanjay", "Neha", "Raj"}
day2_visitors = {"Priya", "Neha", "Amit", "Ananya", "Vikram", "Rakesh"}
day3_visitors = {"Amit", "Priya", "Neha", "Rohan", "Sonia", "Karan"}













unique_visitors = day1_visitors.union(day2_visitors, day3_visitors)

regular_visitors = day1_visitors.intersection(day2_visitors, day3_visitors)

only_day1 = day1_visitors - (day2_visitors.union(day3_visitors))
only_day2 = day2_visitors - (day1_visitors.union(day3_visitors))
only_day3 = day3_visitors - (day1_visitors.union(day2_visitors))

print("Total Unique Visitors:", unique_visitors)
print("Visitors Who Came on All Days:", regular_visitors)
print("Visitors Who Came Only on Day 1:", only_day1)
print("Visitors Who Came Only on Day 2:", only_day2)
print("Visitors Who Came Only on Day 3:", only_day3)



🔍 The Curious Case of the Missing Data in the Grand Bazaar! 🔍

Hey everyone! The Grand Bazaar of Marketopolis is in trouble! 
😱 A mysterious data corruption has messed up product info, sales 
records, and customer details. 
Your mission, should you choose to accept it, is to use your 
Python skills to restore order! 🐍✨

Part 1: Product Inventory Check (Data Types & Loops)

⚠️ Problem: The inventory system is a mess! Some product 
lists have incorrect data types.

Task:
1.  Iterate through the products list.
2.  For each product:
    * Check if Product Name is str, Price is float, and 
    Quantity is int.
3.  Print an error message for incorrect data types.

Products:
products = [
    ["Spices", 12.50, 100],
    ["Silk Fabric", "25.00", 50],
    ["Pottery", 30.00, "20"],
    ["Gold Rings", 500.00, 5],
    ["Magic Lamp", "priceless", 1],
]


def check_prodcut_datatype(products):
    for product in products:
        if not isinstance(product[0],str):
            print(f"Error: {product[0]} - Name should be String.")
        if not isinstance(product[1],float):
            print(f"Error: {product[1]} - price should be Float.")
        if not isinstance(product[2],int):
            print(f"Error: {product[2]} - Quantity should be int.")

Expected Output:

Error: Silk Fabric - Price should be float.
Error: Pottery - Quantity should be int.
Error: Magic Lamp - Price should be float.

Part 2: Sales Record Analysis (Functions & Loops)

💰 Problem: Calculate the total sales from the given sales records.

Task:

1.  Create a function calculate_total_sales(sales_records).
2.  Iterate through sales_records.
3.  Sum the sale_amount values.
4.  Return the total sales.

Sales Records:

sales_records = [
    {"customer_id": "C123", "product_name": "Spices", "sale_amount": 125.00},
    {"customer_id": "C456", "product_name": "Silk Fabric", "sale_amount": 1250.00},
    {"customer_id": "C789", "product_name": "Pottery", "sale_amount": 600.00},
    {"customer_id": "C101", "product_name": "Gold Rings", "sale_amount": 2500.00},
]



def calculate_total_sales(sales_records):
    total_sales=0.0
    for sale in sales_records:
        total_sales +=sale["sale_amount"]
    return total_sales

Expected Output:

Total Sales: 4475.00

Part 3: Customer Loyalty Program (Functions, Loops, & Dictionaries)

👑 Problem: Identify loyal customers (3+ purchases).

Task:

1.  Create a function find_loyal_customers(customer_purchases).
2.  Iterate through customer_purchases.
3.  Count each customer's purchases.
4.  Add customer IDs with 3+ purchases to a list.
5.  Return the list.

Customer Purchases:

customer_purchases = {
    "C123": [125.00, 150.00, 200.00],
    "C456": [1250.00],
    "C789": [600.00, 300.00, 100.00, 50.00],
    "C101": [2500.00, 1000.00],
}

Expected Output:

Loyal Customers: ['C123', 'C789']

Let's get to work! 🚀 Share your solutions below!


def find_loyal_customers(customer_purchases):
    loyal_customers=[]
    for cust_id,purschases in customer_purchases:
        if len(purschases)>=3:
            loyal_customers.append(cust_id)
    return loyal_customers



```
'''

print(hello.find('lle'))