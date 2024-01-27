from copy import deepcopy


class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.result_matrix = deepcopy(adj_matrix)
        self.nrol = len(adj_matrix)
        self.ncol = len(adj_matrix[0])
        self.nrol_indexes = [-1, 0, 1, 0]
        self.ncol_indexes = [0, 1, 0, -1]

    def dfs(self, starting_row, starting_col, new_color, init_color):
        self.result_matrix[starting_row][starting_col] = new_color
        for i in range(4):
            new_row = starting_row + self.nrol_indexes[i]
            new_col = starting_col + self.ncol_indexes[i]

            if (
                new_row >= 0
                and new_row < self.nrol
                and new_col >= 0
                and new_col < self.ncol
                and self.adj_matrix[new_row][new_col] == init_color
                and self.result_matrix[new_row][new_col] != new_color
            ):
                self.dfs(new_row, new_col, new_color, init_color)

    def fill_color(self, starting_row, starting_col, new_color, init_color):
        self.dfs(starting_row, starting_col, new_color, init_color)


matrix = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

graph = Graph(matrix)
graph.fill_color(1, 1, 3, 1)
print(graph.result_matrix)
