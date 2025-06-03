#queue format
class queue:
    def __init__(self,value):
        self.Q=[]
        self.value=value
        self.front=-1
        self.rare=-1
    def enqueue(self,Q,value):
        return Q.append(value)
    def dequeue(self,Q):
        return Q.pop()