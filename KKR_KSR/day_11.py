<!-- def quick(arr):
	if len(arr)<=1:return arr
	pivot=arr[len(arr)//2]
	l=[x for x in arr if x<pivot]
	r=[x for x in arr if x>pivot]
	m=[x for x in arr if x==pivot]
	return quick(l)+m+quick(r)
[8,3,5,1,9,6,2,7]
def quick(arr):
	if len(arr)<=1:return arr
	pivot=arr[len(arr)//2]
	l,r,m=[],[],[]
	for i in arr :
		if i<pivot:
			l.append(i)[8351627]
	for i in arr :
		if i>pivot:
			r.append(i)[]
	for i in arr:
		if i==pivot:m.append(i)[9]
	return quick(l)+m+quick(r) 
+[9]+[]

[8351627];p=1
l=[],r=[835627]]m=[1]
[]+[1]+[835627]
835627;p=5;l=[32]+[5]+[867]
([]+[2]+[3])+[5]+([]+[6]+[87])
([]+[2]+[3])+[5]+([]+[6]+[]+[7]+[8])
[]+[1]+[]+[2]+[3])+[5]+([]+[6]+[]+[7]+[8])
[]+[1]+[]+[2]+[3])+[5]+([]+[6]+[]+[7]+[8])+[9]+[]

[1,2,3,5,6,7,8,9]


Bubble sort
  8,3,5,1,9,6,2,7
3 8 5 1 9 6 2 7
3 5 8 1 9 6 2 7
1 3 5 8 9 6 2 7
1 3 5 8 9 6 2 7
1 3 5 6 8 9 2 7
1 2 3 5 6 8 9 7
1 2 3 5 6 7 8 9



merge sort 

8,3,5,1,9,6,2,7
8 3 5 1 9 6 2 7
3 8 1 5 9 6 2 7
1 8 3 5
1 3 8 5
1 3 5 8 9 6 2 7
        6 9 2 7
        6 9 2 7
        2 9 6 7
         2 6 9 7
        2 6 7 9
1  2 5 8 3 6 7 9
1 2  3 8 5 6 7 9
1 2 3  5 8 6 7 9
12356879
12356789
12356789


 -->






"""
SORTING ALGORITHMS CHEAT SHEET
===============================================================================================

| Algorithm      | Best Time  | Avg Time   | Worst Time | Space    | Stable | Real-World Use Case |
|---------------|------------|------------|------------|----------|--------|---------------------|
| Bubble Sort   | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    | Learning, tiny datasets |
| Selection Sort| O(n²)      | O(n²)      | O(n²)      | O(1)     | No     | When memory writes are costly |
| Insertion Sort| O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    | Nearly sorted data |
| Merge Sort    | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    | Databases, external sorting |
| Quick Sort    | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     | General-purpose sorting |
| Heap Sort     | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     | Priority queues |
| Counting Sort | O(n+k)     | O(n+k)     | O(n+k)     | O(k)     | Yes    | Limited-range integers |
| Radix Sort    | O(nk)      | O(nk)      | O(nk)      | O(n+k)   | Yes    | Phone numbers, IDs |
| Bucket Sort   | O(n+k)     | O(n+k)     | O(n²)      | O(n)     | Depends| Uniform distributions |
| Tim Sort      | O(n)       | O(n log n) | O(n log n) | O(n)     | Yes    | Python sorted(), list.sort() |
| Shell Sort    | O(n log n) | ~O(n^1.5)  | O(n²)      | O(1)     | No     | Medium-sized datasets |
| Tree Sort     | O(n log n) | O(n log n) | O(n²)      | O(n)     | Depends| Frequent insertions |

===============================================================================================

BUBBLE SORT
-----------
How it works:
- Compare adjacent elements
- Swap if left > right
- Largest element bubbles to the end after each pass

SELECTION SORT
--------------
How it works:
- Find minimum element
- Swap with current position
- Repeat for remaining array

INSERTION SORT
--------------
How it works:
- Maintain sorted portion on left
- Insert each new element into correct position

MERGE SORT
----------
How it works:
- Divide array into halves
- Recursively sort halves
- Merge sorted halves

QUICK SORT
----------
How it works:
- Choose pivot
- Partition around pivot
- Recursively sort left and right partitions

HEAP SORT
---------
How it works:
- Build heap
- Repeatedly extract root element

COUNTING SORT
-------------
How it works:
- Count occurrences
- Reconstruct sorted array

RADIX SORT
----------
How it works:
- Sort digit by digit
- Uses a stable sort internally

BUCKET SORT
-----------
How it works:
- Distribute elements into buckets
- Sort buckets individually
- Merge buckets

TIM SORT
--------
How it works:
- Hybrid of Merge Sort + Insertion Sort
- Used internally by Python

SHELL SORT
----------
How it works:
- Compare far-apart elements using gaps
- Gradually reduce gap

TREE SORT
---------
How it works:
- Insert into BST
- In-order traversal gives sorted order

INTERVIEW FAVORITES:
1. Quick Sort
2. Merge Sort
3. Insertion Sort
4. Heap Sort
5. Tim Sort (Python Built-in)

PYTHON BUILT-IN:
sorted(arr)      # Returns new sorted list
arr.sort()       # Sorts in-place

Python uses Tim Sort internally.
"""




