class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.V = len(adj_list)
        self.visited = [False] * self.V
        self.path_visited = [False] * self.V
        self.safe_node_check = [False] * self.V

    def check_cycle(self, node):
        self.visited[node] = True
        self.path_visited[node] = True

        for adj_node in self.adj_list[node]:
            if not self.visited[adj_node]:
                if self.check_cycle(adj_node):
                    return True
            elif self.path_visited[adj_node]:
                return True
        self.safe_node_check[node] = True
        self.path_visited[node] = False
        return False

    def eventual_safe_node(self):
        for node in range(self.V):
            if not self.visited[node]:
                self.check_cycle(node)
        safe_nodes = []
        for node, result in enumerate(self.safe_node_check):
            if result == True:
                safe_nodes.append(node)
        return safe_nodes


adj_list = [
    [1],
    [2, 8],
    [3],
    [4, 5],
    [6],
    [6],
    [7],
    [],
    [9],
    [10],
    [8],
    [9]
]

graph = Graph(adj_list)
print(graph.eventual_safe_node())
