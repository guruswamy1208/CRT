# Enter your code here inorder and preorder , postorder
class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,Node):
        sum=0
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
    def sum_of_Nodes(self,Node):
        if Node is None:
            return 0
        return Node.data + self.sum_of_Nodes(Node.left) + self.sum_of_Nodes(Node.right)
            
    def count_Nodes(self,Node):
        if(Node is None):
            return 0
        return 1+ self.count_Nodes(Node.left) + self.count_Nodes(Node.right)
    def height(self,Node):
        if(Node is None):
            return 0
        return max(self.height(Node.left) + self.height(Node.right))
            
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
print("\nSum of all nodes in binary tree is:")
print(tree.sum_of_Nodes(Node=tree))
print("\nSum of all nodes in left subtree is:")
print(tree.sum_of_Nodes(Node=tree.left))
print("\nSum of all nodes in right subtree is:")
print(tree.sum_of_Nodes(Node=tree.right))
print("\n No of nodes in left sub tree")
print(tree.count_Nodes(Node=tree.left))
print("\n No of Nodes in right sub tree")
print(tree.count_Nodes(Node=tree.right))
print("\n No of nodes in given tree are:")
print(tree.count_Nodes(Node=tree))








