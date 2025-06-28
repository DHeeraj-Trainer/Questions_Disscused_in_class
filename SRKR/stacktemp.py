# class Stack(object):
#     def __init__(self):
#         self.items = []
    
#     def is_empty(self):
#         return len(self.items)==0
    
#     def push(self, item):
#         self.items.append(item)
#         return self.items
    
#     def pop(self):
#         raise IndexError("Stack is empty")
#         return self.items[-1]
#         self.items.pop()
    
#     def get_peek(self):
#         raise IndexError("Stack is empty")

#         return self.items[-1] 
    
#     def get_size(self):
#         raise IndexError("Stack is empty")
#         return len(self.items)
    

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



def is_valid(st):
    stack=[]
    pairs={')':'(','}':'{',"]":"["}
    for ch in st:
        if ch in ['(','{',"["]:
            stack.append(ch)
        elif ch in [')','}',"]"]:
            if not stack:
                return False
            top=stack.pop()
            if top!=pairs[ch]:
                return False
        else:return False
    return len(stack)==0

print(is_valid("(){}[]"))
print(is_valid("{[()]}"))
print(is_valid("[)]]"))

"""
"""
# Implement a first in first out (FIFO) queue using only two stacks.

# Example Test Cases:
# Input: push(1), push(2), peek(), pop(), empty() -> Output: 1, 1, False



class Myqueue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]
    
    def push(self, x):
        self.in_stack.append(x)
        print (self.in_stack)
    
    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    
    def get_peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] 

    def is_empty(self):
        return not self.in_stack and not self.out_stack              


queue=Myqueue()
queue.push(5)
queue.push(6)
queue.push(7)
print(queue.pop())
print(queue.get_peek())
"""

# 3. First Unique Character in a String
"""
Problem:
Given a string, find the first non-repeating character and 
return its index.

Example Test Cases:
Input: "leetcode" -> Output: 0
Input: "loveleetcode" -> Output: 2



def freuq_count(s:str):
    freq={}
    queue=[]

    
    for i,ch in enumerate(s):
        if ch not in freq:
            freq[ch]=1
            queue.append((ch,i))
        else:
            freq[ch]+=1

    i=0
    for ch in s:
        if ch not in freq:
            freq[ch]=1
            queue.append((ch,i))
        else:
            freq[ch]+=1
        i+=1


    # print(freq,queue)
    for ch ,idx in queue:
        if freq[ch] == 1:
            return idx
    return -1

print(freuq_count("leetcode"))
"""



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

from collections import deque
class Movingavg(object):
    def __init__(self, size: int):
        self.size = size
        self.q=deque()
        self.total=0
    def next(self,value:int):
        self.q.append(value)
        self.total+=value
        if len(self.q)>self.size:
            self.total-=self.q.popleft()
        return self.total/len(self.q)
m = Movingavg(3)  # Window size is 3

print(m.next(1))      # → 1.0       (Window: [1])
print(m.next(10))     # → (1+10)/2 = 5.5  (Window: [1,10])
print(m.next(3))      # → (1+10+3)/3 = 4.67 (Window: [1,10,3])
print(m.next(5))      # → (10+3+5)/3 = 6.0 