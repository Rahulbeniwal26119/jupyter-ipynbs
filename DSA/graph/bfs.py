import queue
from collections import defaultdict


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs(adj, start):
    visited = {}
    que = queue.Queue()

    que.put(start)
    visited[start] = True
    result = [start]

    while que.qsize() != 0:
        u = que.get()
        visited[u] = True

        for v in adj[u]:
            if v not in visited:
                que.put(v)
                result.append(v)
        
    return result

def main():
    adj = defaultdict(list)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 4)
    addEdge(adj, 2, 5)
    addEdge(adj, 3, 6)

    start = 3

    for i in bfs(adj, start):
        print(i, end=" ")

main()

