#Uses python3

import sys


def dfs(adj, v, visited, path):
    visited[v] = True

    for neigh in adj[v]:
        if neigh in path:
            return 1

        if not visited[neigh]:
            path.add(neigh)
            r = dfs(adj, neigh, visited, path)
            if r == 1:
                return 1
            path.remove(neigh)

    return 0


def acyclic(adj):
    # print("adj : {0}".format(adj))

    n = len(adj)
    visited = [False for _ in range(n)]

    for v in range(n):
        if not visited[v]:
            path = set()
            path.add(v)
            r = dfs(adj, v, visited, path)
            if r == 1:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1]
    # print("data : {0}".format(data))

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
