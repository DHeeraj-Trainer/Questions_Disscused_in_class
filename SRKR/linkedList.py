#Manual Implemenation of Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next=None
    

# n1=Node(1)
# n2=Node(2)
# n3=Node(3)
# n4=Node(4)

# n1.next=n2
# n2.next=n3
# n3.next=n4

# current_node=n1 
# while current_node:
#     print(current_node.data,end="->")
#     current_node=current_node.next
# print("None")
"""
#Single Linked List 
class Node:
    def __init__(self, data,):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None
    
    def insert_end(self, data):
        new_node= Node(data)
        if not self.head:
            self.head= new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next= new_node
    
    def insert_after_value(self, target,data):
        new_node= Node(data)
        if not self.head:
            self.head= new_node
        else:
            current=self.head
            while current:
                if current.data==target:
                    new_node.next= current.next
                    current.next= new_node
                    return
                current=current.next
            print(f"value {target}not found in the list")
    def insert_head(self, data):
        new_node=Node(data)
        new_node.next= self.head
        self.head= new_node
    def get_nodes(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        return("None")
    
    def delete_at_start(self):
        if not self.head:
            print("List is Empty ")
        else:
            self.head=self.head.next

    def delete_at_end(self):
        if not self.head:
            print("List is Empty")
        if not self.head.next:
            self.head= None
        current=self.head
        while current.next.next:
            current=current.next
        current.next= None
    

    def delete_by_value(self, value):
        current=self.head
        prev=None
        while current:
            if current.data==value:
                if prev:
                    prev.next= current.next
                else:
                    self.head=current.next
            prev=current
            current=current.next



ll=LinkedList()
ll.insert_head(1)
print(ll.get_nodes())
ll.insert_head(10)
print(ll.get_nodes())
ll.insert_head(100)
print(ll.get_nodes())
ll.insert_end(1000)
print(ll.get_nodes())
ll.insert_after_value(10,55)
print(ll.get_nodes())
ll.delete_at_start()
print(ll.get_nodes())
ll.delete_at_end()
print(ll.get_nodes())


"""

# Node class
class Carriage:
    def __init__(self, number):
        self.number = number
        self.next = None

# Train (LinkedList) class
class Train:
    def __init__(self):
        self.head = None

    # Add carriage at the end
    def add_carriage_end(self, number):
        new_carriage = Carriage(number)
        if not self.head:
            self.head = new_carriage
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_carriage

    # Insert after a given carriage number
    def insert_after(self, target_number, new_number):
        current = self.head
        while current:
            if current.number == target_number:
                new_carriage = Carriage(new_number)
                new_carriage.next = current.next
                current.next = new_carriage
                return
            current = current.next
        print(f"Carriage {target_number} not found!")

    # Delete carriage by number
    def delete_carriage(self, number):
        current = self.head
        prev = None
        while current:
            if current.number == number:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print(f"Carriage {number} not found!")

    # Display train composition
    def display_train(self):
        if not self.head:
            print("Train is empty.")
            return
        current = self.head
        print("Train Composition: ", end="")
        while current:
            print(f"{current.number} -> ", end="")
            current = current.next
        print("None")

def main():
    train = Train()
    while True:
        print("\n====== Train Management System ======")
        print("1. Add carriage at the end")
        print("2. Insert carriage after a given carriage")
        print("3. Delete a carriage by number")
        print("4. Display train composition")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            number = int(input("Enter carriage number to add: "))
            train.add_carriage_end(number)
        elif choice == '2':
            target = int(input("Enter target carriage number: "))
            new_number = int(input("Enter new carriage number: "))
            train.insert_after(target, new_number)
        elif choice == '3':
            number = int(input("Enter carriage number to delete: "))
            train.delete_carriage(number)
        elif choice == '4':
            train.display_train()
        elif choice == '5':
            print("Exiting Train Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
