# CLL:
# Data
# next

class Cnode:
    def __init__(self, data):
        self.data = data
        self.next=None
    
class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def inser_at_end(self, data):
        new_node=Cnode(data)
        if not self.head:
            self.head=new_node
            new_node.next=self.head
            return 
        curr =self.head
        while curr.next!=self.head:
            curr=curr.next
        curr.next=new_node
        new_node.next=self.head 