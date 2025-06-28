'''
# STACK

# Linear Data Structure
# Stack is a LIFO (Last In First Out) / FILO (First In Last Out) data structure.
# Whether we want to add elements or remove them, it can be done only from the top of the Stack.
# Operations of a Stack
# Insertion operation: PUSH
# Deletion operation: POP
# Top (or) Peek: returns the top element of the stack
# Overflow – when stack is completely FULL :
# PUSH (Insertion) Operation gets rejected in such scenarios.
# Underflow – when the stack s completely EMPTY :
# POP (Deletion) Operation gets rejected in such scenarios.
# Description:
#     Write a Python program to create a class representing a STACK data structure.

# Output:
# Stack Operations
# 1. Push (Insert Element)
# 2. Pop (Delete Element)
# 3. Traverse (View Elements)
# 4. Peek (Viewing the First Element)
# 5. Size (Number of Elements)
# 6. Quit




#implemenataion of STack Using List

class Stack:
    def __init__(self):
        self.items=[]  #List as Stack
    
    def push(self,ele):
        self.items.append(ele)
        print(f"{ele} added ")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:return "can't delete an element because the stack is empty"
        if not (len(self.items==0)):
            return self.items.pop()
        else:return "can't delete an element because the stack is empty"

    def is_empty(self):
        return len(self.items )==0

    def size(self):
        return len(self.items)

    def traverse(self):
        print("Index  Value")
        for index,value in enumerate(self.items):
            print(f"{index}  {value}")
        print()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:return"Empty Stack"


stack=Stack()
while True:
    # Menu
    print()
    print("Stack Operations")
    print("1. Push (Insert Element)")
    print("2. Pop (Delete Element)")
    print("3. Traverse (View Elements)")
    print("4. Peek (Viewing the First Element)")
    print("5. Size (Number of Elements)")
    print("6. Quit")
    op = int(input("Enter your Choice [1 to 6]: "))
    print()

    if op == 1:
        ele = eval(input("Enter the Element to Insert: "))
        stack.push(ele)

    elif op == 2:
        popped_item = stack.pop()
        print(F"Popped item: {popped_item}")
        print()

    elif op == 3:
        stack.traverse()
       
    elif op == 4:
        print("Top element:", stack.peek())

    elif op == 5:
        print("Stack size:", stack.size())

    elif op == 6:
        print("Stack Operation Ended")
        break
    else:
        print("Invalid Option, Try again")
'''


# Problem 2: Undo-Redo System
# Concepts to Use: Classes, Polymorphism, Stack
# Scenario:
# Design a text editor with undo-redo functionality:

# Use a stack to store the history of actions (UndoStack).
# Use another stack for RedoStack to store the actions reversed during an undo operation.
# Implement a TextEditor class with methods:
# write(text): Adds text to the editor and pushes it onto the undo stack.
# undo(): Pops the last action from the undo stack and pushes it to the redo stack.
# redo(): Pops an action from the redo stack and restores it to the editor.
# Ensure proper handling of edge cases when no more undo/redo actions are available.



class UndoRedo:
    def __init__(self):
        self.undo_stack=[]
        self.redo_stack=[]
    
    def write(self,action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"Action: '{action}' added.")

    def undo(self):
        if not self.undo_stack:
            print("No actions to undo.")
        else:
            action=self.undo_stack.pop()
            self.redo_stack.append(action)
            print(f"undo : {action}")

    def redo(self):
        if not self.redo_stack:
            print("No actions to redo")
        else:
            action=self.redo_stack.pop()
            self.undo_stack.append(action)
            print(f"Redo : {action}")

    def display(self):
        print(f"undo Stack: {self.undo_stack}")
        print(f"redo Stack: {self.redo_stack}")

if __name__=="__main__":
    text=UndoRedo()
    text.write("writing Dheeraj")
    text.write("adding '.'")
    text.write("deleting 'Dheeraj'")

    text.display()

    text.undo()
    text.display()
    text.undo()
    
    text.redo()
    text.display()

