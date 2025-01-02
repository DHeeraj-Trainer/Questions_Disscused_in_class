# CONVERT CELSIUS TO FAHRENHEIT
# def celsius_to_fahrenheit(celsius): return (celsius * 9/5) +32
# print("fahrenheit:", celsius_to_fahrenheit(int(input("Enter the celsius Temp :"))))

# x= lambda celsius:(celsius * 9/5) +32
# print("fahrenheit:",x(int(input("Enter the celsius Temp :"))))

# SWAP TWO VARIABLES without temp
# def Swap(a,b):return b,a
# print(Swap(input("a :"),input("b :")))
# swap=lambda a,b : print(b,a)
# swap(input("a :"),input("b :"))
# rgb_to_hex
# def rgb_to_hex(r, g, b): return f"#{((r << 16) + (g << 8) +b):06X}"
# print(rgb_to_hex(0, 51, 255))
# rgb_to_hex=lambda r,g,b:f"#{((r << 16) + (g << 8) +b):06X}"
# print(rgb_to_hex(0, 51, 255))
# from datetime import datetime

# def is_date_valid(val):
#     return datetime.strptime(val, "%B %d, %Y %H:%M:%S") if val else False
# print(is_date_valid("December 17, 1995 03:24:00"))

'''
FIND THE FRECUENCY OF CHARACTER IN A STRING
input:Hello
output:
H-1
e-1
l-2
o-1

VALIDATE VOWEL SANDWICH
The is_vowel_sandwich function validates
whether a 3-character string is a vowel
sandwich.
def vowel_sandwich(String):
    vowels='aeiouAEIOU'
    if len(String)==3:
        if String[0] not in vowels and String[1] in vowels and String[2] not in vowels:print(f"{String}:Valid VOwel Sandwich")
        else:print(f"{String}:Not Valid VOwel Sandwich")
    else:print("Enter the 3-char String")    
vowel_sandwich(input("Enter the 3-char String :"))

VALIDATE NUMBER WITHIN BOUNDS
input:
100
20
5
output:False


GENERATE A RANDOM NUMBER WITHIN A RANGE






CHECK IF ALL ELEMENTS IN AN list ARE THE SAME
list1=[2,2,2,2,2,2,2,2,2]
if len(set(list1))==1:
    print("Valid)
else:print("invalid")

FIND THE INTERSECTION OF TWO lists

list1=[1,2,3,6,5,8,6]
list2=[1,2,3,5,6]
intersection_set=(set(list1)).intersection(set(list2))
print(intersection_set)

COUNT DECIMAL PLACES
num=input("Enter a Decimal Value :)
0_pos=num.index('.')+1
print("COunt of decimal values is  :",len(num)-0_pos)





FIND THE DIFFERENCE BETWEEN TWO lists

list1=[1,2,3,6,5,8,6]
list2=[1,2,3,5,6]
diffrence_set=(set(list1)).diffrence(set(list2))
print(diffrence_set)



FIND NEMO
string="There is Mom Nemo and Father Nemo in a Nemo Family. They gave a Birth for SOn Nemo and Daughter Nemo "
a=string.split(" ")
print(a.count("Nemo"))

REMOVE DUPLICATES FROM A STRING
input:Hello
output:Helo

s=input("Enter the String :")
res=''
for i in s:
    if i not in res:
        res+=i
print(res)

def rem(strr):
    s=set(strr)
    s=','.join(s)
    t=''
    for i in strr:
        if i not in t:
            t+=i
    print(s,type(s))
    print(t,type(t))
rem("Hello")




FIND THE MODE OF AN list OF NUMBERS

list1=[1,1,1,2,3,2]
dic={}
for i in list1:
   if i not in dic:
     dic[i]=1
   else:
     dic[i]=dic[i]+1
maximum=max(dic.values())
for i in dic:
    if dic[i]==maximum:
        print(i)



# CONVERT CELSIUS TO FAHRENHEIT
# def celsius_to_fahrenheit(celsius): return (celsius * 9/5) +32
# print("fahrenheit:", celsius_to_fahrenheit(int(input("Enter the celsius Temp :"))))

# x= lambda celsius:(celsius * 9/5) +32
# print("fahrenheit:",x(int(input("Enter the celsius Temp :"))))

# SWAP TWO VARIABLES without temp
# def Swap(a,b):return b,a
# print(Swap(input("a :"),input("b :")))
# swap=lambda a,b : print(b,a)
# swap(input("a :"),input("b :"))
# rgb_to_hex
# def rgb_to_hex(r, g, b): return f"#{((r << 16) + (g << 8) +b):06X}"
# print(rgb_to_hex(0, 51, 255))
# rgb_to_hex=lambda r,g,b:f"#{((r << 16) + (g << 8) +b):06X}"
# print(rgb_to_hex(0, 51, 255))
# from datetime import datetime




FIND THE FRECUENCY OF CHARACTER IN A STRING
input:Hello
output:
H-1
e-1
l-2
o-1

VALIDATE VOWEL SANDWICH
The is_vowel_sandwich function validates
whether a 3-character string is a vowel
sandwich.
def vowel_sandwich(String):
    vowels='aeiouAEIOU'
    if len(String)==3:
        if String[0] not in vowels and String[1] in vowels and String[2] not in vowels:print(f"{String}:Valid VOwel Sandwich")
        else:print(f"{String}:Not Valid VOwel Sandwich")
    else:print("Enter the 3-char String")    
vowel_sandwich(input("Enter the 3-char String :"))

VALIDATE NUMBER WITHIN BOUNDS
input:
100
20
5
output:False


GENERATE A RANDOM NUMBER WITHIN A RANGE






CHECK IF ALL ELEMENTS IN AN list ARE THE SAME
list1=[2,2,2,2,2,2,2,2,2]
if len(set(list1))==1:
    print("Valid)
else:print("invalid")

FIND THE INTERSECTION OF TWO lists

list1=[1,2,3,6,5,8,6]
list2=[1,2,3,5,6]
intersection_set=(set(list1)).intersection(set(list2))
print(intersection_set)

COUNT DECIMAL PLACES
num=input("Enter a Decimal Value :)
0_pos=num.index('.')+1
print("COunt of decimal values is  :",len(num)-0_pos)





FIND THE DIFFERENCE BETWEEN TWO lists

list1=[1,2,3,6,5,8,6]
list2=[1,2,3,5,6]
diffrence_set=(set(list1)).diffrence(set(list2))
print(diffrence_set)



FIND NEMO
string="There is Mom Nemo and Father Nemo in a Nemo Family. They gave a Birth for SOn Nemo and Daughter Nemo "
a=string.split(" ")
print(a.count("Nemo"))

REMOVE DUPLICATES FROM A STRING
input:Hello
output:Helo

s=input("Enter the String :")
res=''
for i in s:
    if i not in res:
        res+=i
print(res)

def rem(strr):
    s=set(strr)
    s=','.join(s)
    t=''
    for i in strr:
        if i not in t:
            t+=i
    print(s,type(s))
    print(t,type(t))
rem("Hello")




FIND THE MODE OF AN list OF NUMBERS

list1=[1,1,1,2,3,2]
dic={}
for i in list1:
   if i not in dic:
     dic[i]=1
   else:
     dic[i]=dic[i]+1
maximum=max(dic.values())
for i in dic:
    if dic[i]==maximum:
        print(i)



# SUM OF NUMBERS UP TO A GIVEN NUMBER








CAPITALIZE THE FIRST LETTER OF EACH WORD IN A STRING







COUNT THE NUMBER OF WORDS IN A STRING







COUNT ONES IN BINARY REPRESENTATION





input_=str(bin(int(input("Enter the Value :"))))
count=0
for i in input_:
    if i=='1':
        count+=1

print("1 count :",count)
print("1 count :",input_.count('1'))


GENERATE A RANDOM NUMBER BETWEEN 1 AND 10
CHECK IF A STRING IS EMPTY



a=input("Enter u re string :")
print(a,len(a))
if len(a)==0:
    print("String is empty")
else:print("Not Empty")

CONVERT MINUTES TO SECONDS

CONVERT AN list TO A COMMA-SEPARATED STRING




lst1=[1,2,3,4,5]
lst=list('students')
print(lst)
a=','.join(lst)
print(a)

CHECK IF A LIST IS SORTED IN ASCENDING ORDER




spELL OUT A WORD
input:example
 Output: e, ex, exa, exam, examp, exampl, example   
 

a=input("Enter the String :")
s=''
for i in a:
    s+=i
    print(s)

lst=[1,2,3,4]
sum=0
for i in lst:
    sum+=i**3
print(sum)



# FIND THE NTH FIBONACCI NUMBER (RECURSIVE)
# 0 1 1 2 3 5 8 13 21 34 55
def FIBONACCI(n):
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    else:
        return FIBONACCI(n-1)+FIBONACCI(n-2)
print(FIBONACCI(int(input("Enter the Nth number :"))))    


# Find All Permutations
# def string_permutations(s):
#     pass

# print(string_permutations("abc"))  
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# a='abc'

# print(a[0]+a[2:0:-1])
# print(a[0]+a[1:])
# print(a[1]+a[0::2])
# print(a[1]+a[2::-2])
# print(a[2]+a[1::-1])
# print(a[2]+a[0:2])


# Maximum Difference Between list of Elements

# Find the First Non-Repeating Character



def permm(n):
    if len(n)==1:
        return [n]
    pre =[]
    for i in range(len(n)):
        for char in permm(n[:i]+n[i+1:]):
            pre.append(n[i]+char)
    return pre
print(permm('abc'))


# Check for Balanced Parentheses
# Write a function to check if an expression has balanced parentheses, including {}, [], and ().
# intt=input("enter the string :")
# if intt.count('(')=intt.count(')')

# Word Break Problem
# Write a function to check if a string can be segmented into a space-separated sequence of dictionary words.
# def word_break(s, word_dict):
#     pass

'''
# String Compression
# Implement a function to compress a string 
# based on the counts of repeated characters.
# Example:
#     def compress_string(s):
#     pass

