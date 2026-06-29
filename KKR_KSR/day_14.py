class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after_value(self, target, data):
        current = self.head
        while current and current.data != target:
            current = current.next

        if current is None:
            print("Value not found")
            return

        new_node = Node(data)

        new_node.prev = current
        new_node.next = current.next

        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node

    def delete_start(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def forward_traversal(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    def backward_traversal(self):
        current = self.tail

        while current:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class CircularLinkedList:
#     def __init__(self):
#         self.tail = None

# insert 10
# self.tail=new
# new.next=new
# 10
# ↑
# └── points to itself
# 10 -> 20
# ↑     ↓
# └─────┘head=10;tail=20
# new.next=(20.next=10.next)=self.tail.next
# 10.next=20 ->  self.tail.next=new
# self.tail=new;tail=20;head=10
# insert 30 at end 
# 10 -> 20 -> 30-T
# ↑           ↓
# └───────────┘
# 30.next=20.next 
# 20.next=30
# tail=30 tail=30,head=10
# inser 5 at head
# 5.next=30.next
# 30.next=5
# 5-> 10 -> 20 -> 30-T
# ↑                 ↓
# └─────────────────┘
# tail=30;head=5
# prev=None
# curr=self.tail.next
# while True:
#     if current.data==value:
#         #only one node
#         if current==self.tail and current==self.tail.next:
#             self.tail=None
#         #del head node
#         elif curret==self.tail.next:
#             self.tail.next=curr.next
#         #delete tail
#         elif current ==self.tail:
#             prev.next=current.next  20.next=30.next=5
#             self.tail=prev 
#         else:
#             prev.next=current.next
#         return
#     prev=current
#     current=current.next
#     if curre==self.tail.next:break




# 5 -> 10 -> 20 -> 30
# ^              |
# |              v
# +--------------+
# tail = 30

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert_head(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    def insert_tail(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, value, data):
        if self.tail is None:
            return

        current = self.tail.next

        while True:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

                if current == self.tail:
                    self.tail = new_node
                return

            current = current.next

            if current == self.tail.next:
                return

    def delete_by_value(self, value):
        if self.tail is None:
            return

        prev = self.tail
        current = self.tail.next

        while True:
            if current.data == value:#value found
                #only one value
                if current == self.tail and current == self.tail.next:
                    self.tail = None
                elif current == self.tail.next:#value is head
                    self.tail.next = current.next
                elif current == self.tail:#vaue is tail
                    prev.next = current.next
                    self.tail = prev
                else:#value is not tail nor head 
                    prev.next = current.next
                return

            prev = current
            current = current.next

            if current == self.tail.next:#again came back to head 
                return

    def traverse(self):
        if self.tail is None:
            print("List is empty")
            return

        current = self.tail.next

        while True:
            print(current.data, end=" ")
            current = current.next

            if current == self.tail.next:
                break

        print()


cll = CircularLinkedList()

cll.insert_head(10)
cll.insert_head(5)
cll.insert_tail(20)
cll.insert_tail(30)
cll.insert_after(20, 25)

cll.traverse()

cll.delete_by_value(5)
cll.delete_by_value(30)

cll.traverse()


# i = 0

# while i < 5:
#     if i == 3:
#         break
#     i += 1
# else:
#     print("else")

# print("done")

# x=dit from the head to start of the cycle
# y=dist fro start of the cycle to meet point
# c=length of cycle
# slow= will travel x+y steps
# fast wil trave 2(x+y)
# 2(x+y)-(x+y)=x+y=k*c

#   0     1    2     3    4   5
# 10 → 20 → 30 → 40 → 50 → 60
#            ↑               ↓
#            ← ← ← ← ← ← ← ←
# s=f=h
# i   s   f
# 0   10  10
# 1   20  30
# 2   30  50
# 3   40  30
# 4   50  50
# slow:0>1>2>3>4 
# f:0>2>4>6>8
# diff : 0>1>2>3>4
# f-slow;x=2;y=2
# slow=x+y=2+2=4
# fast=2(x+y)=2(2+2)=8
# fast-slow=8-4=4
# 2(x+y)-(x+y)=KC=1*4
# pos=2,x=head->cycle start=2
# y=cycle start -> meeting point
# y=2
# cycle=30->40->50->60=>c=4
# k=(fast-slow)/c=4/4=1
# slow=head(10)
# fast=meeting(50)
# x+y=kc
# x=kc-y=1*4-2=2
# Fast pointer creates a “cycle offset”
# That offset becomes full rotations (k·c)
# After reset, both pointers have equal remaining distance to cycle start
# So they meet exactly there
# distance(head → start) = distance(meeting → start around cycle)


#https://cp-algorithms.com/others/tortoise_and_hare.html