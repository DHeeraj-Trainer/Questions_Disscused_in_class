""" 
### 1. Reverse a Linked List
# Problem Statement: Reverse a singly linked list.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> None
# Output: 4 -> 3 -> 2 -> 1 -> None

""" 


class Node:
    def __init__(self, val,):
        self.val = val
        self.next=None
    def revers_list(head):
        prev=None
        curr=head
        while curr:
            next_node=curr.next   #Store Next Node
            curr.next=prev#reverse the link
            prev=curr#move forward
            curr=next_node#curr moe formward
        return prev

# prev=None
# curr=1
# next_node= 2
# curr.next=None
# prev=1
# curr=2

# 1>None    

# next_node= 3
# curr.next=1
# prev=2
# curr=3

# 2>1>None







""" 
### 2. Detect a Loop in a Linked List
# Problem Statement: Determine if a cycle exists.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
# Output: True
 
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def has_cycle(head):
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f:
                s=head
                while s!=f:
                    s=s.next
                    f=f.next
                return s
        return None




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2  

if has_cycle(node1):
    print("Cycle detected in the linked list.")
else:
    print("No cycle in the linked list.")
"""



""" 
### 3. Find the Middle of a Linked List
# Problem Statement: Find the middle node of a linked list.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 3

""" 

""" 
### 4. Count the number of nodes
# Problem Statement: Count total nodes in a linked list.
# Test Case:
# Input: 10 -> 20 -> 30 -> None
# Output: 3
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")

    def count_nodes(self):
        count=0
        curr=self.head
        while curr:
            count+=1
            curr=curr.next
        return count

    def is_palidrome(self):
        vals=[]
        curr=self.head
        while curr:
            vals.append(curr.data)
            curr=curr.next
        return vals==vals[::-1]
    

ll=LinkedList()
values=[10,20,50,20,10]
for val in values:
    ll.insert_end(val)
print("Linked List")
ll.display()
print(f"TOtal no of nodes:{ll.count_nodes()}")
print(f"Is Palindrome:{ll.is_palidrome()}")

""" 
### 5. Check if a Linked List is Palindrome
# Problem Statement: Check if linked list is a palindrome.
# Test Case:
# Input: 1 -> 2 -> 3 -> 2 -> 1
# Output: True

"""

""" 
### 6. Remove Duplicates from Unsorted Linked List
# Problem Statement: Remove duplicates from an unsorted list.
# Test Case:
# Input: 1 -> 3 -> 2 -> 3 -> 1
# Output: 1 -> 3 -> 2

""" 
""" 
### 7. Remove N-th Node from End
# Problem Statement: Remove the N-th node from end of list.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 5, N = 2
# Output: 1 -> 2 -> 3 -> 5

""" 

""" 
### 8. Merge Two Sorted Lists
# Problem Statement: Merge two sorted linked lists.
# Test Case:
# Input: 1 -> 3 -> 5 and 2 -> 4 -> 6
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
""" 


""" 


### 10. Delete Node with Only Access to that Node
# Problem Statement: Delete given node without head access.
# Test Case:
# Input: Node with value 3 in 1 -> 2 -> 3 -> 4
# Output: 1 -> 2 -> 4
""" 

""" 
### 11. Rotate a Linked List
# Problem Statement: Rotate list to the right by k places.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 4 -> 5 -> 1 -> 2 -> 3

""" 

""" 

### 13. Flatten a Multilevel Linked List
# Problem Statement: Flatten linked list with child pointers.
# Test Case: Custom structure, not applicable to basic singly list.
""" 
""" 
### 14. Clone a Linked List with Random Pointer
# Problem Statement: Clone nodes with next and random pointers.
# Test Case: Custom random pointer not supported here.
""" 
""" 
### 15. Sort a Linked List (Merge Sort)
# Problem Statement: Sort list in O(n log n) time.
# Test Case:
# Input: 4 -> 2 -> 1 -> 3
# Output: 1 -> 2 -> 3 -> 4
""" 
""" 


### 16. Reorder List
# Problem Statement: L0→Ln→L1→Ln-1...
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 5 -> 2 -> 4 -> 3

""" 
""" 

### 17. Detect and Remove Loop
# Problem Statement: Detect and remove loop.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4 -> 2 (loop)
# Output: Loop removed, list ends at 4

""" 
""" 


### 18. Pairwise Swap Nodes
# Problem Statement: Swap every two adjacent nodes.
# Test Case:
# Input: 1 -> 2 -> 3 -> 4
# Output: 2 -> 1 -> 4 -> 3

""" 
""" 


### 19. Segregate Even and Odd Nodes
# Problem Statement: Place even nodes before odd ones.
# Test Case:
# Input: 17 -> 15 -> 8 -> 9 -> 2 -> 4 -> 6
# Output: 8 -> 2 -> 4 -> 6 -> 17 -> 15 -> 9

""" 

# Define a basic Node class to support all examples
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
