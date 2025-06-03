# Enter your code here inorder and preorder , postorder
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,Node):
        if Node:
            self.inorder_traversal(Node.left)
            print(Node.data)
            self.inorder_traversal(Node.right)
    def preorder_traversal(self,Node):
        if Node:
            print(Node.data, end=" ")
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
    def postorder_traversal(self,Node):
        if Node:
            self.preorder_traversal(Node.left)
            self.preorder_traversal(Node.right)
            print(Node.data, end=" ")
tree=Node()
tree.data = 1
tree.left = Node() 
tree.left.data = 2 
tree.right = Node()
tree.right.data = 3
print(tree.data) 
print(tree.left.data)
print(tree.right.data) 
tree.inorder_traversal(Node=tree)
tree.preorder_traversal(Node=tree)
tree.postorder_traversal(Node=tree)




