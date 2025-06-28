
import numpy as np

# 1. array() function
# Creates a NumPy array from a regular Python list or tuple.
# arr1 = np.array([1, 2, 3, 4, 5])
# print("array():", arr1)

# 2. linspace() function
# Returns evenly spaced numbers over a specified interval.
# Arguments: start, stop, number of samples
# arr2 = np.linspace(0, 10, 5)
# print("linspace():", arr2)

# 3. logspace() function
# Returns numbers spaced evenly on a log scale.
# Arguments: start exponent, stop exponent, number of samples
# 10^1 to 10^3 (i.e., 10 to 1000)
# arr3 = np.logspace(1, 3, 3)
# print("logspace():", arr3)

# 4. arange() function
# Returns evenly spaced values within a given interval.
# Arguments: start, stop (exclusive), step
# arr4 = np.arange(1, 10, 2)
# print("arange():", arr4)

# 5. zeros() function
# Returns a new array of given shape and type, filled with zeros.
# Argument: tuple for shape
# arr5 = np.zeros((2, 3))
# print("zeros():\n", arr5)

# 6. ones() function
# Returns a new array of given shape and type, filled with ones.
# Argument: tuple for shape
# arr6 = np.ones((2, 3))
# print("ones():\n", arr6)

import numpy as np



#QUestions


# 1. Create a 1D NumPy Array
# Problem: Create a 1D array with values from 0 to 9.
# Expected Output: [0 1 2 3 4 5 6 7 8 9]

# 2. Create a 2D Array with Zeros
# Problem: Create a 3x4 NumPy array filled with zeros.
# Expected Output: A 3x4 matrix of all zeros


# 3. Create an Array with a Specific Step
# Problem: Generate a NumPy array from 5 to 50 with step 5.
# Expected Output: [ 5 10 15 20 25 30 35 40 45]


# 4. Create Evenly Spaced Array
# Problem: Generate 6 evenly spaced values from 0 to 1.
# Expected Output: [0.  0.2 0.4 0.6 0.8 1. ]


# 5. Reshape an Array
# Problem: Create a 1D array of 12 elements and reshape to 3x4.
# Expected Output: 3x4 matrix with values 1 to 12


# 6. Perform Element-wise Addition
# Problem: Add [1,2,3,4,5] and [10,20,30,40,50] element-wise.
# Expected Output: [11 22 33 44 55]


# 7. Multiply Two Matrices
# Problem: Multiply two 2x2 matrices using matrix multiplication.
# Expected Output: [[19 22] [43 50]]


# 8. Slice a 2D Array
# Problem: Extract the second row from a 3x3 matrix.
# Expected Output: [4 5 6]


# 9. Filter Values Greater Than a Number
# Problem: Return elements > 10 from array.
# Input: [3, 12, 5, 18, 7]
# Expected Output: [12 18]


# 10. Find Max and Min in Array
# Problem: Find max and min from the array.
# Input: [4, 9, 2, 7, 1]
# Expected Output: Max=9, Min=1


# 11. Replace Negative Values with Zero
# Problem: Replace all negative values with 0.
# Input: [-1, 2, -3, 4]
# Expected Output: [0 2 0 4]


# 12. Create Identity Matrix
# Problem: Create a 4x4 identity matrix.
# Expected Output: Diagonal of ones


# 13. Create Logarithmic Space Array
# Problem: Create array of 5 values from 10^1 to 10^5.
# Expected Output: [1.e+01 1.e+02 1.e+03 1.e+04 1.e+05]


# 14. Stack Two Arrays Vertically and Horizontally
# Problem: Stack arrays [1, 2, 3] and [4, 5, 6] vertically and horizontally.


# 15. Flatten a Multidimensional Array
# Problem: Convert a 2D array into 1D.
# Input: [[1, 2], [3, 4]]
# Expected Output: [1 2 3 4]




# 1. Reverse a 1D Array
# Problem: Reverse the elements of the array.
# Input: [1, 2, 3, 4, 5]
# Expected Output: [5 4 3 2 1]


# 2. Get Diagonal of a Matrix
# Problem: Extract the diagonal from a 3x3 matrix.
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Expected Output: [1 5 9]


# 3. Sum Across Axis
# Problem: Sum elements column-wise in a 2D array.
# Expected Output: [12 15 18]


# 4. Boolean Indexing
# Problem: Extract elements greater than 50.
# Input: [34, 67, 89, 12, 50]
# Expected Output: [67 89]


# 5. Replace All Even Numbers with -1
# Input: [10, 15, 20, 25, 30]
# Output: [-1, 15, -1, 25, -1]


# 6. Find Duplicate Elements
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [2 4]


# 7. Sort a 2D Array by a Column
# Problem: Sort the array by the second column.


# 8. Find Unique Elements
# Problem: Extract unique values from the array.
# Input: [1, 2, 2, 3, 3, 4]
# Output: [1 2 3 4]


# 9. Normalize an Array (Min-Max Scaling)
# Problem: Scale all values between 0 and 1.
# Input: [10, 20, 30]
# Output: [0. 0.5 1.]


