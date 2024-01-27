from queue import Queue
from copy import deepcopy
from enum import Enum


class RowDirection(Enum):
    UP = -1
    DOWN = +1
    LEFT = 0
    RIGHT = 0


class GraphDefinations(Enum):
    ROTTEN = 2
    FRESH = 1


class ColDirection(Enum):
    UP = 0
    DOWN = 0
    LEFT = -1
    RIGHT = +1


class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.nrows = len(adj_matrix)
        self.ncols = len(adj_matrix[0])
        self.result_matrix = deepcopy(adj_matrix)
        self.rows_direction = [
            RowDirection.UP.value,
            RowDirection.DOWN.value,
            RowDirection.LEFT.value,
            RowDirection.RIGHT.value,
        ]
        self.col_direction = [
            ColDirection.UP.value,
            ColDirection.DOWN.value,
            ColDirection.LEFT.value,
            ColDirection.RIGHT.value,
        ]

    def calculate_time_to_rottern_all_orange(self):
        queue = Queue()
        total_fresh = 0
        converted_oranges = 0

        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.adj_matrix[i][j] == GraphDefinations.ROTTEN.value:
                    queue.put(((i, j), 0))
                elif self.adj_matrix[i][j] == GraphDefinations.FRESH.value:
                    total_fresh += 1
        tm = 0

        while queue.qsize() != 0:
            ((row, col), t) = queue.get()
            tm = max(tm, t)

            for i in range(4):
                nrow = row + self.rows_direction[i]
                ncol = col + self.col_direction[i]

                if (
                    nrow >= 0
                    and nrow < self.nrows
                    and ncol >= 0
                    and ncol < self.ncols
                    and self.result_matrix[nrow][ncol] != GraphDefinations.ROTTEN.value
                    and self.adj_matrix[nrow][ncol] == GraphDefinations.FRESH.value
                ):
                    queue.put(((nrow, ncol), t + 1))
                    self.result_matrix[nrow][ncol] = GraphDefinations.ROTTEN.value
                    converted_oranges += 1

        if converted_oranges != total_fresh:
            return -1
        return tm


matrix = [
    [0, 1, 2], 
    [0, 1, 2], 
    [2, 1, 1]
]

graph = Graph(matrix)
print(graph.calculate_time_to_rottern_all_orange())
