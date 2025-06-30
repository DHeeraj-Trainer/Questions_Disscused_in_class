"""
FizzBuzz Twist

Problem Statement
Print numbers from 1 to 50. Replace multiples of 3 with `"Fog"`, multiples of 5 with `"Buzz"`, and multiples of both 3 and 5 with `"FogBuzz"`.

Test Cases


# Sample output fragments:
[... "Fog", ..., "Buzz", ..., "FogBuzz", ...]


* 3 → "Fog"
* 5 → "Buzz"
* 15 → "FogBuzz"

"""

def fizzbuzz_twist():
    for n in range(1, 51):
        output = ""
        if n % 3 == 0:
            output += "Fog"
        if n % 5 == 0:
            output += "Buzz"
        print(output or n)  




"""
*Step‑by‑step:*

1. Loop `n = 1…50`.
2. Build `output` if divisible by 3 and/or 5.
3. If nothing added, `or n` ensures the number itself prints.


### 2. Max Consecutive Ones

Problem Statement
Given a list of 0s and 1s, return the maximum number of consecutive 1s.

Test Cases


[1,1,0,1,1,1] → 3
[0,0,0] → 0
[1,1,1,1] → 4


Purpose
Count longest run of repeated values in a sequence.

"""


def max_consecutive_ones(nums):
    max_run = cur_run = 0
    for bit in nums:
        if bit == 1:
            cur_run += 1
            max_run = max(max_run, cur_run)
        else:
            cur_run = 0
    return max_run

"""
*Step‑by‑step:* increment `cur_run` on 1, reset on 0, track `max_run`.



### 3. Guess the Number (Interactive)

Problem Statement
Let the user guess a random integer between 1 and 100. After each guess, print `"Higher"`, `"Lower"`, or `"Correct!"` until they succeed.

No automated testcases—interactive.

Purpose
Practice loops, conditionals, and user input.

"""


import random

def guess_the_number():
    secret = random.randint(1, 100)
    while True:
        guess = int(input("Guess (1–100): "))
        if guess < secret:
            print("Higher")
        elif guess > secret:
            print("Lower")
        else:
            print("Correct!")
            break

"""
*Step‑by‑step:* continuously prompt, compare with secret, repeat until correct.

"""
"""

Closure Counter

Problem Statement
Write a function that returns another function which, when called, increases an internal count and returns it.

Test Cases


c = make_counter()
c() → 1
c() → 2


Purpose
Demonstrate closures capturing state.


"""

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

"""
*Step‑by‑step:* `count` is enclosed in `make_counter`, `nonlocal` allows modifying it inside `counter`.

 Lambda Sorting

Problem Statement
Given a list of `(a, b)` tuples, sort descending by the second item.

Test Cases


[(1,3),(2,2),(3,1)] → [(1,3),(2,2),(3,1)]
[(5,0),(4,10)] → [(4,10),(5,0)]


Purpose
Use lambda to customize sorting keys.

"""


def sort_by_second_desc(lst):
    return sorted(lst, key=lambda x: x[1], reverse=True)


"""
### 8. Generator Pipeline

Problem Statement
Use two generators: one filters out odd numbers, another squares the even numbers, yielding results lazily.

Test Cases


list(pipeline([1,2,3,4])) → [4, 16]


Purpose
Practice composing generators for lazy evaluation.


"""

def even_filter(nums):
    for x in nums:
        if x % 2 == 0:
            yield x

def squarer(nums):
    for x in nums:
        yield x * x

def pipeline(nums):
    return squarer(even_filter(nums))


"""
### 14. Sliding-Window Maximum

Problem Statement
Given array `nums` and window size `k`, return max of each window using O(n).

Test Cases


[1,3,-1,-3,5,3,6,7], k=3 → [3,3,5,5,6,7]


Purpose
Practice deque-based sliding window optimization.



"""
from collections import deque

def sliding_max(nums, k):
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


"""
### 15. Circular Buffer

Problem Statement
Implement a fixed-size ring buffer supporting `append`, `pop`, and overwrite-on-full behavior.

Test Cases


buf = RingBuffer(2)
buf.append(1)
buf.append(2)
buf.append(3)  # overwrites oldest
buf.pop() → 2
buf.pop() → 3


Purpose
Practice modular indexing and data structure design.

"""


class RingBuffer:
    def __init__(self, size):
        self.buf = [None] * size
        self.start = self.count = 0

    def append(self, val):
        idx = (self.start + self.count) % len(self.buf)
        self.buf[idx] = val
        if self.count < len(self.buf):
            self.count += 1
        else:
            self.start = (self.start + 1) % len(self.buf)

    def pop(self):
        if self.count == 0:
            raise IndexError("empty")
        val = self.buf[self.start]
        self.start = (self.start + 1) % len(self.buf)
        self.count -= 1
        return val


"""
 List vs Generator Memory

Problem Statement
Demonstrate via `sys.getsizeof` that a list comprehension uses more memory than an equivalent generator expression.

Test Cases


import sys
list_size = sys.getsizeof([i*i for i in range(106)])
gen_size = sys.getsizeof((i*i for i in range(106)))
# list_size >> gen_size


Purpose
Highlight memory efficiency of lazy evaluation.

"""
"""

### 18. Run–Length Encode and Decode

Problem Statement
Compress strings like `"aaabbcdddd"` → `"a3b2c1d4"`, and also decode back.

Test Cases


encode("aaabbcdddd") → "a3b2c1d4"
decode("a3b2c1d4") → "aaabbcdddd"


Purpose
Practice basic string parsing and run processing.

"""


