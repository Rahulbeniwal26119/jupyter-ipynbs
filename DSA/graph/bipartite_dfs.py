from queue import Queue

class Graph:

    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.nodes_num = len(adj_list)
        self.color_matrix = [-1] * self.nodes_num

    def check(self, node, color):
        self.color_matrix[node] = color
        for adj_node in self.adj_list[node]:
            if self.color_matrix[adj_node] == -1:
                return self.check(adj_node, not color)
            elif color == self.color_matrix[adj_node]:
                return False
        return True

    def is_bipartite(self):
        for i in range(1, self.nodes_num):
            if self.color_matrix[i] == -1:
                if not self.check(i, 0):
                    return False
        return True

adj_list = [
    [],
    [2],
    [1, 3, 6],
    [2, 4],
    [3, 5, 7],
    [4, 6],
    [2, 5],
    [4, 8],
    [7],
]

graph = Graph(adj_list)
print(graph.is_bipartite())
print(graph.color_matrix)
