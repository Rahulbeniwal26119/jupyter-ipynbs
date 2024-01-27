from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, start_node):
        visited = {}
        def worker(start_node):
            nonlocal visited
            if visited.get(start_node) == True:
                # if already visited
                return

            visited[start_node] = True
            adj_nodes = self.adj[start_node]

            if not adj_nodes:
                return
            else:
                for current_node in adj_nodes:
                    worker(current_node)

        worker(start_node)
        return visited.keys()

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)

print(g.dfs(0))



