"""

# GRAPHS IN PYTHON

A Graph is a non-linear data structure consisting of:

1. Vertices (Nodes)
2. Edges (Connections)

Mathematically:

```
G = (V, E)
```

Where:
V = Set of Vertices
E = Set of Edges

---

## REAL-WORLD EXAMPLES

Facebook:
Users -> Vertices
Friendships -> Edges

Google Maps:
Cities -> Vertices
Roads -> Edges

Computer Networks:
Devices -> Vertices
Connections -> Edges

Flight Systems:
Airports -> Vertices
Flights -> Edges

Web Pages:
Pages -> Vertices
Hyperlinks -> Edges

---

## EXAMPLE GRAPH

```
    A
   / \
  B---C
   \
    D
```

Vertices:
A, B, C, D

Edges:
(A,B)
(A,C)
(B,C)
(B,D)

---

## GRAPH VS TREE

## Feature             Tree               Graph

Root Node           Required           Not Required
Cycles              Not Allowed        Allowed
Connectivity        Always Connected   May be Disconnected
Edges               n - 1              Any Number
Parent-Child        Exists             Not Required

---

## GRAPH REPRESENTATIONS

1. Adjacency Matrix

   ```
    A B C D
   ```

   A [ 0 1 1 0 ]
   B [ 1 0 0 1 ]
   C [ 1 0 0 1 ]
   D [ 0 1 1 0 ]

Space Complexity:
O(V²)

---

2. Adjacency List

graph = {
"A": ["B", "C"],
"B": ["A", "D"],
"C": ["A", "D"],
"D": ["B", "C"]
}

Space Complexity:
O(V + E)

---

3. Edge List

edges = [
("A","B"),
("B","A"),
("A","C"),
("C","B")
]

Space Complexity:
O(E)

---

## COMPARISON OF REPRESENTATIONS

## Feature         Matrix      List        Edge List

Space           O(V²)       O(V+E)      O(E)
Add Edge        O(1)        O(1)        O(1)
Find Edge       O(1)        O(V)        O(E)
Traversal       O(V²)       O(V+E)      O(E)

===========================================================
GRAPH ADT IMPLEMENTATION
========================

"""

class Graph:

```
def __init__(self, graph=None):
    self.graph = graph if graph else {}

def add_vertex(self, vertex):

    if vertex not in self.graph:
        self.graph[vertex] = []

def add_edge(self, vertex, edge):

    if vertex not in self.graph:
        self.add_vertex(vertex)

    if edge not in self.graph:
        self.add_vertex(edge)

    self.graph[vertex].append(edge)
    self.graph[edge].append(vertex)

def remove_edge(self, vertex, edge):

    if vertex in self.graph[edge]:
        self.graph[edge].remove(vertex)

    if edge in self.graph[vertex]:
        self.graph[vertex].remove(edge)

def remove_vertex(self, vertex):

    for neighbor in self.graph[vertex]:
        self.graph[neighbor].remove(vertex)

    del self.graph[vertex]

def display(self):

    for vertex in self.graph:
        print(vertex, "->", self.graph[vertex])
```

"""

# TRAVERSAL GRAPH

"""

graph = {
"A": ["B", "C"],
"B": ["D", "E", "A"],
"C": ["F", "A"],
"D": ["B"],
"E": ["B"],
"F": ["C"]
}

"""
Graph Structure

```
    A
  /   \
 B     C
/ \     \
```

D   E     F

===========================================================
BREADTH FIRST SEARCH (BFS)
==========================

Uses Queue (FIFO)

Time Complexity:
O(V + E)

Space Complexity:
O(V)
"""

from collections import deque

def bfs(start):

    visited = {start}
    q = deque([start])

    while q:

        node = q.popleft()
        print(node, end=" -> ")

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

"""
BFS ITERATION TABLE

Start:

Queue = [A]
Visited = {A}

---

## Step    Node    Queue After Processing

1       A       [B, C]
2       B       [C, D, E]
3       C       [D, E, F]
4       D       [E, F]
5       E       [F]
6       F       []
------------------

BFS Output:

A -> B -> C -> D -> E -> F

===========================================================
DEPTH FIRST SEARCH (RECURSIVE)
==============================

Uses Call Stack

Time Complexity:
O(V + E)

Space Complexity:
O(V)
"""

def dfs_recursive(node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)

    print(node, end=" -> ")

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs_recursive(neighbor, visited)

