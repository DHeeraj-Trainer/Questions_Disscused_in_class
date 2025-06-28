class TreeNode:
    def __init__(self, node,):
        self.node = node
        self.left=None
        self.right=None

# root=TreeNode("A")
# root.left=TreeNode("B")
# root.right=TreeNode("C")
# root.left.right=TreeNode("D")
# root.right.left=TreeNode("E")
from collections import deque
class BinaryTree:
    def __init__(self,):
        self.root=None
    
    def insert(self, node):
        new_node=TreeNode(node)
        #if tree is empty create root node
        if not self.root:
            self.root=new_node
            return
        # level order trasversal to find the empty spot
        queue=deque([self.root])
        while queue:
            temp =queue.popleft()
            if not temp.left:
                temp.left=new_node
                return 
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right=new_node
                return
            else:
                queue.append(temp.right)

            
    def inorder(self,node,res):
        if node:
            self.inorder(node.left,res)
            res.append(node.node)
            self.inorder(node.right,res)
    def preorder(self,node,res):
        if node:
            res.append(node.node)
            self.preorder(node.left,res)
            self.preorder(node.right,res)
    def dfs(self):
        res=[]
        self.preorder(self.root,res)
        return res

    def postorder(self, node,res):
        if node:
            self.postorder(node.left,res)
            self.postorder(node.right,res)
            res.append(node.node)
        
    def P_tree(self,node,level=0):
        if node is not None:
            self.P_tree(node.right,level+1)
            print("    "*level+f'->{node.node}')
            self.P_tree(node.left,level+1)

    def delete(self,key):
        if not self.root:
            return 
        q=deque([self.root]) #level order trasversl
        target=None #key==target
        last=None #last bisited in the level order
        parent_in_last=None #last value parent
        #loop to find the traget ,last and parent of last
        while q:
            node=q.popleft()
            if node.node==key:
                target=node
            if node.left:
                parent_in_last=node
                q.append(node.left)
            if node.right:
                parent_in_last=node
                q.append(node.right)
            last=node
        if target:
            target.node=last.node
            if parent_in_last:
                if parent_in_last.right==last:
                    parent_in_last.right=None
                else:
                    parent_in_last.left=None    
                

values=[1,2,3,4,5,6,7,8,9,10,11,12,13]
tree=BinaryTree()
for val in values:
    tree.insert(val)
tree.P_tree(tree.root)
tree.delete(5)
print("______________________-")
tree.P_tree(tree.root)

# in_order=[]
# tree.inorder(tree.root,in_order)
# print(f"InOrder:{in_order}")
# pre_order=[]
# tree.preorder(tree.root,pre_order)
# print(f"PreOrder:{pre_order}")
# post_order=[]
# tree.postorder(tree.root,post_order)
# print(f"PostOrder:{post_order}")


