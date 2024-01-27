class Graph:

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.row_num = len(adj_matrix)
        self.col_num = len(adj_matrix[0])
        self.rowcols = [0, -1, 0, +1]
        self.colcols = [-1, 0, +1, 0]
        self.visited_arr = [[0] * self.col_num for _ in range(self.row_num)]

    def dfs(self, row, col, coordinates, base_row, base_col):
        self.visited_arr[row][col] = 1
        coordinates.append((row - base_row, col - base_col))

        for i in range(4):
            nrow = row + self.rowcols[i]
            ncol = col + self.colcols[i]

            if nrow >= 0 and nrow < self.row_num and ncol >= 0 and ncol < self.col_num and not self.visited_arr[nrow][ncol] and self.adj_matrix[nrow][ncol] == 1:
                self.dfs(nrow, ncol, coordinates, base_row, base_col)

    def countDistinctIsland(self):
        st = set()

        for i in range(self.row_num):
            for j in range(self.col_num):
                if not self.visited_arr[i][j] and self.adj_matrix[i][j] == 1:
                    coordinates = []
                    self.dfs(i, j, coordinates, i, j)
                    st.add(frozenset(coordinates))

        print(st)
        return len(st)


adj_matrix = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 0]
]

graph = Graph(adj_matrix)
print(graph.countDistinctIsland())
