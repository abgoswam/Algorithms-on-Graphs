#Uses python3

import sys

sys.setrecursionlimit(200000)


def explore(g, visited, order, v):
    visited[v] = True
    neighs = g[v]
    for neighbor in neighs:
        if not visited[neighbor]:
            explore(g, visited, order, neighbor)

    order.append(v)


def number_of_strongly_connected_components(adj, adj_R):
    result = 0
    #write your code here

    # work on the reverse graph adj_R
    n = len(adj_R)
    visited = [False for _ in range(n)]
    order = []
    for v in range(n):
        if not visited[v]:
            explore(adj_R, visited, order, v)

    order_prime = order[::-1]
    visited = [False for _ in range(n)]
    order = []
    for v in order_prime:
        if not visited[v]:
            explore(adj, visited, order, v)
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    adj_R = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_R[b - 1].append(a - 1)

    print(number_of_strongly_connected_components(adj, adj_R))
