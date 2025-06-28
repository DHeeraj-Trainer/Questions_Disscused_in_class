# name='sai'
# cgpa=93.5
# age=21
# hobbies=['games', "stocking", "books reading", "riding bikes"]
# marks=(6.7,6.6,6.9,6.9,7.0,7.4)
# acurracy=6.1+8j
# marks_set={6.7,6.6,6.9,6.9,7.0,7.4}
# info={'name':"sai",
#         'age':age,
#         'cgpa':cgpa,
#         "hobbies":hobbies,
#         "marks":marks_set,
#         "marks":marks,
#         "name":cgpa
#     }

# # print(info)
# # print("List:",hobbies)
# # print("Tuple",marks)
# # print("set",marks_set)


# hobbies=['games', "stocking", "books reading", "riding bikes"]
# marks=(6.7,6.6,6.9,6.9,7.0,7.4)

# print(hobbies[1])
# print(marks[1])
# print(info["name"])



# balance=1000
# def deposit(amount):
#     global balance
#     balance+=amount
#     print(f"Deposit DOne! and avalible :{balance}")
#     return balance
# def withdraw(amount):
#     global balance
#     balance-=amount
#     print(f"Withdraw DOne! and avalible :{balance}")
#     return balance
# def balance_enquairy():
#     print(f"Avalible Balance: {balance}")
# while True:
#     balance_enquairy()
#     print("-------ATM MAchine-------")
#     print("1.Withdraw")
#     print("2.Deposit")
#     print("3.Balance Enquriy")
#     print("4.Exit")
#     choice=int(input("Enter your choice(1-4): "))
#     if choice==1:
#         amount=int(input("Enter the amount for Withdraw: "))
#         withdraw(amount)
#     elif choice==2:
#         amount=int(input("Enter the amount for Depoist: "))
#         deposit(amount) 
#     elif choice==3:balance_enquairy()
#     elif choice==4:
#         print(f"Avalible Balance:{balance}")
#         print("Bye Bye")
#         break
#     else: print("Enter valid choice")   


