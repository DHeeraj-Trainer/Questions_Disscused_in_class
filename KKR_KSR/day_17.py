'''
| Tree Type            | Rule                   | Example Use         |
| -------------------- | ---------------------- | ------------------- |
| General Tree         | Unlimited children     | File systems        |
| Binary Tree          | Max 2 children         | Expressions         |
| Full Binary Tree     | 0 or 2 children        | Structured trees    |
| Complete Binary Tree | Last level left-filled | Heaps               |
| Perfect Binary Tree  | All nodes full         | Mathematical models |
| BST                  | Left < Root < Right    | Searching           |
| AVL Tree             | Balanced BST           | Databases           |
| B-Tree               | Multi-child nodes      | File systems        |
| Heap                 | Parent priority rule   | Priority queues     |
| Trie                 | Character storage      | Autocomplete        |

'''

# nodes=[R,A,C,NONE,NONE,D,NONE,NONE,B,E,NONE,NONE,F,G,NONE,NONE]
# def build(values,index=0):
# 	if values[index] is none:
# 		return None,index+1
# 	node=Node(values[index])
# 	node.left,index=build(values,index+1)
# 	node.right,index=build(values,index)
# 	return node,index
# create the treenode and tree class with root none note down the build tree and implement the preorder traversal
# ============================================================
# 1. BUILD TREE - RECURSION TRACE
# ============================================================
#
# Input:
#
# nodes = [
#     "R","A","C",None,None,"D",None,None,
#     "B","E",None,None,"F","G",None,None,None
# ]
#
# ------------------------------------------------------------
# Step | Call      | Value | Action         | Returned Index
# ------------------------------------------------------------
# 1    | build(0)  | R     | Create R       | 17
# 2    | build(1)  | A     | Create A       | 8
# 3    | build(2)  | C     | Create C       | 5
# 4    | build(3)  | None  | C.left=None    | 4
# 5    | build(4)  | None  | C.right=None   | 5
# 6    | build(5)  | D     | Create D       | 8
# 7    | build(6)  | None  | D.left=None    | 7
# 8    | build(7)  | None  | D.right=None   | 8
# 9    | build(8)  | B     | Create B       | 17
# 10   | build(9)  | E     | Create E       | 12
# 11   | build(10) | None  | E.left=None    | 11
# 12   | build(11) | None  | E.right=None   | 12
# 13   | build(12) | F     | Create F       | 17
# 14   | build(13) | G     | Create G       | 16
# 15   | build(14) | None  | G.left=None    | 15
# 16   | build(15) | None  | G.right=None   | 16
# 17   | build(16) | None  | F.right=None   | 17
#
# ============================================================
# TREE AFTER BUILD
# ============================================================
#
#               R
#            /     \
#           A       B
#         /   \   /   \
#        C     D E     F
#                   /
#                  G
#
# ============================================================
# WHY?
# ============================================================
#
# node.left, index = self.build(values, index + 1)
#
# Left subtree starts immediately after the current node.
#
# node.right, index = self.build(values, index)
#
# Right subtree starts from the index returned after the
# entire left subtree has been processed.
#
# Using index + 1 for the right subtree would skip nodes.
#
# ============================================================
# INSERT("H") - LEVEL ORDER (BFS) TRACE
# ============================================================
#
# Initial Queue:
#
# [R]
#
# ------------------------------------------------------------
# Iteration 1
# ------------------------------------------------------------
#
# Pop R
#
# R has both children.
#
# Queue = [A, B]
#
# ------------------------------------------------------------
# Iteration 2
# ------------------------------------------------------------
#
# Pop A
#
# A has both children.
#
# Queue = [B, C, D]
#
# ------------------------------------------------------------
# Iteration 3
# ------------------------------------------------------------
#
# Pop B
#
# B has both children.
#
# Queue = [C, D, E, F]
#
# ------------------------------------------------------------
# Iteration 4
# ------------------------------------------------------------
#
# Pop C
#
# Check:
#
# C.left = None
#
# Empty position found.
#
# Insert:
#
# C.left = H
#
# Stop.
#
# ============================================================
# QUEUE MOVEMENT TABLE
# ============================================================
#
# Iteration | Removed | Queue After Expansion | Action
# ------------------------------------------------------------
# 1         | R       | [A, B]               | Continue
# 2         | A       | [B, C, D]            | Continue
# 3         | B       | [C, D, E, F]         | Continue
# 4         | C       | ---                  | Insert H
#
# ============================================================
# TREE AFTER INSERTING H
# ============================================================
#
#               R
#            /     \
#           A       B
#         /   \   /   \
#        C     D E     F
#       /           /
#      H           G
#
# ============================================================
# TRAVERSALS
# ============================================================
#
# Preorder  (Root -> Left -> Right)
#
# R A C D B E F G
#
# After inserting H:
#
# R A C H D B E F G
#
# Inorder (Left -> Root -> Right)
#
# C A D R E B G F
#
# Postorder (Left -> Right -> Root)
#
# C D A E G F B R
#
# ============================================================
# TIME COMPLEXITIES
# ============================================================
#
# Build Tree             : O(n)
# Preorder Traversal     : O(n)
# Inorder Traversal      : O(n)
# Postorder Traversal    : O(n)
# Insert (Level Order)   : O(n) worst case
# Space (Recursion)      : O(h)
#
# h = height of tree
#
# ============================================================