# print(compress_string("aaabbc"))  # Output: "a3b2c1"
''' s='aabbcc'
dic={}
n=''
for i in s:
   if i not in dic:
     dic[i]=1
   else:
     dic[i]=dic[i]+1
for char in dic:
    n=char+str(dic[char])
    print(n)''' 



# from datetime import datetime
# def is_date_valid(val):
#     return datetime.strptime(val, "%B %d, %Y %H:%M:%S") if val else False
# print(is_date_valid("December 17, 1995 03:24:00"))



# def FIBONACCI(n):
#     if n == 1:
#         return 0
#     if n == 2 or n == 3:
#         return 1
#     else:
#         return FIBONACCI(n - 1) + FIBONACCI(n - 2)

# def fibonacci_triangle(rows):
#     count = 1
#     for i in range(1, rows + 1):
#         row = []
#         for _ in range(i):
#             row.append(FIBONACCI(count))
#             count += 1
#         for num in row:
#             print(num, end=" ")
#         print()

# n = int(input("Enter the number of rows for the Fibonacci Triangle: "))
# fibonacci_triangle(n)



def fib(n):
    a,b =0,1
    for i in range(1,n+1):
        row=[]
        for _ in range(i):
            row.append(a)
            a,b=b,a+b
        print(" ".join(map(str,row)))
n=int(input())
fib(n)

def fib(n,memo={}):
    if n==1:
        return 0
    elif n==2:
        return 1
    if n not in memo:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
n=int(input())
print(fib(n))












