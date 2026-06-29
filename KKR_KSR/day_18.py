from collections import deque

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
            return

        curr = self.root

        while True:

            if value < curr.data:

                if curr.left is None:
                    curr.left = TreeNode(value)
                    return

                curr = curr.left

            else:

                if curr.right is None:
                    curr.right = TreeNode(value)
                    return

                curr = curr.right

    def search(self, value):

        curr = self.root

        while curr:

            if curr.data == value:
                return True

            elif value < curr.data:
                curr = curr.left

            else:
                curr = curr.right

        return False

    def find_min(self, node):

        while node.left:
            node = node.left

        return node

    def find_max(self, node):

        while node.right:
            node = node.right

        return node

    def delete(self, node, value):

        if node is None:
            return None

        if value < node.data:

            node.left = self.delete(node.left, value)

        elif value > node.data:

            node.right = self.delete(node.right, value)

        else:

            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = self.find_min(node.right)

            node.data = successor.data

            node.right = self.delete(
                node.right,
                successor.data
            )

        return node

    def preorder(self, node):

        if node is None:
            return

        print(node.data, end=" ")

        self.preorder(node.left)

        self.preorder(node.right)

    def inorder(self, node):

        if node is None:
            return

        self.inorder(node.left)

        print(node.data, end=" ")

        self.inorder(node.right)

    def postorder(self, node):

        if node is None:
            return

        self.postorder(node.left)

        self.postorder(node.right)

        print(node.data, end=" ")

    def bfs(self):

        if self.root is None:
            return

        queue = deque([self.root])

        while queue:

            curr = queue.popleft()

            print(curr.data, end=" ")

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

