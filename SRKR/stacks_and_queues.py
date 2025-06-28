class Stack(object):
    def __init__(self,items):
        self.items = []
    
    def set_push(self, item):
        self.items.append(item)
    
    def get_pop(self):
        return self.items.pop()
    
    def get_peek(self):
        return self.items[-1]
    
    def Is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)



class Queue(object):
    def __init__(self,items):
        self.items = []
    
    def set_push(self, item):
        self.items.append(item)
    
    def get_pop(self):
        return self.items.pop(0)
    
    def get_peek(self):
        return self.items[0]
    
    def Is_empty(self):
        return len(self.items)==0
    
    def size(self):
        return len(self.items)







    # Implement a first in first out (FIFO) queue using only two stacks.

    # Example Test Cases:
    # Input: push(1), push(2), peek(), pop(), empty() -> Output: 1, 1, False


# 1. Valid Parentheses
"""
Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example Test Cases:
Input: "()[]{}" -> Output: True
Input: "(]" -> Output: False
"""


# 2. Min Stack
"""
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Example Test Cases:
Input: push(-2), push(0), push(-3), getMin() -> Output: -3
Input: pop(), top(), getMin() -> Output: 0, -2
"""


# 3. First Unique Character in a String
"""
Problem:
Given a string, find the first non-repeating character and return its index.

Example Test Cases:
Input: "leetcode" -> Output: 0
Input: "loveleetcode" -> Output: 2
"""

# 4. Moving Average from Data Stream
"""
Problem:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example Test Cases:
Input: [1, 10, 3, 5], size = 3 -> Output: 1.0, 5.5, 4.67, 6.0

m = MovingAverage(3)  # Window size is 3

print(m.next(1))      # → 1.0       (Window: [1])
print(m.next(10))     # → (1+10)/2 = 5.5  (Window: [1,10])
print(m.next(3))      # → (1+10+3)/3 = 4.67 (Window: [1,10,3])
print(m.next(5))      # → (10+3+5)/3 = 6.0 (Window slides forward: [10,3,5])
"""


## Palindrome Checker*

### 📘 Problem:

# Check whether a given string is a **palindrome** (reads the same forwards and backwards), **ignoring spaces, case, and punctuation**. Use a **deque** to solve it efficiently.

### 🧪 Example Test Cases:


# Input: "racecar"            → Output: True  
# Input: "A man a plan a canal Panama" → Output: True  
# Input: "hello"              → Output: False




## Reverse Queue

### 📘 Problem:

# Given a queue, **reverse its elements** using a **stack**.

### 🧪 Example Test Case:

# Input Queue: [1, 2, 3, 4]  
# Output: [4, 3, 2, 1]



# 5. Evaluate Reverse Polish Notation
"""
Problem:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators: +, -, *, /

Example Test Cases:
Input: ["2", "1", "+", "3", "*"] -> Output: 9
Input: ["4", "13", "5", "/", "+"] -> Output: 6
"""
def evalu(tokens):
    stack=[]
    for token in tokens:
        if token in "+-/*":
            b=stack.pop()
            a=stack.pop()
            if token =='+':
                stack.append(a+b)
            elif token =="-":
                stack.append(a-b)
            elif token =="*":
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        else:
            stack.append(int(token))
    return stack[0]

token=["2", "1", "+", "3", "*"]
print(evalu(token))



# 6. Implement Queue using Stacks
"""
Problem:
Implement a first in first out (FIFO) queue using only two stacks.

Example Test Cases:
Input: push(1), push(2), peek(), pop(), empty() -> Output: 1, 1, False
"""

# 7. Daily Temperatures
"""
Problem:
Given a list of daily temperatures, return a list such that, for each day,
you tell how many days you would have to wait until a warmer temperature.

Example Test Cases:
Input: [73, 74, 75, 71, 69, 72, 76, 73] -> Output: [1, 1, 4, 2, 1, 1, 0, 0]


# 8. Next Greater Element (Circular)
"""
# Problem:
# Given a circular array, return the next greater element for each element.

# Example Test Cases:
# Input: [1,2,1] -> Output: [2,-1,2]


# 9. Sliding Window Maximum
"""
Problem:
Given an array and an integer k, return the max value in each sliding 
window of size k.

Example Test Cases:
Input: [1,3,-1,-3,5,3,6,7], k = 3 -> Output: [3,3,5,5,6,7]
"""


# 10. Rotting Oranges
"""
Problem:
Given a grid, each cell can be empty, contain a fresh orange, or a rotten orange.
Each minute, any fresh orange that is adjacent to a rotten one becomes rotten.
Return the minimum number of minutes that must elapse until no fresh orange remains.

Example Test Cases:
Input: [[2,1,1],[1,1,0],[0,1,1]] -> Output: 4
"""
