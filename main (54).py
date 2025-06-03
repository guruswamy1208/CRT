# Enter your code here
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
tree=Node()
tree.data = 1 #root Node
tree.left = Node() #creating new node for left
tree.left.data = 2 # inserting data in left child
# creating new node for right child
tree.right = Node()
# inseting data in right child
tree.right.data = 3
print(tree.data) # root Node
print(tree.left.data) # left child
# right child
print(tree.right.data)# right child)