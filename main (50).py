# Enter your code here
# linked list pass sum last guru
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None     #starting point of linked list
        
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node   # move the node
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
        
        
    def count(self):
        pass
    
    def insert_begnning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def delete_begnning(self):
        self.head = self.head.next
        def delete_end(self):
            temp = self.head
            while temo.next.next:
                temp = temp.next
            temp.next = None
    def insert_position(self,pos,data):
        if(pos==0):
            self.insert_begnning(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delete_position(self.pos,data):
        if(pos==0):
            self.delete_begnning(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp=temp.next
            temp.next=temp.next.next
    def delete_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data !=value:
            temp = temp.next
        if temp.next is None:
            print("value not found")
            return
        temp.next = temp.next.next
    
    
ll=LinkedList()
ll.insert_begnning(10)
ll.insert_begnning(20)
ll.insert_begnning(30)
ll.insert_position(3,900)
ll.insert_end(40)
ll.delete_position(2)
ll.delete_value(20)
ll.display()