def encode(s):
    res = []
    prev = s[0]; count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            res.append(prev + str(count))
            prev, count = c, 1
    res.append(prev + str(count))
    return ''.join(res)

def decode(s):
    res = []; i = 0
    while i < len(s):
        c = s[i]
        i += 1
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]; i += 1
        res.append(c * int(num))
    return ''.join(res)



"""
19. Isomorphic Strings

Problem Statement
Check if strings `s` and `t` are isomorphic: each character in `s` mappings one-to-one to characters in `t`.

Test Cases


("egg","add") → True  
("foo","bar") → False  
("paper","title") → True


Purpose
Validate bijective character mapping in parallel strings.

"""


def isomorphic(s, t):
    if len(s) != len(t):
        return False
    m1, m2 = {}, {}
    for cs, ct in zip(s, t):
        if m1.get(cs, ct) != ct or m2.get(ct, cs) != cs:
            return False
        m1[cs] = ct
        m2[ct] = cs
    return True



"""
20. Rotate String In-Place

Problem Statement
Rotate string (e.g. `"hello"`) left by k in place—without creating new string objects (swap blocks).

Test Cases


"hello", k=2 → "llohe"
"abcd", k=1 → "bcda"


Purpose
Show block reversal for in-place rotation.

"""


def rotate_left(s, k):
    lst = list(s)
    n = len(lst); k %= n
    def reverse(i, j):
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1; j -= 1

    reverse(0, k-1)
    reverse(k, n-1)
    reverse(0, n-1)
    return ''.join(lst)



"""
Stock Buy‑Sell Twice (Max Profit)

Problem Statement
Given a list of stock prices, compute max profit with at most two transactions (buy-sell).

Test Cases


[3,3,5,0,0,3,1,4] → 6
# Buy at 0, sell at 3, buy at 1, sell at 4 → 3 + 3 = 6


Purpose
Use dynamic programming with transaction-state tracking.

"""


def max_profit_two(prices):
    t1_cost = t2_cost = float('inf')
    t1_profit = t2_profit = 0
    for p in prices:
        t1_cost = min(t1_cost, p)
        t1_profit = max(t1_profit, p - t1_cost)
        t2_cost = min(t2_cost, p - t1_profit)
        t2_profit = max(t2_profit, p - t2_cost)
    return t2_profit

"""
*Step‑by‑step:* track minimal cost and maximal profit for first and second transaction.


## 4. Reorder List

Problem Statement
Given singly linked list `L: L0→L1→…→Ln`, reorder to: `L0→Ln→L1→Ln-1→…`.

Test Cases


1→2→3→4 → 1→4→2→3
1→2→3→4→5 → 1→5→2→4→3


Purpose
Practice list splitting, reversing, and merging.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow.next
    slow.next = None
    # reverse second half
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    # merge
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

"""
*Step‑by‑step:* split, reverse second half, then interleave nodes.

---

## 5. Restore IP Addresses

Problem Statement
Given a string of digits, return all valid IP addresses formatted by inserting three dots. Each part must be `0-255` with no leading zeros (except single ‘0’).

Test Cases


"25525511135" → ["255.255.11.135", "255.255.111.35"]
"0000" → ["0.0.0.0"]
"101023" → ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Purpose
Practice backtracking and string validation.

"""


def restore_ip(s):
    res = []
    def backtrack(start, parts):
        if len(parts) == 4:
            if start == len(s):
                res.append('.'.join(parts))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            part = s[start:start+length]
            if (part.startswith('0') and length > 1) or int(part) > 255:
                continue
            backtrack(start+length, parts+[part])
    backtrack(0, [])
    return res

"""
*Step‑by‑step:* recursively build 4 segments, validate each for range and format.

---

##

## 7. Daily Temperatures

Problem Statement
Given daily temperatures, return a list where each position indicates how many days you have to wait until a warmer temperature. If none, return 0.

Test Cases


[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]


Purpose
Use monotonic decreasing stack for next greater element problems.
"""



def daily_temperatures(T):
    n = len(T)
    res = [0] * n
    stack = []
    for i, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res

"""
*Step‑by‑step:* keep indices of unresolved temps, resolve when warmer seen.

---

## 8. Browser History Forward/Back

Problem Statement
Design a browser history with operations: `visit(url)`, `back(steps)`, `forward(steps)`.

Test Cases


h = BrowserHistory("a.com")
h.visit("b.com")
h.visit("c.com")
h.back(1) → "b.com"
h.back(1) → "a.com"
h.forward(1) → "b.com"
h.visit("d.com")
h.forward(2) → "d.com"
h.back(2) → "a.com"
h.back(7) → "a.com"


Purpose
Practice using stacks or list with pointer manipulation.

"""


class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url):
        self.history = self.history[:self.cur+1]
        self.history.append(url)
        self.cur += 1

    def back(self, steps):
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps):
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]


"""
*Step‑by‑step:* maintain list, current index; truncate forward history on visit.

---

## 9. Infix → Postfix Conversion

Problem Statement
Convert arithmetic expression in infix notation (with operators +, -, \*, /, parentheses) to postfix (Reverse Polish Notation).

Test Cases


"a+b*c" → "a b c * +"
"(a+b)*c" → "a b + c *"


Purpose
Implement Shunting Yard algorithm using operator stack.
"""



def infix_to_postfix(expr):
    prec = {'+':1,'-':1,'*':2,'/':2}
    output = []
    stack = []
    tokens = list(expr)
    for t in tokens:
        if t.isalnum():
            output.append(t)
        elif t in prec:
            while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[t]:
                output.append(stack.pop())
            stack.append(t)
        elif t == '(':
            stack.append(t)
        elif t == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ' '.join(output)