"""
List
l=[1,2,3,4,5,6,7,'u',5]
el=[]

# for i in range(len(l)):
#     print(l[i])
# for i in l:print(i)

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1
    




for i in range(5):
    val=input("ENter value: ")
    el[i:i]=[val]
    el.append(val)
    
print(el)


l=[1,2,3,4,5,6,7,'u',5]
print(l)
# for i in range(len(l)):
#     print(f"{i}={l[i]}")
l[l.index('u')]=8
print(l)





l=[1,2,3,4,5,6,7,'u',5]
# evenlist=l[2:5]
# print("Even:",evenlist)
# b = [1, 2, 3]
# result = b * 3
# print("",result)
# for i in range(10):
#     if i%2==0:
#         print(i)

# for i in range(0,11,2):
#     print(i)
l=[1,2,3,4,5,6,7,8,5]
# for i in l:print(i)-
# a=[print(x) for x in l]
# print(a)
eben=[]
for i in l:
    if i%2==0:
        eben.append(i)
print(eben)
even=[x for x in l if x%2==0]
print(even,type(even))
even=tuple((x for x in l if x%2==0))
print(even,type(even))
even={x for x in l if x%2==0}
print(even,type(even))

ml=[1,2,3,[5,6,7,8,9,6]]
for i in ml:print(i)





# a=[1,2,35,6,8,6,5,8,99,0,66]
# a.append(5)
# a.insert(2,85)
# a.remove(2)
# a.pop()
# a.pop(0)
# print("Index-85:",a.index(85))
# print("2's Count:",a.count(2))
# a.sort()
# a.reverse()
# a.extend(a[2:3])
# print("SUm:",sum(a))
# a.append(sum(a))
# a.append(max(a))
# print("Index of 0",a.index(0))
# print("FInallen",len(a))
# print(f"Min:{min(a)} and Max:{max(a)}")


# list1=[1,5,8,9,6,3,7,-52,69,55,1,-4,5,2,3,6,9,555,125,145]
# print("Postion of max value:",list1.index(max(list1)))
# even_lst=[i for i in list1 if i%2==0]
# odd_lst=[i for i in list1 if i%2!=0]
# print("Len of even",len(even_lst))
# print("Len of Odd",len(odd_lst))
# sec_lst=sorted((list1),reverse=True)
# print("Second Largest",sec_lst[1])
# print("Avg Value:",(sum(list1)/len(list1)))
# pos_eve=[i for i in list1 if i%2==0 and i>0]
# lar_even=max(i for i in list1 if i%2==0)
# print((sec_lst))
# print(list1)



# names = ["Alice", "Bob", "Alice", "David", "Bob"]
# result=[]
# names.sort()
# for i in range(len(names)-1):
#     if names[i] != names[i+1]:
#         result.append(names[i])

# result.append(names[-1])

# print(result)

# el=[]
# for i in range(5):
#     val=input("ENter value: ")
#     el[i:i]=[val]
#     # el.append(val)
    
# print(el)


# sales = [0,120, 0, 340, 0, 230, 560, 0]
# #[120,340,230,560,0,0,0,0]
# el=[]
# non_zero=[]
# for i in sales:
#     if i >0:
#         el.append(i)
#     else:
#         non_zero.append(i)
# sales=el+non_zero
# print(sales)

# non_zero=[x for x in sales if x!=0]
# zeros=[x for x in sales if x==0]
# result=non_zero+zeros
# print(result)


# zero_count=sales.count(0)

# for i in range(zero_count):
#     sales.remove(0)
# for i in range(zero_count):
#     sales.append(0)

# print("Sales:",sales)



# From a list of user inputs, extract all palindromes.
words = ["madam", "apple", "noon", "hello"]
# Expected: ["madam", "noon"]

# words_=[]
# palindromes_list=[]
# n=int(input("Enter no of words: "))
# for i in range(n):
#     words_.append(input("Enter the word: "))
# palindromes_list_=[word for word in words_ if word==word[::-1]]
# for word in words_:
#         if word==word[::-1]:
#             palindromes_list.append(word)
# print(palindromes_list)


cart = ["apple", "banana", "apple", "orange", "banana"]

# unique_items=[]
# for item in cart:
#     if item not in unique_items:
#         unique_items.append(item)
# print(unique_items)

# for item in unique_items:
#     count=cart.count(item)
#     print(f"{item}>>>>{count}")


# From a list of student scores, get the top 3.
# scores = [50, 80, 90, 95, 70]
# # Output: [95, 90, 80]
# temp=sorted(scores)[::-1]
# top3=temp[:3]
# print(top3)

# data = [20, -5, 15, -1, 0, 33]
# res=[]
# for i in data:
#     if i>=0:
#         res.append(i)
# print(res)
nested = [[1, 2], [3, 4], [5],6,"5"]
# [
#     [1,2],
#     [3, 4],
#     [5]
# ]
# output=[1,2,3,4,5]
# ou=[]
# for i in nested:
#     if (type(i) == list):
#         for j in i:
#             ou.append(j)
#         # print(j)
#     else:ou.append(i)
# print(ou)

# team[start:stop:step]
team=['a','b','c','e','f','j','h']
# if len(team)%2==0:
#     mid=len(team)//2
#     print(team[:mid] ,team[mid:])
# else:print("Not an even length")
tasks=["t1","t2","t3","t4","t5"]
# k=int(input("enter roataions: "))
# k%=len(tasks)
# res=tasks[k:]+tasks[:k]
# print(res)

# logs=[1,2,3,4,5,6,7]


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
"""

# gven_lst = [2,4,6,8,10]
# n=int(input("enter the number: "))
# el=[]
# for i in range(len(gven_lst)):
#     gven_lst[i] = gven_lst[i]+n
# print(gven_lst)
# # for i in gven_lst:
# #     el.append(i+n)
# # print(el)


# range(0,11,2)
# numbers = [10, 20, 30, 40, 50, 60]
# even=numbers[0:len(numbers):2]
# odd=numbers[1:len(numbers):2]
# print(odd ,"and" ,even)


# items = ["abc", "a", "de", "abcd", "b"]
# for i in range(len(items)):
#     for j in range(i+1, len(items)):
#         if (len(items[i]))>(len(items[j])) or (len(items[i]) == len(items[j])) and items[i]>items[j]:  
#             items[i],items[j]=items[j],items[i]
# print(items)



# tasks=["t1","t2","t3","t4","t5"]
# k=int(input("Enter no of rotations: "))
# k%=len(tasks)
# print(tasks)
# tasks=tasks[k:]+tasks[0:k]
# print(tasks)

sales=[0,120,0,340,230,0,0,520,55,5200,0]
zero_count=sales.count(0)
# print(zero_count)
# for i in range(zero_count):
#     sales.remove(0)
# for i in range(zero_count):
#     sales.append(0)
# print(sales)

# zeros=[x for x in sales if x==0]
# non_zeros=[x for x in sales if x!=0]
# res=non_zeros+zeros
# print(res)


