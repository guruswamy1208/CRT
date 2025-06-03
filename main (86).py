# Graphlist program
class Graphlist:
    def __init__(self):
        self.graph={}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        # add the node v if it's not in the graph
        if v not in self.graph:
            self.graph[v]=[]
        # since it's an undirected graph,add each to the others list
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def display(self):
        print("Adjacency list:")
        for i in self.graph:
            print(f"{i}----->{self.graph[i]}")
# inserting nodes           
g=Graphlist()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,7)
# display the adjancy list
g.display()
        
  
    

    

