class Graph:

    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.visited_arr = [False] * len(adj_list)
        self.path_visited_arr = [False] * len(adj_list)
        self.V = len(adj_list)

    def dfs(self, node):
        self.visited_arr[node] = True
        self.path_visited_arr[node] = True

        for adj_node in self.adj_list[node]:
            if not self.visited_arr[adj_node]:
                if self.dfs(adj_node) == True:
                    return True
            elif self.path_visited_arr[adj_node]:
                return True
        self.path_visited_arr[node] = False
        return False

    def isCyclic(self):
        for node in range(1, self.V):
            if not self.visited_arr[node]:
                if self.dfs(node) == True:
                    return True
        return False


adj_matrix = [
    [],
    [2],
    [3],
    [4, 7],
    [5],
    [6],
    [],
    [5],
    [2, 9],
    [10],
    [8]
]

g = Graph(adj_matrix)
print(g.isCyclic())
