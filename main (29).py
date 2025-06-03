#queue format
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