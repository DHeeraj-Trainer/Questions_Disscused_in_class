import array as arr
# array_name=array.array('type_code',[eles])


# ex:  
# stu_roll=arr.array('b',["b",])
# stu_roll=arr.array('f',[101,102,103,104])
# print(stu_roll)
# stu_roll[1]=105
# print(type(stu_roll))
# for i in range(len(stu_roll)):
#     print(i,stu_roll[i])

# stu_roll.append(105)
# print(tuple(stu_roll))
# print(stu_roll)


marks = [55, 67, 72, 80, 91]
# for i in range(len(marks)):
#     marks[i]=marks[i]+5
# print(marks)
# marks = [(x+5) for x in marks] 
# print(marks)

def l_search(marks,target):
    if target in marks:
        for i in range(len(marks)):
            if marks[i]==target:
                return i
    else: return -1
# print(l_search(marks,2))
def bin_search(marks,target):
    if target in marks:
        low=0
        high=len(marks)-1
        while (low<=high):
            mid=(low+high)//2
            if marks[mid]==target:
                return mid
            elif marks[mid]<target:
                low=mid+1
            else:high =mid-1
    return -1
def bin_search_rec(marks,target,low=0,high=len(marks)-1):
    if target in marks:
        # low=0
        # high=len(marks)-1
        while (low<=high):
            mid=(low+high)//2
            if marks[mid]==target:
                return mid
            elif marks[mid]<target:
                # low=mid+1
                return bin_search_rec(marks,target,mid+1,high)
            else:
                # high =mid-1
                return bin_search_rec(marks,target,low,mid-1)
    return -1
# print(bin_search(marks,55))
# print(bin_search_rec(marks,55))
# marks = ["(55)","88","True"," [67]", "72", "8.0", "{91}"]
import numpy as np
marks = [55, 67, 72, 80, 91]
# arr_name=np.array([elements])
# marks_np=np.array(marks)
# print(marks_np)
# print(type(marks_np))

# marks=[[x,x*x,x**3] for x in marks]

# marks_np=np.array(marks)
# print(marks_np)
# print(type(marks_np))
# d2=[[1,2],[23,56],[8,9,7]]
d2=np.array([[1,2],
             [4,5],
             [7,8]],dtype=np.float32)
# print(d2)
# lst=[]
# for i in range(len(d2)):
#     for j in range(len(d2[i])):
#         # print(d2[i][j],end=' ')
#         lst.append(d2[i][j])
# print(lst)
# print(type(d2),d2.dtype)
# print(d2.shape)
# print(d2.ndim)
# print(len(d2))
# print(d2.size)
# print(d2[2])
# print(d2[2][2])
# np.int8
# np.int16
# np.int32
# np.int64

# np.uint8
# np.uint16

# np.float16
# np.float32
# np.float64

# np.complex64
# np.complex128

# np.bool_

# np.str_

# marks = np.array(["(55)","88","True"," [67]", "72", "8.0", "{91}"])
# print(type(marks[0]))

# d3=np.array([
#     [[1,2],[3,4]],
#     [[5,6],[7,8]]
# ])
# print(d3)
# print(d3.shape)
# print(d3.ndim)

# array ( ) Function
# • linspace ( ) Function
# • logspace ( ) Function
# • arange ( ) Function
# • zeros ( ) Function
# • ones ( ) Function
# zero=np.zeros((3,4))
# print(zero)

# one=np.ones((2,2))
# print(one)
# arrg=np.arange(0,10,2)
# print(arrg)
# ls=np.linspace(0,10,5)
# print(ls)
# logs=np.logspace(1,10,10)
# print(logs)
# rand=np.random.randint(3,100,5)
# print(rand)

# d2=np.array([[1,2],
#              [4,4],
#              [7,2]],dtype=np.float32)
# print(d2)#(3,2)
#(6,1)
# print(d2.astype(int))
# d3=np.zeros((6,1))
# print(d3)
# k=0
# for i in d2:
#     for j in i:
#         d3[k]=j
#         k+=1
# print(d3)
# d3=d2.reshape(6,1)
# print(d3)
# print(d2.flatten())
# print(d2.T)
# print(sum(d2))
# print(d2.sum(),d2.max(),d2.mean(),np.median(d2),d2.std(),d2.var())

# print(np.unique(d2))
# d2=np.array([[1,2],
#              [4,4],
#              [7,2]],dtype=np.float32)
# print(d2)#(3,2)
# # print(np.where(d2>4))
# print(np.any(d2>2))
# print(np.all(d2>0))

# A school stores attendance records in a matrix where:
# 1 means Present,0 means Absent
# Each row represents a student and each column represents a day.Write a program to:
# Find the total number of presents.,Find the total number of absences.Find the student with the highest attendance.
# Find the attendance percentage of each student.
attendance =   np.array([[1,1,1,0,1],[1,0,1,0,1],[1,1,1,1,1],[0,0,1,0,1]])
# Expected Output
# Total Presents: 15  
# ,Total Absences: 5   
# Student With Highest Attendance: Student 

# Attendance Percentage:
# Student 1 -> 80.0%,Student 2 -> 60.0%
# Student 3 -> 100.0%,Student 4 -> 40.0%
# print("Total Presents",(np.sum(attendance)))

# print("Absences",attendance.size-np.sum(attendance))
# rowsum=[]
# for row in attendance:rowsum.append(sum(row))
# rowsum=[4,3,5,2]
# Highest_Attendance=rowsum.index(max(rowsum))+1
# print("Student",Highest_Attendance)
# student_attendance = [sum(row) for row in attendance]
# for i in range(len(student_attendance)):
# 	pct=(student_attendance[i]/len(attendance[0]))*100
# 	print(f"student {i+1} -> {pct}%")





# You are given the marks of N students in an np array. Write a program to:

# Find the highest mark.
# Find the lowest mark.
# Find the average mark.
# Count how many students scored above the average.
# Display the top 5 highest marks in descending order.
# Input
# marks = [78, 92, 65, 88, 95, 72, 84, 90, 67, 99]
# marks=np.random.randint(10,100,10)
# marks=np.array(input("enter:").split(','),dtype=int)
# Expected Output
# Highest Mark: 99   np.max(marks)
# Lowest Mark: 65   np.min(marks)
# Average Mark: 83.0  np.mean(marks)
# Students Above Average: 5  
# np.sum(marks>np.mean(marks))
# Top 5 Marks: [99, 95, 92, 90, 88]  
# np.sort(marks)[::-1][:5]