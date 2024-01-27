class Graph:

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.n = len(adj_matrix)
        self.m = len(adj_matrix[0])
        self.rowcols = [0, -1, 0, 1]
        self.colcols = [-1, 0, 1, 0]
        self.visited_arr = [[False] * self.m for _ in range(self.n)]

    def dfs(self, i, j):
        self.visited_arr[i][j] = True
        print(i, j)

        for loop_var in range(4):
            nrow = i + self.rowcols[loop_var]
            ncol = j + self.colcols[loop_var]
            if nrow < self.n and nrow >= 0 and ncol < self.m and ncol >= 0 and not self.visited_arr[nrow][ncol] and self.adj_matrix[nrow][ncol] == 'O':
                self.dfs(nrow, ncol)

    def capture(self):
        # traverse first and last row
        for j in range(self.m):
            if not self.visited_arr[0][j] and self.adj_matrix[0][j] == 'O':
                self.dfs(0, j)

            if not self.visited_arr[self.n - 1][j] and self.adj_matrix[self.n - 1][j] == 'O':
                self.dfs(self.n -1, j)

        for i in range(self.n):
            if not self.visited_arr[i][0] and self.adj_matrix[i][0] == 'O':
                self.dfs(i, 0)

            if not self.visited_arr[i][self.m -1] and self.adj_matrix[i][self.m - 1] == 'O':
                self.dfs(i, self.m - 1)

        for i in range(self.n):
            for j in range(self.m):
                if not self.visited_arr[i][j] and self.adj_matrix[i][j] == 'O':
                    self.adj_matrix[i][j] = 'X'

adj_matrix = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
    ['X', 'X', 'O', 'O']
]

graph = Graph(adj_matrix)
graph.capture()
print(graph.adj_matrix)
print(graph.visited_arr)
