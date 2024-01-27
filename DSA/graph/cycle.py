from queue import Queue

class Graph(object):
    """docstring for Graph."""

    def __init__(self, adj_list: dict[any, list]):
        super(Graph, self).__init__()
        self.adj_list = adj_list
        self.visited = {}

    def detect(self, src) -> bool :
        self.visited[src] = True
        queue = Queue()
        # q.put((node, parent_node))
        queue.put((src, -1))

        while queue.qsize() != 0:
            node, parent = queue.get()

            for neighbour in self.adj_list[node]:
                if not self.visited.get(neighbour):
                    self.visited[neighbour] = True
                    queue.put((neighbour, node))
                elif neighbour != parent:
                    #  if a node is already visited but that is not parent
                    # that means somebody also has path to it
                    return True
        return False

    def is_cycle(self, src) -> bool:
        for node in self.adj_list:
            if not self.visited.get(node):
                if self.detect(node):
                    return True
        return False

adj_list = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2],
    5: [6],
    6: [5],
    7: [8, 9],
    8: [7, 9],
    9: [7, 8]
}

graph = Graph(adj_list)
print(graph.is_cycle(1))
