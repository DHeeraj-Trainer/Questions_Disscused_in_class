# Problem Statement:
# An ATM machine can dispense only ₹500, ₹200, and ₹100 currency notes. Write a program to determine the minimum number of notes required for a given withdrawal amount.

# Conditions:
# 1. Use the maximum possible number of ₹500 notes first.
# 2. Then use ₹200 notes for the remaining amount.
# 3. Finally use ₹100 notes for the remaining amount.
# 4. Display the count of each note.

# Input:
# An integer representing the withdrawal amount.

# Output:
# Display the number of ₹500, ₹200, and ₹100 notes.

# Test Case 1:
# Input:
# 1700

# Output:
# 500x3 200x1 100x0

# Test Case 2:
# Input:
# 900

# Output:
# 500x1 200x2 100x0



# char=input("Enter a char:")
# for i in char:
#     alpha="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
#     nums="7410852963"
#     if i in alpha:print("Alphabet")
#     elif i in nums:print("Digit")
#     else:print("SPl Char")

# a=0
# while a==0:
#     a+=1
#     print("Hello Everyone")
# print("Welcome to Python Programming")


# a=1
# while a<=10:
#     # a+=1
#     print(a)
#     a+=1



# n=int(input("Enter number: "))
# i=1
# sum=0
# while i<=n:
# 	sum+=i
# 	#print(i)
# 	i+=1
# 	print(sum)
	
# for i in range(1,n+1,1):
# 	sum+=i
# 	print(sum)
	
# n=int(input("Enter number: "))
# i=1
# while i<=10:
# 	print(f"{n} x {i}= {n*i}")
# 	i+=1
# for i in range(1,11):
# 	print(f"{n} x {i}= {n*i}")


list1=[5,8,9,6,3,66,8993,6332,5622,-9]
# print(list1)
# print(list1[0])
# for i in list1: #without index
#     print(i)
# for i in range(len(list1)): #with index
#     print(list1[i])
# i=0
# while i<len(list1): #with index
#     print(list1[i])
#     i+=1
# i,even_count,odd_count=0,0,0
# while i<len(list1): #with index
#     if list1[i]%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#     i+=1
# print(f"Even count: {even_count} Odd count: {odd_count}")


# n=int(input("Enter number: "))
# if n<=1:
# 	print("Not prime")
# else:
# 	prime=True
# 	for i in range(2,int(n**0.5)+1):
# 		if n%i==0:
# 			prime=False
# 			break
# 	if prime:print("Prime")
# 	else:print("Not prime")




# n=int(input("Enter number: ")) #144
# temp=n
# digits=0
# sum=0

# while temp>0:#144>0
# 	digits+=1   #digits=1
# 	temp//=10   #temp=temp//10=144//10=14
# #14>0                 1>0
# #digits=1+1=2		digits=2+1
# #temp=14//10=1  		temp=1//10=0
# temp=n
# while temp>0:
# 	digit=temp%10 #4
# 	sum=sum+digit**digits #0+4**3=64
# 	temp//=10#144//10=14
# if sum==n:print("Armstrong")
# else:print("no")









# word=input("Enter a word: ")
# vc=0
# for i in word:
#     if i in "aeiouAEIOU":
#         vc+=1
# print(f"Number of vowels in the word: {vc}")
# print(f"Number of consonants in the word: {len(word)-vc}")

# num=8
# for i in range(5):
# 	n=int(input("enter the number:"))
# 	if num==n:
# 		print("correct")
# 		break
# 	else:print("wrong guess")
# print("Game Over")





# total_seats=int(input("enter total no of seats: "))
# while total_seats>0:
# 	tickets=int(input("enter: "))
# 	if not tickets>total_seats:
# 		total_seats-=tickets
# 		print(total_seats,"reamining")
# 	else:print("enter below ",total_seats)	
# else:print("bus full")



# balance=10000
# while True:
# 	amount=int(input("enter the amount:"))
# 	if (amount>0 and amount<=balance and amount%100==0):
# 		balance-=amount
# 		print("updated balance:",balance)
# 	op=input("do u want continue?(y/N) :")
# 	if (op=="N" or balance==0):
# 		print("Thank you")
# 		break









