#Uses python3

import sys


def dfs(adj, v, t, visited):
    visited[v] = True
    neighbors = adj[v]
    for neigh in neighbors:
        if neigh == t:
            return 1
        if not visited[neigh]:
            res = dfs(adj, neigh, t, visited)
            if res:
                return 1
    return 0


def reach(adj, x, y):
    # write your code here
    visited = [False for _ in range(len(adj))]
    return dfs(adj, x, y, visited)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    # print("edge : {0}".format(edges))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
