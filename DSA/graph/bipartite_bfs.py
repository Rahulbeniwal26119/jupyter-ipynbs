from queue import Queue

class Graph:

    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.nodes_num = len(adj_list)
        self.color_matrix = [-1] * self.nodes_num

    def check(self, node):
        queue = Queue()
        queue.put(node)
        self.color_matrix[node] = False;
        while queue.qsize() > 0:
            node = queue.get()
            for adj_node in self.adj_list[node]:
                if self.color_matrix[adj_node] == -1:
                    self.color_matrix[adj_node] = not self.color_matrix[node]
                    queue.put(adj_node)
                elif self.color_matrix[node] == self.color_matrix[adj_node]:
                    return False
        return True

    def is_bipartite(self):
        for i in range(1, self.nodes_num):
            # Loop will run once it is connected
            if self.color_matrix[i] == -1:
                if not self.check(i):
                    return False
        return True

adj_list = [
    [],
    [2],
    [1, 3, 6],
    [2, 4],
    [3, 5, 7],
    [4, 9],
    [2, 9],
    [4, 8],
    [7],
    [6, 5]
]

graph = Graph(adj_list)
print(graph.is_bipartite())
print(graph.color_matrix)
