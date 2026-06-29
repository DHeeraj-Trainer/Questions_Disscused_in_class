from collections import deque

class SimpleQueue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, value):
        # Insert at rear — O(1)
        self.q.append(value)
        print(f"Enqueued: {value} | Queue: {list(self.q)}")

    def dequeue(self):
        # Remove from front — O(1)
        if self.isEmpty(): return "Queue Underflow!"
        val = self.q.popleft()
        print(f"Dequeued: {val} | Queue: {list(self.q)}")
        return val

    def front(self):
        return self.q[0] if not self.isEmpty() else "Empty"

    def rear(self):
        return self.q[-1] if not self.isEmpty() else "Empty"

    def isEmpty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

# q = SimpleQueue()
# q.enqueue("A"); q.enqueue("B"); q.enqueue("C")
# print("Front:", q.front())    # A
# print("Rear :", q.rear())     # C
# q.dequeue()
# print("Size :", q.size())     # 2

















# import heapq
# pq=[]
# heapq.heappush(pq,(30,"TaskA"))
# heapq.heappush(pq,(15,"TaskC"))
# heapq.heappush(pq,(20,"TaskB"))
# heapq.heappush(pq,(1,"Task B"))
# heapq.heappush(pq,(10,"TaskB1"))
# heapq.heappush(pq,(1,"Task A"))
# while pq:
#     p,t=(heapq.heappop(pq))
#     print(p,t)

# from collections import deque

# dq=deque()
# # print(type(dq))
# dq.append(20)
# dq.append(10)
# dq.appendleft(5)
# print(dq) #[5,20,10]
# dq.pop()
# print(dq)#[5,20]
# dq.popleft()
# print(dq)#[20]























class CircularQueue:
    def __init__(self, size):
        self.size  = size
        self.queue = [None] * size
        self.front = -1
        self.rear  = -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def isEmpty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.isFull():
            return "Queue Overflow!"
        if self.isEmpty(): self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued {value} at index {self.rear}")

    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow!"
        val = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1   # last element removed
        else:
            self.front = (self.front + 1) % self.size
        return val

    def display(self):
        if self.isEmpty(): print("Empty"); return
        i, elems = self.front, []
        while True:
            elems.append(self.queue[i])
            if i == self.rear: break
            i = (i + 1) % self.size
        print("CQ:", elems)

# ── Driver Code ───────────────────────────────────
cq = CircularQueue(5)
cq.enqueue(1); cq.enqueue(2); cq.enqueue(3)
cq.dequeue()        # frees slot 0
cq.enqueue(4)     # wraps around to slot 0
cq.display()         # CQ: [2, 3, 4]