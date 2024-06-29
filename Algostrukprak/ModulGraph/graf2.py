class Graph(object):
    # Initialisasi matriks
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    # Tambah edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Verteks yang sama %d dan %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Hapus edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("Tidak terdapat edge antara %d dan %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=" ")
            print()
    
    def bfs(self, start):
        visited = [False] * self.size
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            print(start, end=' ')
            for i in range(self.size):
                if self.adjMatrix[start][i] == 1 and (not visited[i]):
                    queue.append(i)
                    visited[i] = True

    def dfs(self, start):
        visited = [False] * self.size
        self._dfs(start, visited)

    def _dfs(self, start, visited):
        visited[start] = True
        print(start, end=' ')
        for i in range(self.size):
            if self.adjMatrix[start][i] == 1 and (not visited[i]):
                self._dfs(i, visited)
# Driver code

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 2)


"""
   1
 / | 
0  |      _   
 \\      | | 
   2 -- 3-

"""

g.bfs(2)
print("\n")
g.dfs(2)
print("\n")
g.print_matrix()
