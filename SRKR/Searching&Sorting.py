# import time
# import sys

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def calculate_factorial_time_and_space(n):
#     start_time = time.time()
#     factorial_result = factorial(n)
#     end_time = time.time()

#     initial_memory = sys.getsizeof(factorial)
#     final_memory = sys.getsizeof(factorial)

#     time_taken = end_time - start_time
#     space_used = final_memory - initial_memory

#     print(f"\nFactorial of {n} is: {factorial_result}")
#     print(f"Time taken for recursion: {time_taken:.6f} seconds")
#     print(f"Space used by recursion (approximate): {space_used} bytes")

# n = 10
# calculate_factorial_time_and_space(n)




# Searching:
# finding of element /data postion in a data structure

# Liner and Binary 

# Liner Seacrhing
# 1.Trasverse each elemel from start 
# 2.compare with target
# 3.if found return index else return -1
# Best Case :O(1)
# Worst Or AVG Case:O(n)
import time
import sys
def liner_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# initial_memory = sys.getsizeof(liner_search)
# start_time = time.time()
# a=[5,3,8,6,2,1,4,7,9,5]
# target=7
# output=liner_search(a,target)
# end_time = time.time()
# final_memory = sys.getsizeof(liner_search)
# time_taken = end_time - start_time
# space_used = final_memory - initial_memory
# print(f"\nlocation of {target} is: {output}")
# print(f"Time taken for recursion: {time_taken:.6f} seconds")
# print(f"Space used by recursion (approximate): {space_used} bytes")



"""
# arr=[1,5,7,8,2,3,6,220,7,8,2,3,6,14,7,8,2,3,6]
# arr.sort()
# print(arr)
# target=12
# print(arr.index(target))
def liner_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
def binary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low =mid+1
        else:high=mid-1
    return -1
    
def binary_search_recursion(arr,target,low,high):
    # low,high=0,len(arr)-1
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursion(arr,target,mid+1,high)
    else: return binary_search_recursion(arr,target,low,mid-1)
arr=[1,5,7,8,2,3,6,220,7,8,2,3,6,14,7,8,2,3,6]

# arr=[1,2,3,4,4,5,6,6,8,9,9,11,15]
target=220
start_time2 = time.time()
print(liner_search(arr,target))
end_time2 = time.time()
start_time1 = time.time()
print(binary_search(arr,target))
end_time1 = time.time()
start_time = time.time()
print(binary_search_recursion(arr,target,0,len(arr)-1))
end_time = time.time()
# Comparison of Linear and Binary
time_taken = end_time - start_time
time_taken1 = end_time1 - start_time1
time_taken2 = end_time2 - start_time2
print(f"ARR:{arr} and Target:{target}")
print(f"Time taken for binary_search_recursion: {time_taken:.6f} seconds")
print(f"Time taken for binary_search: {time_taken1:.6f} seconds")
print(f"Time taken for linear_search: {time_taken2:.6f} seconds")
""" 

# Sorting Algo:
# Algo Name   Best Case   Worst Case
# Bubble      :O(n)       O(n^2)
# Selections  :O(n^2)     O(n^2)
# Inserstion  :O(n)       O(n^2) 
# Merge       :O(nlogn)   O(nlogn)
# Quick       :O(nlogn)   O(n^2)
# Radix       
# Heap        :O(nlogn)   O(nlogn)
# TImsort     :O(n)       O(nlog)


# Bubble sort:
# Repatedely Swaps with the Adjectent Or Beside Values until out of order of elements
# Repeat for n-1 times

# def bubble_Sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr 

# Selection Sort:
# finding the smallest index in the array and make it as min value
# swap with less  value in the array
# repeat for all postions 
# [20,10,14,37,14]
# def Selection_Sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index = j
#                 arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr 


# Insertion SOrt: 
# 1.Take an element
# 2.COmapre with left values
# 3.shift larger element right
# 4.inser at the correct postion

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key




# def merge_sort(arr):
#     if len(arr) <=1:
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])
#     right=merge_sort(arr[mid:])
#     return merge(left, right)
# def merge(left,right):
#     result=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# arr1=[1,5,8,2,3,6,0,7]
# print(merge_sort(arr1))

# def merge_sort(arr, depth=0):
#     indent = "  " * depth  
#     print(f"{indent}merge_sort({arr})")
    
#     if len(arr) <= 1:
#         print(f"{indent}Returning single element: {arr}")
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid], depth + 1)
#     right = merge_sort(arr[mid:], depth + 1)

#     merged = merge(left, right, depth + 1)
#     print(f"{indent}Merged {left} and {right} into {merged}")
#     return merged

# def merge(left, right, depth=0):
#     indent = "  " * depth
#     print(f"{indent}Merging: {left} + {right}")
    
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             print(f"{indent}Appending {left[i]} from left")
#             i += 1
#         else:
#             result.append(right[j])
#             print(f"{indent}Appending {right[j]} from right")
#             j += 1

#     if i < len(left):
#         print(f"{indent}Extending remaining left: {left[i:]}")
#     if j < len(right):
#         print(f"{indent}Extending remaining right: {right[j:]}")
#     result.extend(left[i:])
#     result.extend(right[j:])

#     print(f"{indent}Result of merge: {result}")
#     return result

# arr1 = [1, 5, 8, 2, 3, 6, 0, 7]
# print("\nFinal Sorted Output:")
# print(merge_sort(arr1))


# Quick SOrt:
# Pick A Pivot Elemt(mid/strat/last/Random)
# divide the arry into :
#     left and right
# Left: Allelement<pivot
# RIght:all elements >=pivot

# Recuisulsy apply quick sort to left and right subarryas
# combine left+piovt+right 





# def quick_sort(arr):
#     if len(arr)<=1:
#         return arr
#     pivot=arr[0]
#     left=[x for x in arr[1:] if x<pivot]
#     right=[x for x in arr[1:] if x>=pivot]
#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr=[1,9,7,8,5,0,-1]
# print(quick_sort(arr))