# given_list = [1, 3, 2, 6, 5] 
# b=max(given_list)
# summ=(b*(b+1))//2
# print("Missing number:",summ-sum(given_list))
# palindrom=[]
# words = ["madam", "apple", "noon", "hello"]
# for word in words:
#     if word==word[::-1]:
#         palindrom.append(word)
# print(palindrom)


# cart = ["apple", "banana", "apple", "orange", "banana"]
# unique_items=[]
# for item in cart:
#     if item not in unique_items:
#         unique_items.append(item)
# # print(unique_items)
# for item in unique_items:
#     print(f"{item} -> {cart.count(item)}")




# def display_menu():
#     print("\n____________Welcome to Mart___________")
#     print("1.Add item")
#     print("2.Remove Item")
#     print("3.Sort List")
#     print("4.Display the List")
#     print("5.Exit")

# def add_item(shop_list):
#     item=input("Enter the item u want add :")
#     shop_list.append(item)
#     print(f"{item}.Has been added to list.")
#     print(shop_list)

# def remove_item(shop_list):
#     item=input("Enter the item u want to remove :")
#     if item in shop_list:
#         shop_list.remove(item)
#         print(f"{item} has been removed")
#         print(shop_list)
#     else:
#         print(f"{item} is not in the list")
# def sort_list(shop_list):
#     shop_list.sort()
#     print("Sorted List :",shop_list)
# def display_finallist(shop_list):
#     if shop_list:
#         print("\n Final Shopping List")
#         for item in shop_list:
#             print(item)
#     else:print("No items in List")

# def list_manager():
#     shop_list=[]
#     while True:
#         display_menu()
#         choice=input("Enter Your Choice :")
#         if choice=='1':
#             add_item(shop_list)
#         elif choice=='2':
#             remove_item(shop_list)
#         elif choice=='3':
#             sort_list(shop_list)
#         elif choice=='4':
#             display_finallist(shop_list)
#         elif choice=='5':
#             print("Thank You")
#             break
#         else:
#             print("Invalid CHoice,Plese Try Again")
        

# list_manager()



"""
Tuples

"""

# a=10,20,30,40,50
# del a[0]
# del b
# b=10,
# del b
# print(a,b)
# print(type(a),a)
# print(type(b),b)

# a = (10, 20, 30, (50, 60))
# for i in a:
#     if type(i) ==tuple:
#         for j in i:
#             print(j)
#     else: print(i)


# Create a List of Tuples with the First Element 
# as the Number and Second Element as the Square of the Number
#  lowerlimit = 5
#  upperlimit = 13
el=[]
for i in range(5,14):
    el.append((i,i**2))
# print(el)
el=[(x,x**2) for x in range(5,14)]


# Remove Element from a Tuple at num postion
gven_tup = (14, 32, 16, 85, 47, 65)
#  num = 3

gven_list=list(gven_tup)
gven_list.pop(3)
# print(tuple(gven_list))

# get the First Element of each Tuple in a new List
gvn_tupl_lst = [(1, 2), (3, 4)]
# Output:[1,3]

# el=[]
# for i in range(len(gvn_tupl_lst)):
#     el.append((gvn_tupl_lst[i][0]))
# print(el)
# el=[gvn_tupl_lst[i][0] for i in range(len(el))]


# Swap First and Last Elements of a Tuple
Input= (10, 20,0, 300, 300, 300, 30, 30, 40)
# Output: (40, 20, 30, 10)

def swap(t):
    return (t[-1],)+t[1:-1]+(t[0],)
t=(10, 20,0, 300, 300, 300, 30, 30, 40)
# print(swap(t))

# Count Occurrence of  2 in a Tuple
Tuple= (1, 2, 3, 2, 4, 2)
# print(Tuple.count(2))

# Check if Two Tuples are Identical or not
Tuple1= (1, 2, 3)
Tuple2= (1, 2, 3)
# Output: True

# print(Tuple1==Tuple2)

# Find Maximum and Minimum in a Tuple
Input= (12, 5, 78, 34, 1)
# Output: max = 78, min = 1
# print(f"max = {(max(Input))}, min = {(min(Input))}")

# Concatenate Two Tuples
t1 = (1, 2) 
t2 = (3, 4)
# print(t1+t2)
# Result: (1, 2, 3, 4)


products = [("pen", 10), ("book", 50), ("bag", 120), ("pencil", 5)]
# Output: bag (120)
first_value=products[0]
for i in products[1:]:
    if i[1]>first_value[1]:
        first_value=i
