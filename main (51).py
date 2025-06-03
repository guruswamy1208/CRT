# double linked list
class Node:
    def __init__(self,prv,next,data):
        self.prv = None
        self.next = None
        self.data = data
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_begnning(self,data):
        new_node=Node(None,None,data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prv = new_node
            self.head = new_node
    
    def delete_begnning(self):
            self.head = self.head.next
            self.head.prv = None
            
    def delete_end(self):
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prv.next = None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
ll=DoublyLinkedList()
ll.insert_begnning(10)
ll.insert_begnning(20)
ll.insert_begnning(30)
ll.display()
ll.delete_begnning(30)        
ll.display()
        
        
        
        
        
        
        