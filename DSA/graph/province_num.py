from collections import defaultdict


class Graph:
    
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, start_node):
        visited = {}
        province_count = 0

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

        for node in [start_node, *self.adj.keys()]:
            if visited.get(node) != True:
                province_count += 1
                worker(node)
            else:
                continue

        return visited.keys(), province_count

g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(7, 8)
g.add_edge(9, 10)

print(g.dfs(7))



