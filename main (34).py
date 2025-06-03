#queue format original
class queue:
    def __init__(self,value):
        self.Q=[]
        self.value=value
        self.front=-1
        self.rare=-1
    def enqueue(self,Q,value):
        if(self.front==-1):
            self.front=0
        self.rare=self.rare+1
        # append it
        self.Q.append(value)
    def dequeue(self):
        # check for empty condition
        # delete element at front
        if self.is_empty():
            return "queue is empty!"
        value = self.queue[self.front]
        self.front += 1 
        if self.front > self.rear:
            self.front = self.rear = -1
        return value
    def is_empty(self):
        return self.front == -1 
    def size(self):
        if self.is_empty():
            return 0
        return self.front-self.rare-1
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print(self.q[self.front:self.rear+1])

            
            
            
            
            
        