# print(first_value[0],first_value[1])


student_answers = ('A', 'B', 'D', 'C', 'A')
correct_answers = ('A', 'B', 'C', 'C', 'A')
count=0
for i in range(len(student_answers)):
    if student_answers[i] == correct_answers[i]:
        count+=1

# print(f"{count} correct answers")
"""
14/6



attendance = [
    ["Alice", "Bob", "David"],
    ["Alice", "Charlie", "David"],
    ["Alice", "Bob"],
    ['Alice',"Charlie", "David"],
    ["Alice", "Bob", "Charlie"],
    ["Alice", "Charlie", "Bob"],
    ["Alice", "Bob"]
]


total_days=len(attendance)

all_students=[]
for day in attendance:
    for student in day:
        if student not in all_students:
            all_students.append(student)

print(all_students)

#Students who logged in every day

students_every_day=[]
for student in all_students:
    present_all_days=True
    for day in attendance:
        if student not in day:
            present_all_days = False
            break
    if present_all_days:
        students_every_day.append(student)
print(students_every_day)

# Login count for each student

login_count=[]
for student in all_students:
    count=0
    for day in attendance:
        for name in day:
            if name==student:
                count+=1
    login_count.append([student,count])

print(login_count)

# Students inactive more than 2 days
inactive_students=[]
for student,count in login_count:
    if total_days-count>2:
        inactive_students.append(student)

print(inactive_students)



a={1,2,3,5,10}
b={1,2,5,8,9,6,3,10}
#union
print("Union:",a.union(b))
print("Union:",a|b)
#Intersections
print("Intersections:",a.intersection(b))
print("Intersections:",a&b)
#difference
print("difference:",a.difference(b))
print("difference:",a-b)
#Symmetric difference
print("Symmetric difference: ",a^b)
#subset
print("Subset",a.issubset(b))
print("Subset",a<=b)
print("Subset",b<=a)
#superset
print("Subset",a.issuperset(b))
print("Subset",a>=b)
print("Subset",b>=a)
A = {1, 2}
B = {3, 4}
print("Disjoint",A.isdisjoint(B))


dept1 = {"Alice", "Bob", "Charlie"}
dept2 = {"Bob", "David", "Emma"}
# Output: Total unique attendees = 5
print("Lenght of uiques values:",len(dept1.union(dept2)))


store1 = {"apple", "banana", "orange"}
store2 = {"banana", "kiwi", "apple"}
print(" items available in both stores: ",store1.union(store2))
print("only in store1",store1-store2)
print("only in store2",store2-store1)


def manage_playlist(playlist, operation, song=None, another_playlist=None):
    if operation == "add":
        playlist.add(song)
        return f"Song {song} added to the playlist."
    elif operation == "remove":
        if song in playlist:
            playlist.remove(song)
            return f"Song {song} removed from the playlist."
        else:
            return f"Error: Song {song} not found in the playlist."
    elif operation == "discard":
        playlist.discard(song)
        return f"Song {song} discarded (if it existed)."
    elif operation == "pop":
        if playlist:
            removed_song = playlist.pop()
            return f"Randomly removed song: {removed_song}"
        else:
            return "Error: Playlist is empty."
    elif operation == "clear":
        playlist.clear()
        return "Playlist cleared successfully."
    elif operation == "union":
        if another_playlist is not None:
            return playlist.union(another_playlist)
        else:
            return "Error: Provide another playlist for union."
    elif operation == "intersection":
        if another_playlist is not None:
            return playlist.intersection(another_playlist)
        else:
            return "Error: Provide another playlist for intersection."
    elif operation == "difference":
        if another_playlist is not None:
            return playlist.difference(another_playlist)
        else:
            return "Error: Provide another playlist for difference."
    else:
        return "Error: Invalid operation."


def interactive_playlist_manager():
    playlist = set()
    print("Welcome to the Playlist Manager!")
    print("Initial Playlist:", playlist)
    
    while True:
        print("\nOperations: add, remove, discard, pop, clear, union, intersection, difference, exit")
        operation = input("Enter the operation you want to perform: ").strip().lower()
        
        if operation == "exit":
            print("Exiting the playlist manager.")
            break

        song = None
        another_playlist = None
        
        if operation in ["add", "remove", "discard"]:
            song = input("Enter the song ID: ").strip()
            if not song.isdigit():
                print("Invalid song ID! Please enter a numeric value.")
                continue
            song = int(song)

        if operation in ["union", "intersection", "difference"]:
            another_playlist_input = input("Enter another playlist as comma-separated song IDs (e.g., 101,102,103): ").strip()
            another_playlist = set(int(s) for s in another_playlist_input.split(",") if s.isdigit())
        
        result = manage_playlist(playlist, operation, song, another_playlist)
        print("\nResult:", result)
        print("Updated Playlist:", playlist)


interactive_playlist_manager()



drama_club = {"Aarav", "Priya", "Ravi", "Meera", "Sneha"}
music_club = {"Sneha", "Karan", "Aarav", "Divya", "Rohit"}
dance_club = {"Divya", "Ravi", "Ishaan", "Meera", "Asha"}
tech_club = {"Karan", "Aarav", "Rohit", "Vikram", "Meena"}
sports_club = {"Ravi", "Vikram", "Asha", "Neha", "Divya"}


ai_club = {"Riya", "Ishaan", "Meena"}

other=[drama_club,music_club,dance_club,tech_club,sports_club]
new=[ai_club.isdisjoint(culb) for culb in other]
print(new)



a="Try programiz.pro"
a[0]="P"
print(a)





# drama_club = {"Aarav", "Priya", "Ravi", "Meera", "Sneha"}
# music_club = {"Sneha", "Karan", "Aarav", "Divya", "Rohit"}
# dance_club = {"Divya", "Ravi", "Ishaan", "Meera", "Asha"}
# tech_club = {"Karan", "Aarav", "Rohit", "Vikram", "Meena"}
# sports_club = {"Ravi", "Vikram", "Asha", "Neha", "Divya"}
# # 👁️‍🗨️ Is "Aarav" in more than one club?
# c=D=0
# clubs=[drama_club,music_club,dance_club,tech_club,sports_club]
# for club in clubs:
#     if "Aarav" in club:
#         c+=1
#     if "Divya" in club:
#         D+=1
# print(c,D)
# if c>1 :print(True)


# names=input("Enter names: ").split(' ')
# print(names)
# names=["Aarav", "Priya", "Ravi", "Meera", "Sneha"]
# print('-'.join(names))



story = "   Once upon a TIME in a distant village, there lived a wise coder named Python. He was respected for his WISDOM, logic, and power. python often said: 'Code is poetry!'   "



start=story.find("'")
end=story.rfind("'")
print(start, end)
print(story[start+1:end])
print(story[:13])
print(story[-15::])
print(story[10:50:2])
print(story[::-1])
story.strip()
# 25. Finally, form a password using: 
# the first 3 letters, the last 3 letters, 
# and the length of the final story.

print(story[:3]+story[-3:]+str(len(story)))

""" 


