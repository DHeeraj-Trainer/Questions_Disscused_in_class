



# # Pizza Shop Ordering System
# # Create a menu-driven program to simulate a pizza shop ordering system.
# # The shop offers the following pizzas:
# # * Small Pizza – $10,* Medium Pizza – $15,* Large Pizza – $20
# # Customers can add extra toppings:
# # * Cheese – $2,* Pepperoni – $3
# # Customers can also choose home delivery for an additional charge of **$5**.
# # The program should:
# # 1. Display a menu with options to place an order, view the bill, or exit.
# # 2. Allow customers to select a pizza size.
# # 3. Allow customers to add toppings if desired.
# # 4. Ask whether delivery is required.
# # 5. Calculate and display the cost of each order.
# # 6. Keep a running total of all orders.
# # 7. Return to the main menu after each transaction.
# # 8. Display the final bill when the customer chooses to exit.
# # The program should continue running until the user selects the **Exit** option.



# total_bill = 0

# while True:
#     print("\n========== PIZZA SHOP MENU ==========")
#     print("1. Place Order")
#     print("2. View Current Bill")
#     print("3. Exit")
#     print("=====================================")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("\nPizza Sizes:")
#         print("1. Small  - $10")
#         print("2. Medium - $15")
#         print("3. Large  - $20")

#         size = int(input("Choose pizza size: "))

#         if size == 1:
#             pizza_cost = 10
#             pizza_name = "Small"
#         elif size == 2:
#             pizza_cost = 15
#             pizza_name = "Medium"
#         elif size == 3:
#             pizza_cost = 20
#             pizza_name = "Large"
#         else:
#             print("Invalid Pizza Size!")
#             continue

#         toppings_cost = 0

#         cheese = input("Add Cheese ($2)? (y/n): ")
#         if cheese.lower() == 'y':
#             toppings_cost += 2

#         pepperoni = input("Add Pepperoni ($3)? (y/n): ")
#         if pepperoni.lower() == 'y':
#             toppings_cost += 3

#         delivery = input("Home Delivery ($5)? (y/n): ")
#         delivery_charge = 5 if delivery.lower() == 'y' else 0

#         order_total = pizza_cost + toppings_cost + delivery_charge
#         total_bill += order_total

#         print("\n----- Order Summary -----")
#         print("Pizza Size      :", pizza_name)
#         print("Pizza Cost      : $", pizza_cost)
#         print("Toppings Cost   : $", toppings_cost)
#         print("Delivery Charge : $", delivery_charge)
#         print("Order Total     : $", order_total)
#         print("-------------------------")

#     elif choice == 2:
#         print("\nCurrent Total Bill: $", total_bill)

#     elif choice == 3:
#         print("\nFinal Bill: $", total_bill)
#         print("Thank you for ordering!")
#         break

#     else:
#         print("Invalid Choice! Please try again.")



def details(name,age,college="KITS College"):
	print(f"Name: {name}\nAge: {age}\nCollege: {college}")
# details(age=20,name="Alice", college="XYZ University")#Keyword Arguments
# details(20,"Alice","XYZ University")# Positional
# details("Alice",20,"XYZ University") #Positional
# details("Alice",20) #Default
#Variable Length Arguments
def add(a,b):
    return a+b
# print(add(5,10,55))

def add(*nums):
      return sum(nums)
# print(add(5,10,55))
#Keyword Variable Length Arguments
def details(**values):
      for key,value in values.items():
            print(f"{key}: {value}")
# details(name="Alice", age=20, college="XYZ University", city="New York").

PI=3.14
# def areaof_circle():
#     radius=int(input("enter the radius: "))
#     print(PI*radius**2)
# print("Area of Circle:",areaof_circle())
# area=lambda r=int(input("radius:")): 3.14*r**2
# print("Area of Circle:",area())


def is_palindrome():
	word=input("enter word")
	left=0
	right=len(word)-1
	while left<right:
		if word[left]!=word[right]:
			return False
		left+=1
		right-=1
	return True
# print(is_palindrome())
# print(is_palindrome())
# # print(is_palindrome())

# count=0
# def counter():
#     global count
#     count+=1
#     print(count)
# counter()
# counter()
# counter()


