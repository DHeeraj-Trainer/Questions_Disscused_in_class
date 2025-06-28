import time
# import sys

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = 995
# start_time = time.time()
# initial_memory = sys.getsizeof(factorial)
# factorial_result = factorial(n)
# end_time = time.time()
# final_memory = sys.getsizeof(factorial)

# time_taken = end_time - start_time
# space_used = final_memory - initial_memory

# print(f"\nFactorial of {n} is: {factorial_result}")
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

"""
SOrting
"""

# Bubble Sort 
# Reapatedly swap the adjecnt /next element until out of order of elements
# repeat n-1 times
# Best Case:O(1) worst Case:O(n^2)

arr=[1,5,7,8,2,3,6,220,7,8,2,3,6,14,7,8,2,3,6]

# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr

# print(bubble_sort(arr))



# Selection Sort:
# Find the smallest element in unsort PendingDeprecationWarning
# swap from start
# repeat with all postions
    
# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#                 arr[i],arr[min_index]=arr[min_index],arr[i]
#         return arr



# Insertion SOrt:
# Take element
# compare to left elemts
# shift larger elements to right
# inser at correct postions
# Best Case:O(n) worst Case:O(n^2)


# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr






# def merge_sort(arr):
#     if len(arr)<= 1:
#         return arr
#     mid=len(arr)//2
#     left_half=merge_sort(arr[:mid])
#     # print(left)
#     right_half=merge_sort(arr[mid:])
#     # print(right)
#     return merge(left_half, right_half)


# def merge(left,right):
#     result=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             result.append(left[i])
#             print(left)
#             i+=1
#         else:
#             result.append(right[j])
#             print(right)
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr=[1,2,12,8,0,9,11,15]
# print(merge_sort(arr))

# Quick sort
# CHosse one pivot element(Start,stop,mid value,random)
# partion array into 
#     left and right 
#     Left: all elements<pivot
#     right :all elements>=pivot
# recurisualy apply quick sort to the left and right subarrys
# combine left+pivot+right

# def quick_sort(arr):
#     if len(arr) <=1:
#         return arr
#     pivot=arr[0]
#     left=[z for z in arr[1:] if z<pivot]
#     right=[z for z in arr[1:]if z>=pivot]

#     return quick_sort(left)+[pivot]+quick_sort(right)
# arr=[1,5,8,2,3,6,0,7]
# print(quick_sort(arr))





