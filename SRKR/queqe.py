'''
Queue follows the FIFO (First In, First Out) principle.

Queue is a Linear form of data structure where elements are arranged in FIFO manner. [First In First Out]
We also call this as LILO (Last In Last Out)
It means that the elements that gets inserted first are the ones to be deleted first also.
Enqueue: adding of the elements into the queue
Dequeue: deleting elements from the queue
Front: points to the 1st element within the queue
Rear: points to the last element within the queue




Here are the four types of queues and their applications in various domains:

---

 1. Simple Queue (FIFO Queue)  
Definition: A queue where elements are inserted at the 
            rear and removed from the front, following the 
            First-In-First-Out (FIFO) principle.

 Applications:
Task Scheduling
Order Management
Print Spooling
Call Center Systems
Breadth-First Search (BFS)

---

 2. Circular Queue  
Definition: A queue where the last position is connected back 
            to the first position to make it circular, 
            avoiding wastage of memory.

 Applications:
CPU Scheduling (Round-Robin)
Memory Management (Buffer Pools)
Traffic Light Systems
Audio/Video Streaming
---

 3. Priority Queue  
Definition: A queue where each element is assigned a priority, 
        and elements with higher priority are dequeued before those 
            with lower priority.

 Applications:
Task Scheduling (Priority-Based)
Shortest Path Algorithms (e.g., Dijkstra’s)
Job Scheduling
Event Simulation
Data Compression (Huffman Coding)

---

 4. Double Ended Queue (Deque)  
Definition: A queue where elements can be added or removed 
            from both the front and rear ends.

 Applications:
Undo Operations
Palindrome Checking
Sliding Window Problems
Job Scheduling (Flexible Prioritization)
Caching (LRU Cache)

---








Problem 1: Ticket Booking System
Concepts to Use: Classes, Inheritance, Queue
Scenario:
Design a ticket booking system for a movie theater where:
Customers are queued up to book tickets, and the queue follows 
the FIFO (First In, First Out) principle.
Implement a CustomerQueue class using a queue to manage customer 
requests.
Each customer should have details like name, age, and 
number_of_tickets.
A TicketBooking class should handle adding customers to the 
queue, booking tickets for the first customer in the queue, 
and displaying the queue.
After booking, the customer is removed from the queue.
'''
from collections import deque 

class Customer:
    def __init__(self,name,age,no_of_tickets):
        self.name=name
        self.age=age
        self.no_of_tickets=no_of_tickets

    def __str__(self):
        return f"Name:{self.name}, Age={self.age} ,no_of_tickets={self.no_of_tickets}"

class TicketBooking:
    def __init__(self):
        self.customer_queue=deque()
    
    def add_customers(self,customer):
        self.customer_queue.append(customer)
        print(f"Customer {customer} added")

    def book_ticket(self):
        if self.customer_queue:
            customer=self.customer_queue.popleft()
            print(f"Booking {customer.no_of_tickets} tickets for {customer.name}")
        else:print("No Customers in QUeue")

    def display_queue(self):
        if not self.customer_queue:
            print("The queue is empty")
        else:
            print("Customer in the Queue :")
            for customer in  self.customer_queue:
                print(customer)


if __name__=='__main__':
    booking=TicketBooking()

    c1=Customer("Dheeraj",28,5)
    c2=Customer("Rajesh",25,6)

    booking.add_customers(c1)
    booking.add_customers(c2)

    booking.display_queue()

    booking.book_ticket()
    booking.display_queue()
    booking.book_ticket()
    booking.display_queue()
'''



Description:
Write a Python program to create a class representing a QUEUE data structure.

It includes methods to add an item to the queue, remove an item from the queue, check if the queue is empty, and display the contents of the queue.

Output:
Queue Operations
1. Enqueue (Insert Element)
2. Dequeue (Delete Element)
3. Traverse (View Elements)
4. Size (Number of Elements)
5. Quit


'''