from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def build(self, values, index=0):
        if index >= len(values) or values[index] is None:
            return None, index + 1

        node = TreeNode(values[index])

        node.left, index = self.build(values, index + 1)
        node.right, index = self.build(values, index)

        return node, index

    def insert(self, value):
        new = TreeNode(value)

        if self.root is None:
            self.root = new
            return

        queue = deque([self.root])

        while queue:
            curr = queue.popleft()

            if curr.left is None:
                curr.left = new
                return
            queue.append(curr.left)

            if curr.right is None:
                curr.right = new
                return
            queue.append(curr.right)

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

nodes = [
    "R", "A", "C", None, None, "D", None, None,
    "B", "E", None, None, "F", "G", None, None, None
]

tree = BinaryTree()
tree.root, _ = tree.build(nodes)

print("Preorder:")
tree.preorder(tree.root)

print("\n\nInorder:")
tree.inorder(tree.root)

print("\n\nPostorder:")
tree.postorder(tree.root)

tree.insert("H")

print("\n\nAfter Inserting H (Preorder):")
tree.preorder(tree.root)




from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def build(self, values, index=0):
        if index >= len(values) or values[index] is None:
            return None, index + 1

        node = TreeNode(values[index])

        node.left, index = self.build(values, index + 1)
        node.right, index = self.build(values, index)

        return node, index

    def insert(self, value):
        new = TreeNode(value)

        if self.root is None:
            self.root = new
            return

        queue = deque([self.root])

        while queue:
            curr = queue.popleft()

            if curr.left is None:
                curr.left = new
                return
            queue.append(curr.left)

            if curr.right is None:
                curr.right = new
                return
            queue.append(curr.right)

    def search(self, value):
        if self.root is None:
            return False

        queue = deque([self.root])

        while queue:
            curr = queue.popleft()

            if curr.data == value:
                return True

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return False

    def delete_deepest(self, target):
        queue = deque([self.root])

        while queue:
            curr = queue.popleft()

            if curr.left:
                if curr.left == target:
                    curr.left = None
                    return
                queue.append(curr.left)

            if curr.right:
                if curr.right == target:
                    curr.right = None
                    return
                queue.append(curr.right)

    def delete(self, value):
        if self.root is None:
            return

        if self.root.left is None and self.root.right is None:
            if self.root.data == value:
                self.root = None
            return

        queue = deque([self.root])

        target = None
        deepest = None

        while queue:
            deepest = queue.popleft()

            if deepest.data == value:
                target = deepest

            if deepest.left:
                queue.append(deepest.left)

            if deepest.right:
                queue.append(deepest.right)

        if target:
            target.data = deepest.data
            self.delete_deepest(deepest)

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

nodes = [
    "R", "A", "C", None, None, "D", None, None,
    "B", "E", None, None, "F", "G", None, None, None
]

tree = BinaryTree()
tree.root, _ = tree.build(nodes)

print("Preorder:")
tree.preorder(tree.root)

print("\n\nSearch G:")
print(tree.search("G"))

print("\nSearch X:")
print(tree.search("X"))

tree.insert("H")

print("\nAfter Insert H:")
tree.preorder(tree.root)

tree.delete("E")

print("\n\nAfter Delete E:")
tree.preorder(tree.root)





class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )



from collections import deque

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return depth








#----------------------------


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )








from collections import deque

class Solution:
    def isSameTree(self, p, q):
        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True


#-----------------------------