# l1=[1,2,3,6,8,0]
# print(l1)
# for i in l1:
#        print(i)
# for i in range(len(l1)):print(l1[i])

def userdefined_list():
	n=int(input("enter the size: "))
	l=[]
	for i in range(n):
		# l.append(int(input("enter the value: ")))
		l+=[int(input("enter the value: "))]
	return l
def ticket_price(lst):
	total=0
	for i in lst:
		if i<12 and i>0:
			print(i,"->",10)
			total+=10
		elif i>12 and i<60:
			print(i,"->",15)
			total+=15
		elif i>60:
			print(i,"->",12)
			total +=12
		else:total+=0
	return total
# print(ticket_price(userdefined_list()))


# a=[1,2,35,6,8,6,5,8,99,0,66]
# a.append(5)
# a.insert(2,85)
# a.remove(2)
# a.pop()
# a.pop(0)
# print(a.index(85))
# print(a.count(2))
# a.sort()
# a.reverse()
# slice=a[2:3]
# #a.extend(a[2:3])
# a.extend(slice)
# a.append(sum(a))
# a.append(max(a))
# print(len(a),a.index(0),min(a),max(a))


# def move_zeroes(lst):
# 	z=lst.count(0)
# 	for i in range(z):
# 		lst.remove(0)
# 		lst.append(0)
# 	return lst
# print(move_zeroes([0,1,0,3,12]))

def missing_num(lst):
	n=len(lst)+1
	total_sum=(n*(n+1))//2
	return total_sum-sum(lst)
# print(missing_num([1,2,3,5]))

decimals=[1.2,1.5,85.0,563.585,0.0001]
def count_decimals(value):
	value=list(str(value))
	dot=value.index('.')

	return (len(value)-dot-1)
# count_decimals()

#map(function, iterable)

# res=list(map(count_decimals,decimals))
# print(res)
# lst=[1,2,3,4,5]
# # res=list(map(lambda x:x**2,lst))
# # print(res)
# res=list(filter(lambda x:x%2!=0,lst))

# tup=(1,5.5,8,"9m6")
# print(tup)
# tup=(1,5)
# print(tup[0])
# # tup[0]=10
# del tup[0]
# print(tup)
# s1="Hello"
# s1="world"
# # del s1
# print(s1[0])
# s1[0]="h"
# print(s1)

# tup=(8)
# print(type(tup))
# tup=(8,)
# print(type(tup))

# tup=(1,5.5,8,"9m6")
# tup1=(1,5)
# tup=tup+tup1
# print(tup)



a = (  (10, 20, 30),
         (40, 50, 60)  )
# # for i in a:
# 	print(i)
# 	for j in i:
# 		print(j)
a=[]
r=3
c=2
# for i in range(r):
# 	a.append([])
# 	for j in range(c):
# 		a[i].append(int(input(":")))
# print(a)

def add_item(lst,item):
	lst.append(item)
	print("item added successfully")
	return lst

def remove_item(lst,item):
	if item in lst:
		lst.remove(item)
		print("item deleted")
	else:print("item not found")
	return lst

def sort_list(lst):
	if lst:
		lst.sort()
		return lst
	else:print("list is empty")
def display_list(lst):
	if lst:
		for i in range(len(lst)):
			print(i+1,")",lst[i])
	else:print("list is empty")
def menu():
	print("1.Add item \n 2. remove \n 3. sort\n4.display \n 5.exit() ")


# lst=[]
# while True:
# 	menu()
# 	choice=int(input("enter(1,2,3,4):"))
# 	if choice==1:
# 		item=input("enter the item: ")
# 		add_item(lst,item)
# 	elif choice==2:
# 		item=input("enter the item: ")
# 		remove_item(lst,item)
# 	elif choice==3:
# 		print(sort_list(lst))
# 	elif choice==4:
# 		display_list(lst)
# 	elif choice==5:
# 		print("Final List:",lst)
# 		print("Bye Bye")
# 		break

import copy

org=[1,2,3,[4,5]]
shallow=copy.copy(org)
deep=copy.deepcopy(org)
print(org)
print(shallow)
print(deep)
print("-----------------")
shallow[3][0]=9
print(org)
print(shallow)
print(deep)



