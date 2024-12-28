# a=15
# if a>10:print("Greater")
# else:print("less")
# if a>10:print("Greater")
# else:print("less")
# if a>10:print("Greater")
# else:print("less")
sub1=int(input("ENter sub1 Marks :"))
sub2=int(input("ENter sub2 Marks :"))
sub3=int(input("ENter sub3 Marks :"))
sub4=int(input("ENter sub4 Marks :"))
sub5=int(input("ENter sub5 Marks :"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
if sub1>35 and sub2>35 sub3>35 and sub4>35 and sub5>35:
    if sub1<=100 and sub2<=100 sub3<=100 and sub4<=100 and sub5<=100:
        if avg>90:print("A Grade")
        elif avg>80:print("B Grade")
        elif avg>70:print("C Grade")
        elif avg>60:print("D Grade")
        elif avg>50:print("E Grade")
        elif avg>35 and avg<50 :print("Pass")
    else:print("Enter the Valid Marks out of 100")
else:print("Fail, AVG=",avg)
Take a input from user and print like it is +ve or -ve
if it is a +ve number check it is even or odd
if it is a odd number check prime or not

take a amount input and 
if the amount is above 10000 apply 10%discont and print total amount and final amount
if less than 10000 print no discount applied 
and total amount
amount=int(input("enter the amount"))
if amount>10000:
    print("The Bill Amount :",amount)
    print("The Final Amount :",amount*0.1)
else:
    print("The Bill Amount :",amount)
    print("No Discount")
    
write a logic for the remote,check for the valid inputs or not 
if valid print the fucntion
'+'-VOlume UP,'-'-VOlume Down,'Ch+'-CHannel Incresed
'Ch-'-CHannel Dec,'On'-Power On,'off'-Power Off

a=input("Enter the work :")
list1=['+','-','ch+','ch-','on','off']
if a in list1:
    if a=='+':print('V-up')
else: print("invalid")


check user entered integer is Digit(1 number) or Number(2numbers) using function

write a program to caclute the bmi
BMI<18.5: UNDERWEIGHT
(18.5 -25)-normal
(25-30)-overweight
else obsese
weight=int(input("Enter the Weight in kgs :"))
height=int(input('Enter the height in cm :'))
bmi=(weight/((height/100)**2))
if bmi<18.5:print("under weight")
elif 18.5>=bmi<25:print('Normal')
elif 25>=bmi<30:print("Overwieght")
else:print("Obsese")


take 3 inputs check weather it is a valid triangle or not
a=int(input("Side1 :"))
b=int(input("Side2 :"))
c=int(input("Side3 :"))
if a+b>c and b+c>a and c+a>b :
    print("Valid")
else:print('invalid')



take a input check weather it is palindrom or not

a=input("enter the string :")
if a==a[::-1]:print("palindrom")
else: print("it is not a palindrom")

check valid password or not 
conditions:
    no-of charcters:min 8 and max 15
    only $,%,^,& spl charcter are allowed
    atleast one spl should be there
only using condtional statments only


password=input("enter the password")
spl=['$','%','^','&']
if len(password)>7 and len(password)<16:
    if spl[0] in password or '%' in password or '^' in password or '&' in password:
        print("Valid")
else:print("invalid")

# def monthname(int a,b):
#     days_30=[]
#     days_31=[]
#     days_28=[]
#     if month in days_30 or month in days_31 or month in days_28:
#         if month in days_30:print(month ,": 30days")
#         elif month in days_31:print(month ,": 31days")
#         else : print(month,": 28 days")
#     else: print("invalid month")
    
# month=input("enter the month name  :")
# monthname(month)



# def disp():
#     def show():
#         print("Show Function")
#     print("Disp Function")

# disp()



# def add(a):
#     b=90
#     print(a+b)
# add(5)

