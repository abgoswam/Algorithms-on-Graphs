#Uses python3

import sys
import queue


def bfs(adj, v, t):
    q = queue.Queue()
    visited = [False for _ in range(len(adj))]
    dist = [0 for _ in range(len(adj))]

    visited[v] = True
    q.put(v)
    while q.qsize():
        item = q.get()
        if item == t:
            return dist[item]

        for neigh in adj[item]:
            if not visited[neigh]:
                visited[neigh] = True
                dist[neigh] = dist[item] + 1
                q.put(neigh)

    return -1


def distance(adj, s, t):
    #write your code here
    return bfs(adj, s, t)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
