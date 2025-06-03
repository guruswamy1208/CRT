# Enter your code here
# Graphlist program with bfs
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
            
    def bfs(self,start):
        visited = set() # empty set to keep try
        queue=[start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                for i in self.graph[vertex]:
                    if i not in visited:
                        queue.append(i) 
    def dfs(self,start,visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for i in self.graph[start]:
            if i not in visited:
                self.dfs(i,visited)
# inserting nodes  

g=Graphlist()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(5,6)
g.add_edge(6,7)
# display the adjancency list
g.display()
g.bfs(1) # Perform BFS starting from node 1
g.display()
g.dfs(1)
# Adjacencey matrix representation of the same Graph
adj_matrix=[
[0,1,1,0,0,0,0],
[1,0,0,1,0,0,0],
[1,0,0,1,0,0,0],
[0,1,1,0,0,0,0],
[0,0,0,1,0,1,0],
[0,0,0,0,1,0,1],
[0,0,0,0,0,1,0]
]

        
  
    

    