"""
DFS RECURSIVE CALL STACK

dfs(A)

Call Stack

dfs(A)
|
+-- dfs(B)
|   |
|   +-- dfs(D)
|   |
|   +-- dfs(E)
|
+-- dfs(C)
|
+-- dfs(F)

---

## Execution Order

Visit A

Visit B

Visit D
Return to B

Visit E
Return to B

Return to A

Visit C

Visit F

Return to C

Return to A

---

DFS Output

A -> B -> D -> E -> C -> F

===========================================================
DEPTH FIRST SEARCH (USING STACK)
================================

Uses Explicit Stack (LIFO)

Time Complexity:
O(V + E)

Space Complexity:
O(V)
"""

def dfs_stack(start):

    visited = set()

    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            print(node, end=" -> ")

            visited.add(node)

            for neighbor in reversed(graph[node]):

                if neighbor not in visited:
                    stack.append(neighbor)

"""
DFS STACK ITERATION TABLE

Start

Stack = [A]

---

## Step    Node    Stack After Processing

1       A       [C, B]
2       B       [C, A, E, D]
3       D       [C, A, E]
4       E       [C, A]
5       C       [A, F]
6       F       [A]
-------------------

DFS Output

A -> B -> D -> E -> C -> F

===========================================================
PROGRAM EXECUTION
=================

"""

print("\nBFS Traversal")
bfs("A")

print("\n\nDFS Recursive Traversal")
dfs_recursive("A")

print("\n\nDFS Stack Traversal")
dfs_stack("A")

"""


## BFS

Uses Queue
Level-by-Level Traversal

Output:
A -> B -> C -> D -> E -> F

## DFS Recursive

Uses Function Call Stack

Output:
A -> B -> D -> E -> C -> F

## DFS Iterative

Uses Explicit Stack

Output:
A -> B -> D -> E -> C -> F

===========================================================
"""
"""
Shortest Path Problems

One of the most common problems in Graph Theory is:

Given a starting vertex, find the shortest distance to all other vertices.

This problem appears in:

Google Maps
GPS Navigation
Network Routing
Airline Route Planning
Social Network Recommendations
Game Development
Robotics Path Planning

Dijkstra's Algorithm is a Greedy Algorithm used to find:

The shortest path from a source vertex to all other vertices in a weighted graph.

Invented By

Edsger W. Dijkstra

In 1956.

3. Conditions for Using Dijkstra

✅ Weighted Graph

✅ Non-negative edge weights

❌ Negative weights are not allowed

For negative weights:

Use Bellman-Ford Algorithm

Core Idea Behind Dijkstra

Imagine standing in a city.

You always choose:

The nearest unvisited city first.

Then update distances to neighboring cities.

This process repeats until all cities are processed.

This is why Dijkstra is called a:

Greedy Algorithm


Dijkstra Algorithm Steps
1. Set source distance = 0

2. Set all other distances = ∞

3. Push source into Min Heap

4. While heap is not empty:

       Extract minimum distance vertex

       For each neighbor:

            new_distance =
            current_distance + edge_weight

            If smaller:

                 update distance

                 push into heap

5. Return distance array

Dijkstra Visualization
A
│\
│ \
4  2
│   \
B----C
 \   /
 10 3
   D

Shortest Paths from A:

A → A = 0

A → B = 4

A → C = 2

A → D = 5
Time Complexity

Using Min Heap:

O((V + E) log V)

Where:

V = Vertices
E = Edges

Without Heap:

O(V²)


"""


# graph = {
#     'A': [('B',4), ('C',2)],
#     'B': [('A',4), ('C',5), ('D',10)],
#     'C': [('A',2), ('B',5), ('D',3)],
#     'D': [('B',10), ('C',3)]
# }
#       A
#     /   \
#   4/     \2
#   /       \
#  B----3----C
#   \        /
#   \10   /5
#      \  /
#       D
# source =A
# build the distance table:
# A->0,B->4,C->2,D->5
# VISITED={ACD}
# PQ=[(A,0)]->[]
# WHILE PQ:
# 	CURRNODE,CURRDIST=PQ.HEAPPOP()
# 	VISTAED A
# 	IF DISTACT TABLE DISTACE<NEWCOST
# 	B=0+4=4
# 	C=0+2=2
# 	[(B,4),(C,2)]->>>[(C,2),(B,4)]>>>[(B,4)]
# 	CN.CD=C,2
# 	DBA
# 	DB
# 	D=2+3=5
# 	B=2+5=7
# 	[(B,4),(D,3),]>>>>[(D,5),(B,4)]
# 	CURR.N,CURR.=[D,5]

	
	
	
import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(start):
    pq = [(0, start)]          # (cost, node)
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    return dist

print(dijkstra('A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}



# Dijkstra Characteristics
# Property	Value
# Algorithm Type	Greedy
# Graph Type	Weighted
# Negative Weights	Not Allowed
# Data Structure	Min Heap (Priority Queue)
# Time Complexity	O((V+E)logV)
# Output	Shortest Distance