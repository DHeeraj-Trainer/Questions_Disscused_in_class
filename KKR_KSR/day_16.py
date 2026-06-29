# Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

# Instead of solving the entire problem at once:

# Break the problem into smaller subproblems.
# Solve the smaller subproblem.
# Use that result to solve the larger problem.
def A():
    A()
---------------
def A():
    B()

def B():
    A()
def fun():
	i=0
	print(i)
	i+=1
	return fun()
def fun(i=0):
# 	print(i)
	if i==10:
	    return
	print(i)
	return fun(i+1)
fun()
# ------------------
# fun(5)
# fun(4)
# fun(3)
# fun(2)
# fun(1)
# fun(0)

lst=[1,5,9,8,7,6,3,5,8]
def sum_E_O(lst):
	e_sum=0
	o_sum=0
	for i in lst:
		if i%2==0:e_sum+=i
		else:o_sum+=i
	return e_sum,o_sum
print(sum_E_O(lst))

lst=[1,5,9,8,7,6,3,5,8]
def sum_E_O(lst,index=0,o_sum=0,e_sum=0):
	if index==len(lst):
		return o_sum,e_sum

	if lst[index]%2==0:
		e_sum+=lst[index]
	else:o_sum+=lst[index]
	return sum_E_O(lst,index+1,o_sum,e_sum)

def sumNto1(n=10):
    if n==1:return 1
    return n+sumNto1(n-1)
# 10+9+8+7+6+5+4+3+2+1
# 10+9+8+7+6+5+4+3+2+sumNto1(1)
# 10+9+8+7+6+5+4+3+sumNto1(2)
# 10+9+8+7+6+5+4+sumNto1(3)
# 10+9+8+7+6+5+sumNto1(4)
# 10+9+8+7+6+sumNto1(5)
# 10+9+8+7+sumNto1(6)
# 10+9+8+sumNto1(7)
# 10+9+sumNto1(8)
# 10+sumNto1(9)
# sumNto1(10)

def sumNto1(n=10):
    if n<=0:return 0
    return n+sumNto1(n-1)

# sumNto1(10)
# 10+sum(9)10+45
#   9+sum(8)9+36
#   8+sum(7)8+28
#     7+sum(6)=7+21
#      6+sum(5)=6+15
#       5+sum(4)=5+10
#          4+sum(3)=6+4
#           3+sum(2)=3+3
#              2+sum(1)=2+1
#                  1+0

def fact(n):
	if n==1 or n==0:
		return 1
	return n*fact(n-1)
# t(n)=t(n-1)+O(1)=o(n)
#     =n+n-1+1=2n=n
# t(n)=t(n-1)+t(n-2)+1
# =t(n-1)+t(n-2)


# T(n)=3T(n−1)+2T(n−2)
# t(n)=r^(n)
# r^n=3r^n-1+2r^n-2
# r^2=3r+1
# r2-3r-2=0
# r=3.56
# t(n)=teta(3.56)^n
	
# def power(a,n):#without using ** and math module
# # a=5
# # n=3
def power(a,n):
	product=1
	for i in range(1,n+1):
		#product=a*product
		product*=a
	return prodcut
# product=5*1
# 	5*5
# 	5*25
def power_rec(a,n):
	if n==0:return 1
	#if n==1:return a
	return a*power_rec(a,n-1)
# # power_rec(5,3):125
# # 5*power_rec(5,2):25*5=125
# # 	5*power_rec(5,1):5*5
# # 		5*power_rec(5,0):5*1
# # 			1




