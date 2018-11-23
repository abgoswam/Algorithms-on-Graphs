#Uses python3

import sys
import queue


def bfs(adj, v, indicator):
    q = queue.Queue()

    indicator[v] = 1
    q.put(v)

    while q.qsize():
        item = q.get()
        neighbors = adj[item]
        for neigh in neighbors:
            if indicator[neigh] == -1:
                indicator[neigh] = 1 - indicator[item]
                q.put(neigh)
            elif indicator[item] == indicator[neigh]:
                return 0

    return 1


def bipartite_BFS(adj):

    n = len(adj)
    indicator = [-1 for _ in range(n)]

    for i in range(n):
        if indicator[i] == -1:  # not visited
            is_bipartite = bfs(adj, i, indicator)
            if not is_bipartite:
                return 0

    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    # print(data)

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(bipartite_BFS(adj))
