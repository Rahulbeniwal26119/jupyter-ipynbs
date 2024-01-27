class Graph:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.V = len(adj_list)
        self.visited_arr = [0] * self.V

    def dfs(self, node, stack):
        self.visited_arr[node] = True
        for adj_node in self.adj_list[node]:
            if not self.visited_arr[adj_node]:
                self.dfs(adj_node, stack)
        stack.append(node)

    def topo_sort(self):
        stack = []
        for node in range(self.V):
            if not self.visited_arr[node]:
                self.dfs(node, stack)
        return stack[::-1]

adj_list = [
    [],
    [0],
    [0],
    [0]
]

graph = Graph(adj_list)
print(graph.topo_sort())
