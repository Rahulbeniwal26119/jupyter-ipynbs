class Graph:

    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.visited_array = [0] * len(self.adj_matrix)
        self.V = len(adj_matrix)

    def dfs(self, node, parent):
        self.visited_array[node] = 1
        for neighbour in self.adj_matrix[node]:
            if not self.visited_array[neighbour]:
                if self.dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True
        return False

    def is_cycle(self, start):
        for i in range(self.V):
            if not self.visited_array[i]:
                if self.dfs(i, -1):
                    return True
        return False


matrix = [[1, 4], [0, 2, 4], [1, 3], [4, 2], [0, 1]]
graph = Graph(matrix)
print(graph.is_cycle(0))
