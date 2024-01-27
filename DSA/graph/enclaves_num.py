from queue import Queue


class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.total_rows = len(self.adj_matrix)
        self.total_cols = len(self.adj_matrix[0])
        self.visited_arr = [
            [False] * self.total_cols for _ in range(self.total_rows)
        ]
        self.rowcols = [0, -1, 0, +1]
        self.colcols = [-1, 0, +1, 0]

    def enclaves(self):
        Q = Queue()

        for i in range(self.total_rows):
            for j in range(self.total_cols):
                if i == 0 or j == 0 \
                   or i == self.total_rows - 1 or j == self.total_cols - 1:
                    if self.adj_matrix[i][j] == 'O':
                        Q.put((i , j))
                        self.visited_arr[i][j] = True

        while Q.qsize() > 0:
            row, col = Q.get()
            for i in range(4):
                nrow = row + self.rowcols[i]
                ncol = col + self.colcols[i]
                if nrow >= 0 and nrow < self.total_rows \
                    and ncol >= 0 and ncol < self.total_cols \
                    and not self.visited_arr[nrow][ncol] \
                    and self.visited_arr[nrow][ncol] == 'O':
                    Q.put((nrow, ncol))
                    self.visited_arr[nrow][ncol] = True

        result = 0
        for i in range(self.total_rows):
            for j in range(self.total_cols):
                if not self.visited_arr[i][j] and self.adj_matrix[i][j] == 'O':
                    result += 1

        return result


adj_matrix = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

graph = Graph(adj_matrix)
print(graph.enclaves())
