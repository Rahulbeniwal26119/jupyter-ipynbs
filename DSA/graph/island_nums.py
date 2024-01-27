from queue import Queue
from enum import Enum

class Constants(Enum):
    VISITED = 1
    LAND = 1

class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.total_rows = len(self.adj_matrix)
        self.total_cols = len(self.adj_matrix[0])
        self.islands_count = 0
        self.visited = [
            [False for _ in range(self.total_cols)] for _ in range(self.total_rows)
        ]

    def bfs(self, row, col):
        self.visited[row][col] = Constants.VISITED.value
        q = Queue()
        q.put((row, col))
        neightbours = [-1, 0, 1]

        while q.qsize() != 0:
            row, col = q.get()

            ## traverse all surronding neighbours
            for nrrow in neightbours:
                for nrcol in neightbours:
                    nrow = row + nrrow
                    ncol = col + nrcol
                    if (
                        nrow >= 0
                        and nrow < self.total_rows
                        and ncol >= 0
                        and ncol < self.total_cols
                        and self.adj_matrix[nrow][ncol] == Constants.LAND.value
                        and self.visited[nrow][ncol] != Constants.VISITED.value
                    ):
                        self.visited[nrow][ncol] = Constants.VISITED.value
                        q.put((nrow, ncol))

    def calculate_island_nums(self):
        for row in range(self.total_rows):
            for col in range(self.total_cols):
                if not self.visited[row][col] and self.adj_matrix[row][col] == Constants.LAND.value:
                    self.islands_count += 1
                    self.bfs(row, col)


adj_matrix = [
    [0, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0]
]

g = Graph(adj_matrix)
g.calculate_island_nums()
print(g.islands_count)
