#Uses python3

import sys
import queue


# return 1 if looks good for connected component, else 0
def dfs(adj, v, indicator, ind):
    indicator[v] = ind

    neighbors = adj[v]
    for neigh in neighbors:
        neigh_ind = indicator[neigh]
        if neigh_ind == -1:
            # new node, need to visit
            ret = dfs(adj, neigh, indicator, 1 - ind)
            if ret == 0:
                return 0
        else:
            # neighbor node visited previously, just make sure its different color
            if neigh_ind == ind:
                return 0

    return 1


def bipartite(adj):
    #write your code here
    print(adj)

    n = len(adj)
    indicator = [-1 for _ in range(n)]

    for v in range(n):
        if indicator[v] == -1:
            ret = dfs(adj, v, indicator, 0)
            if ret == 0:
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

    print(bipartite(adj))
