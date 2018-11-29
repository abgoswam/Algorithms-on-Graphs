#Uses python3

import sys

max_weight = 10**9


def relax_edges(adj, cost, dist):
    n = len(adj)
    relaxed = False
    for u in range(n):
        for iv, v in enumerate(adj[u]):
            cost_u_v = cost[u][iv]
            if dist[v] > dist[u] + cost_u_v:
                dist[v] = dist[u] + cost_u_v
                relaxed = True

    return relaxed


def negative_cycle(adj, cost):
    # write your code here
    # add a dummy node , and add an edge from it to all other nodes with weight 0
    n = [i for i in range(len(adj))]
    c = [0 for _ in range(len(adj))]
    adj.append(n)
    cost.append(c)

    V = len(adj)
    dist = [max_weight for _ in range(len(adj))]
    dist[V - 1] = 0

    for _i in range(V-1):
        got_relaxed = relax_edges(adj, cost, dist)
        # print(_i, dist)
        if not got_relaxed:
            return 0, dist

    final_relaxed = relax_edges(adj, cost, dist)
    if final_relaxed:
        return 1, dist

    return 0, dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
    # data = [4, 3, 1, 2, -1, 2, 3, -2, 3, 4, -3]
    # print(data)

    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)

    n, dist = negative_cycle(adj, cost)

    print(n)
    # print(dist)
