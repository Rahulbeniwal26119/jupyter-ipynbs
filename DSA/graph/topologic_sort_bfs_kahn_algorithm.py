from queue import Queue
class Graph:

    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.V = len(adj_list)
        self.indegree = [0] * self.V

    def topo_sort(self):
        for node in range(self.V):
            for adj_node in self.adj_list[node]:
                self.indegree[adj_node] += 1
        q = Queue()

        for node in range(self.V):
            if not self.indegree[node]:
                q.put(node)

        topo = []

        while q.qsize() > 0:
            current_node = q.get()
            topo.append(current_node)

            for adj_node in self.adj_list[current_node]:
                self.indegree[adj_node] -= 1

                if (self.indegree[adj_node] == 0):
                    q.put(adj_node)

        return topo

adj_list = [
    [],
    [0],
    [0],
    [0]
]

graph = Graph(adj_list)
print(graph.topo_sort())
