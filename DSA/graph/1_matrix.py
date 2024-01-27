from queue import Queue
from copy import deepcopy

class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.n = len(adj_matrix)
        self.m = len(adj_matrix[0])

        self.visited = [[0] * self.m for _ in range(self.n)]
        self.result = deepcopy(self.visited)
        self.row_cols = [-1, 0, +1, 0]
        self.col_cols = [0, +1, 0, -1]

    def nearest(self):
        Q = Queue()

        for i in range(self.n):
            for j in range(self.m):
                if(self.adj_matrix[i][j] == 1):
                    Q.put(((i, j), 0))
                    self.visited[i][j] = 1
        while Q.qsize() != 0:
            ((row, col), steps) = Q.get()
            self.result[row][col] = steps

            for i in range(4):
                nrow = row + self.row_cols[i]
                ncol = col + self.col_cols[i]

                if nrow >= 0 and nrow < self.n and ncol >= 0 and ncol < self.m \
                 and self.visited[nrow][ncol] != 1:
                    self.visited[nrow][ncol] = 1
                    Q.put(((nrow, ncol), steps + 1))

def generate_matrix():
    V, E = map(int, input().split())
    adj_matrix = [[0] * V for _ in range(V)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    return adj_matrix

# print(generate_matrix())
adj_matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 1]
]

graph = Graph(adj_matrix)
graph.nearest()

print(graph.result)
