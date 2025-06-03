#queue format
class queue:
    def __init__(self,Q,value):
        self.Q=Q
        self.value=value
    def enqueue(self,Q,value):
        return Q.append(value)