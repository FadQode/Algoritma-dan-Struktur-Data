"""
1. a. Vertex of B = B(v) =  3
   b. A(v) + B(v) + C(v) + D(v) + E(v) + F(v)
      2 + 3 + 5 + 1 + 1 + 2 = 13
   c. adj_map: 

"""
# Python3 program to print DFS traversal
# from a given  graph
from collections import defaultdict
 
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
    # Constructor
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
     
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
     
    # A function used by DFS
    def DFSUtil(self, v, visited):
 
        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
 
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    
 
 
# Driver's code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 4)
g.addEdge(3, 0)
 
print("DFS mulai dari vertex 0")
g.DFS(0)
print("\nBFS mulai dari vertex 0")
g.BFS(0)
print("\nFadhil Erdya Qashmal")
 
# This code is contributed by Neelam Yadav