# 10. Create a Checkerboard Pattern
# Problem: Create an 8x8 array with a checkerboard pattern (0s and 1s).


# 11. Convert Degrees to Radians
# Input: [0, 30, 45, 60, 90]
# Output: Radians array


# 12. Find Row with Maximum Sum
# Input: [[1, 2], [3, 4], [5, 0]]
# Output: Row [3 4]


# 13. Broadcast a Row to 2D Array
# Problem: Create a 5x3 array where each row is [1, 2, 3]


# 14. Find Indices of Max Element
# Input: [10, 25, 3, 99, 57]
# Output: Index of 99 → 3


# 15. Pad a 2D Array with Zeros
# Problem: Pad the 2D array with a 1-pixel wide border of zeros.




'''
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matrix A:\n", A)

# 1. Creation Functions
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))
identity = np.eye(3)
full = np.full((3, 3), 7)
print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)
print("\nIdentity Matrix:\n", identity)
print("\nFull of 7s:\n", full)

# 2. Array Attributes
print("\nShape:", A.shape)
print("Size:", A.size)
print("Dimensions:", A.ndim)
print("Data type:", A.dtype)

# 3. Reshaping & Manipulating
flattened = A.flatten()
reshaped = A.reshape(1, 9)
transposed = A.T
print("\nFlattened:", flattened)
print("Reshaped (1x9):", reshaped)
print("Transposed:\n", transposed)

# 4. Indexing, Slicing, Filtering
print("\nElement at [1,2]:", A[1,2])
print("Second row:", A[1])
print("All rows, 2nd column:", A[:,1])
print("Elements > 5:", A[A > 5])

# 5. Mathematical Operations
print("\nA * 2:\n", A * 2)
print("A squared:\n", np.power(A, 2))
print("Square root:\n", np.sqrt(A))

# 6. Statistical Functions
print("\nMax value:", np.max(A))
print("Min value:", np.min(A))
print("Mean:", np.mean(A))
print("Sum:", np.sum(A))
print("Standard Deviation:", np.std(A))

# 7. Sorting and Searching
sorted_A = np.sort(A, axis=1)
indices = np.argmax(A, axis=1)
print("\nSorted rows:\n", sorted_A)
print("Indices of max in each row:", indices)

# 8. Logical & Comparison Operations
print("\nWhere A > 4:\n", np.where(A > 4))
print("Any > 8:", np.any(A > 8))
print("All > 0:", np.all(A > 0))

# 9. Copying and Views
B = A.copy()
B[0,0] = 100
print("\nCopy B (modified):\n", B)
print("Original A:\n", A)

# 10. Special Utilities
clipped = np.clip(A, 3, 7)
padded = np.pad(A, pad_width=1, mode='constant', constant_values=0)
deleted = np.delete(A, 1, axis=0)
inserted = np.insert(A, 1, [10, 11, 12], axis=0)
print("\nClipped (3-7):\n", clipped)
print("Padded:\n", padded)
print("Row 1 deleted:\n", deleted)
print("Row inserted at index 1:\n", inserted)
'''
import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])
# print(arr.reshape(3, 3))
# print(arr)

# sub_array=arr[1:3,0:2]
# sub_array=arr[-1::,-2::-1]
# print(sub_array)







import numpy as np
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

# Extract the second and third rows, and only the first two columns

# Slice the last row in reverse order (right to left)
# print(arr[2,::-1])
# print(arr[-1,::-1])
# Extract all elements from arr that are greater than 50
# Replace all elements in arr that are >= 100 with 0
# arr[arr>=100]=0
# print(arr)
# Extract all elements from rows where the first column is greater than 20.
# print(arr[arr[:,0]>20])
# Extract all rows where any element is greater than 100.
res=arr[np.any(arr>100,axis=1)]
# print(res)
# Extract all elements that are either less than 40 or greater than 100.
# print(arr[(arr<40) | (arr>100)])
# Set all values in the second row to 0 where values are greater than 60.
# arr[1][arr[1]>60]=0
# print(arr)

# print(arr.shape)
# Print all elements using loops
# for row in arr:
    # for elem in row:
    #     print(elem,end=" ")
    # print()
rows,col=arr.shape
# for i in range(rows):
#     for j in range(col):
        # print(arr[i][j])
# print only diagonal elements
# for i in range(rows):
#     for j in range(col):
#         if i==j:
#             print(arr[i][j])
# for i in range(min(rows,col)):
#     print(arr[i][i])
# # Write a loop to calculate the each row sum
# for i in range(rows):
#     row_sum=0
#     for j in range(col):
#         row_sum+=arr[i][j]
#     print(row_sum)
# Create a new array that contains the square of each element 
# squares_arr=np.zeros_like(arr)
# for i in range(rows):
#     for j in range(col):
#         squares_arr[i][j]=arr[i][j]**2
# print(squares_arr)


# print the value like the output :
# o/p:  
# 10 50 90
# 20 90 100
# 30 70 110
# 40 80 120

for j in range(col):
    for i in range(rows):
        print(arr[i,j],end=" ")
    print()