def power(a,n):
    if n == 0:
        return 1
    half = power(a,n//2)
    if n % 2 == 0:
        return half * half
    return a * half * half
# t(n)=t(n/2)+1
# 	t(n/4)+2
# 		t(n/8)+3
# k
# 1=n/(2^k)+k=n/2^k
# n=2^k
# logn=log(2^k)=k(1)=k
# k=logn

# Master TheoremGeneral Form

# T(n)=aT(n/b)+f(n)
# Where:
# a = number of subproblems
# b = size reduction
# f(n)= extra work
# t(5)
# 	t4
# 		t3
# 		t2
# 	t3
# 		t2
# 		t1
# t(n)=1(t(n-2)/2)+1(t(n-1)/1)+1
# =t(n-1)+t(n-2)


# assume t(n)=r^n
# r^n=r^(n-1)+r^(n-2)
# r^n/r^(n-2)=r^(n-2)/r^(n-2)+r^(n-1)/r^(n-2)
# a^m/a^n=a^(m-n)
# r^n/r^(n-2)=r^(n-(n-2))=r^2
# r^(n-1)/r^(n-2)=r^(n-1)-(n-2)=r^1=r
# r^2=r+1
# r^2-r-1=0

# r=1-5^(1/2)/2=-0.618
# r=1+5^(1/2)/2=1.618

# root=1+5(1/5)/2
# t(n)=teta(root^n)=(1.618)^n=2^n


























#---------------------------------------------Trees________________________________


'''
Trees In Python :
	a
    b       c
d      e   f  g
no of nodes=2^h-1

bst  l<r<right

		5
	3		6
     2                    7


b tree
	[30]
  [20,10]   [40,50]



avl tree:  balancing factor=h(l)-h(r)
-1,0,1

max heap:
p>=c
		90
	70		60
    50     40
min heap:p<=c
		40
	  50       60
    70           80




trie: string storage  (car,cat,cap)
		root
		  c
                  |
                   a
              /     |  \
              r     t   p


'''

class Treenode:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.val=val
class BinaryTree:
	def __init__(self):
		self.root=None
# create 5 nodes ...(n1,n2,n3..)
n1=Treenode("n1")
n2=Treenode("n2")
n3=Treenode("n3")
n4=Treenode("n4")
n5=Treenode("n5")
bt=BinaryTree()
bt.root=n1
n1.left=n2
n1.right=n3
n3.left=n4
n2.left=n5


# 	and n1 as root node
# 		n2 and n3 as subnodes and n4 is child of n3 and n5 is child of n2 
#                     n1
#                n2       n3
#            n5          n4
# [n1]  n1
# [n3,n2] n2 n3
# n5  n5
# n4  n5
# pre :n1 n2 n5 n3 n4 
# write code for preorder using while loop
# preorder : root->left->right
if bt.root is None:
	print("Root->None")
stack=[bt.root]
while stack:
	current_node=stack.pop()
	print(current_node.val,end="->")
	if current_node.right:
		stack.append(current_node.right)
	if current_node.left:
		stack.append(current_node.left)












class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
lst=[a,b,c,d,f,g,h]
for i in lst:
    i=Node(lst.index(i)+1)
# a=1,b=2,c=3,d=4,f=5,g=6,h=7
root=a
root.left=b
rot.right=c
root.left.left=d
root.left.right=f
root.right.left=g
root.right.right=h


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result

'''
1 2 4 2 5 1 3 6 3 7
1 2 4 5 3 6 7
s=[1]
s.pop()#1
spush(1.right) #3
s.push(1.left)#3 2
s.pop()#2
s.push(2.r)#3 5
s.push(2.l)#3 5 4
n=4
s.pop()#4
if n.r:
if n.l :
s.pop()#5
n=5
5.r 5.l
s.pop()#3
3.r
s.push(3.r)#7
s.push(3.l)#7 6
s.pop()6
6.r 6.l
s.pop()7
7.l 7.r
1 2 4  5 3 6 7
'''

def preoder(root):
	if root is None:
		return None
	print(root.data,end=" ")
	preorder(root.left)
	preorder(root.right)
def inorder(root):
	if root is None:return  None
	inorder(root.left)
	print(root.data,end=" ")
	inorder(root.right)
def postorder(root):
	if root is None:return  None
	postorder(root.left)
	postorder(root.right)
	print(root.data,end=" ")
'''
root=1
1
preorder(1.left=2)
	 1 2 preorder(2.l)
			1 2 4
				preorder(4.l)
				preorder(4.r)
            
             preorder(2.r)
			1 2 4 5
				preorder(5.l)preorder(5.r)
1 2 4 5
preorder(1.r)1 2 4 5 3 6 7
	preorder(3.l)
		preorder(6.l)preorder(6.r)
        preorder(3.r)
		preorder(7.l)preorder(7.r)



1 2 4 None None 5 None None 3 6 None None 7 None None
'''
