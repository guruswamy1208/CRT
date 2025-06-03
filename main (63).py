class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
class bst:
    def __init__(self):
        self.root=None
        
    def insert(self,data,root):
    # if root==empty:
        # starting point of a tress
        if(root is None):
            # create a node:
            return Node(data)
    # if data<root----> left rcc call
        if(data<root.data):
            root.left=self.insert(data,root.left)
        elif(data>root.data):
            root.right=self.insert(data,root.right)
        return root
    # if data>root----> left rcc call