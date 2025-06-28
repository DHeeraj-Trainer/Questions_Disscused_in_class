# IN DLL 
# Attribute:Data,next,prev
class Dlnode:
    def __init__(self, node,):
        self.node = node
        self.next = None
        self.prev = None


class DoubleLInkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, node):
        new_node = Dlnode(node)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, node):
        new_node = Dlnode(node)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def insert_after_value(self, target, node):
        curr = self.head
        while curr and curr.node != target:
            curr = curr.next
        if not curr:
            print("Value not found")
            return
        new_node = Dlnode(node)
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
    def forward_trasversal(self,):
        print("Forward: ",end="")
        curr=self.head
        while curr:
            print(curr.node,end="<->")
            curr = curr.next
        print("None")
    def traverse_backward(self):
        print("Backward: ", end="")
        curr = self.head
        if not curr:
            print("List is empty")
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.node, end=" <-> ")
            curr = curr.prev
        print("None")


    def delete_by_value(self, value):
        curr = self.head
        while curr and curr.node != value:
            curr = curr.next
        if not curr:
            print("Value not found")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head=curr.next
        if curr.next:
            curr.next.prev=curr.prev




DLL=DoubleLInkedList()
list_=[1,2,3,4,5,6,7]
for val in list_:
    # DLL.insert_at_beginning(val)
    DLL.insert_at_end(val)
DLL.insert_after_value(5,8)
DLL.forward_trasversal()
DLL.traverse_backward()
DLL.delete_by_value(8)
DLL.forward_trasversal()
        