inventory = {
 "wand": 3,
 "potion": 5,
 "scroll": 7,
 "elixir": 2,
 "wand":2,
 "gem": 10
}

# 1. The wizard needs to know how many types of items he owns.
# print(len(inventory))
# print(inventory.keys())
# print(inventory.values())
# print(inventory.items())
# inventory.pop("elixir")
# print(inventory)
# print(inventory.get("scroll",0))
# inventory["crystal"]=4
# inventory["wand"]=2
new= {"crystal": 4, "wand": 2}
inventory.update(new)
# print(inventory)
inventory["wand"]=10
# print(inventory)
# print("dagger" and "gem" in inventory)
# print(list(inventory.keys())[0])
# print(list(inventory.values()).index(max(list(inventory.values()))))
# print(inventory.items())

# print(list(inventory.keys())[list(inventory.values()).index(max(list(inventory.values())))])

# most_valu=max(inventory,key=inventory.get)
# print(most_valu)

# least_valu=min(inventory,key=inventory.get)
# print(least_valu)


# sroted_by_name=dict(sorted(inventory.items()))
# print(sroted_by_name)
# sroted_by_value=dict(sorted(inventory.items(),key=lambda x:x[1],reverse=True))
# print(sroted_by_value)
# print(inventory.items())
# double={}
# for items,qty in inventory.items():
#     double[items]=qty*2
#     print(double)


# print(sum(inventory.values()))


# names=input("Enter names:").split(" ")
# print(names)
# a="kowshik is multi talented"
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())
# print(a.replace("kowshik", "karthik"))
# print(a.startswith("k"))

story = "   Once upon a the TIME in a distant village, there lived a wise coder named Python. He was respected for his WISDOM, logic, and power. python often said: 'the Code is poetry!'   "

# print(story.count("Python")+story.count("python"))

# a=str(bin(1000))
# print(a,a.count("1"))
story.strip()
print(story[:4]+story[-1:-4]+str(len(story)))