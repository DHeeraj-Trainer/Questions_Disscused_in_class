#Linked List

# A Linked List is a linear 
# data structure where elements 
# are connected using pointers (references).

# Unlike arrays:

# Arrays store elements in contiguous memory.
# Linked Lists store elements anywhere in memory.
# Each node stores:
        # Data
        # Reference to next node
# 10->20->30->40->50->None
# Node:
# +-------+--------+
# | data  | next   |
# +-------+--------+

# arr=[10,20,30,40]
# arr.insert(0,15)
#O(n)
# 10->20->30->40->50->None
# 15->10->20->30->40->50->None
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(5)
n2=Node(4)
n3=Node(3)
n4=Node(2)
n5=Node(1)
# print(n1)
# print(n1.data)
# print(n1.next)
# print("-----------------------------")
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
# print(n1)
# print(n1.data)
# print(n1.next.next.next.next)
# nodes=[n1,n2,n3,n4,n5]
# for i in nodes:
#     print(i.data,"->",end=" ")
# print("None")
# current=n1
# print("Start->")
# while current:
#     print(current.data,"->",end="")
#     current=current.next
# print("None")


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_at_head(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def insert_after_value(self,target,data):
        current=self.head
        while current:
            if current.data==target:
                new_node=Node(data)
                new_node.next=current.next
                current.next=new_node
                return
            current=current.next
        print(f"Values {target} not found")
    def delete_at_head(self):
        if self.head is None:
            print("list is empty")
            return
        self.head=self.head.next
    def delete_at_tail(self):
        if self.head is None:
            print("list is empty")
            return
        #only 1 node
        if self.head.next is None:
            self.head=None
            return 
        #mutiple nodes
        curr=self.head
        while curr.next.next:
            curr=curr.next
        curr.next=None

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
    def __str__(self):
        current,nodes=self.head,[]
        while current:
            nodes.append(str(current.data))
            current=current.next
        return ("->".join(nodes)+"->None")
ll=SLL()
print(ll.head)
# ll.insert_at_head(5)
# ll.insert_at_head(7)
# ll.insert_at_head(8)
ll.insert_end(5)
ll.insert_end(7)
ll.insert_end(8)
ll.display()
print(ll)