'''
bst = BST()

values = [50,30,70,20,40,60,80]

for value in values:
    bst.insert(value)

print(bst.search(60))
print(bst.search(100))


bst = BST()

for value in [50,30,70,20,40,60,80]:
    bst.insert(value)

print("Inorder:")
bst.inorder(bst.root)

print("\nSearch 60:")
print(bst.search(60))

print("\nMinimum:")
print(bst.find_min(bst.root).data)

print("\nMaximum:")
print(bst.find_max(bst.root).data)

bst.root = bst.delete(bst.root, 50)

print("\nAfter Delete 50:")
bst.inorder(bst.root)

print("\nBFS:")
bst.bfs()

#BST Time Complexities

| Operation  | Average  | Worst |
| ---------- | -------- | ----- |
| Insert     | O(log n) | O(n)  |
| Search     | O(log n) | O(n)  |
| Delete     | O(log n) | O(n)  |
| Find Min   | O(log n) | O(n)  |
| Find Max   | O(log n) | O(n)  |
| Traversals | O(n)     | O(n)  |


'''
# ============================================================
# BST DELETION EXAMPLE
# ============================================================
#
# Original BST
#
#                  25
#                /    \
#              20      36
#             /  \    /  \
#           10   22  30   40
#          / \      /    /  \
#         5  12    28   38  48
#
# Goal:
# Delete Node = 10
#
# ============================================================
# STEP 1 : SEARCH FOR THE NODE
# ============================================================
#
# delete(25, 10)
#
# Iteration Table
#
# +-----------+--------------+------------+----------+
# | Iteration | Current Node | Comparison | Action   |
# +-----------+--------------+------------+----------+
# |     1     |      25      | 10 < 25    | Go Left  |
# |     2     |      20      | 10 < 20    | Go Left  |
# |     3     |      10      | 10 == 10   | Found    |
# +-----------+--------------+------------+----------+
#
# Node Found = 10
#
#
# ============================================================
# STEP 2 : IDENTIFY DELETION CASE
# ============================================================
#
# Node 10 has:
#
#       10
#      /  \
#     5   12
#
# Left Child  = 5
# Right Child = 12
#
# Therefore:
#
# CASE 3 -> NODE HAS TWO CHILDREN
#
#
# ============================================================
# STEP 3 : FIND INORDER SUCCESSOR
# ============================================================
#
# Rule:
#
# Inorder Successor =
# Smallest Node in Right Subtree
#
# Right Subtree of 10:
#
#       12
#
# find_min(12)
#
# +-----------+--------------+--------------+--------+
# | Iteration | Current Node | Left Exists? | Action |
# +-----------+--------------+--------------+--------+
# |     1     |      12      |      No      | Stop   |
# +-----------+--------------+--------------+--------+
#
# Successor = 12
#
#
# ============================================================
# STEP 4 : REPLACE NODE DATA
# ============================================================
#
# Execute:
#
# node.data = successor.data
#
#
# Before:
#
#       10
#      /  \
#     5   12
#
#
# After:
#
#       12
#      /  \
#     5   12
#
# Temporary duplicate exists.
#
#
# ============================================================
# STEP 5 : DELETE SUCCESSOR NODE
# ============================================================
#
# Execute:
#
# node.right = delete(node.right, 12)
#
#
# Current Subtree:
#
#       12
#
# Successor node is a LEAF NODE
#
# CASE 1 -> LEAF NODE DELETION
#
#
# Return:
#
# None
#
#
# ============================================================
# FUNCTION CALL STACK
# ============================================================
#
# delete(25,10)
# │
# ├── 10 < 25
# │
# └── delete(20,10)
#       │
#       ├── 10 < 20
#       │
#       └── delete(10,10)
#             │
#             ├── Node Found
#             │
#             ├── find_min(12)
#             │      │
#             │      └── return 12
#             │
#             ├── node.data = 12
#             │
#             └── delete(12,12)
#                    │
#                    ├── Leaf Node
#                    │
#                    └── return None
#
#
# ============================================================
# STACK GROWTH
# ============================================================
#
# TOP
# delete(25,10)
#
#
# TOP
# delete(20,10)
# delete(25,10)
#
#
# TOP
# delete(10,10)
# delete(20,10)
# delete(25,10)
#
#
# TOP
# delete(12,12)
# delete(10,10)
# delete(20,10)
# delete(25,10)
#
#
# ============================================================
# STACK UNWINDING
# ============================================================
#
# delete(12,12)
#       ↓
# delete(10,10)
#       ↓
# delete(20,10)
#       ↓
# delete(25,10)
#       ↓
# Finished
#
#
# ============================================================
# TREE BEFORE DELETION
# ============================================================
#
#                  25
#                /    \
#              20      36
#             /  \    /  \
#           10   22  30   40
#          / \      /    /  \
#         5  12    28   38  48
#
#
# ============================================================
# TREE AFTER REPLACING 10 WITH SUCCESSOR 12
# ============================================================
#
#                  25
#                /    \
#              20      36
#             /  \    /  \
#           12   22  30   40
#          / \      /    /  \
#         5  12    28   38  48
#
#
# ============================================================
# TREE AFTER REMOVING SUCCESSOR
# ============================================================
#
#                  25
#                /    \
#              20      36
#             /  \    /  \
#           12   22  30   40
#          /        /    /  \
#         5        28   38  48
#
#
# ============================================================
# INORDER TRAVERSAL
# ============================================================
#
# Before:
#
# 5 10 12 20 22 25 28 30 36 38 40 48
#
#
# After:
#
# 5 12 20 22 25 28 30 36 38 40 48
#
# ============================================================







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        ans=float('inf')
        def inorder(node):
		if not node:return
		inorder(node.left)
		if prev is not None:
			ans=min(ans,node.val-prev)
		prev=node.val
		inorder(node.right)
i=0	 prev=None ans=inf node=none
i=1	node=4
		node=1,prev=none->prev=1
		node=2,prev=1->prev=2
			ans=min(inf,2-1)
			ans=min(inf,1)=1
		node=3,prev=2->prev=3
			as=min(1,3-2)=1
		node=4;prev=3->prev=4
			ans=min(1,4-3)=1
		node=6;prev=4->6
			ans=min(1,6-4)=1
		



class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:return 0
        ans=0
        if low<=root.val<=high:
            ans+=root.val
        ans+=self.rangSumBST(root.left,low,high)
        ans+=self.rangSumBST(root.right,low,high)
        return ans




class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.ans



Level 1
--------
700  Search BST
701  Insert BST
530  Minimum Difference
938  Range Sum BST

Level 2
--------
98   Validate BST
230  Kth Smallest
653  Two Sum BST
173  BST Iterator

Level 3
--------
108  Sorted Array → BST
1008 BST from Preorder
235  LCA BST

Level 4
--------
450  Delete BST
538  Greater Tree
669  Trim BST

Level 5
--------
96   Unique BST
95   Unique BST II
99   Recover BST

Level 6
--------
333  Largest BST Subtree
1373 Maximum Sum BST
1569 Reorder Array Same BST













