#Uses python3

import sys
import random
import time
import math

max_weight = 10**9
N = 1000
M = 1000
low_weight = -10**3
high_weight = 10**3


# ------------------------

def dfs(i, adj, visited, edges, current_path):

    current_path.add(i)
    visited[i] = True

    for neigh in adj[i]:
        if neigh in current_path:
            # cycle: add edge , but don't start dfs
            edges.append((i, neigh))
            continue

        if visited[neigh]:
            # neigh not in current path cycle, but has been visited in the past
            # still i itself not visited. So cycle cant exists. So just skip this node and edge
            continue

        if not visited[neigh]:
            # add edge, and also add neigh node
            edges.append((i, neigh))
            dfs(neigh, adj, visited, edges, current_path)

    return


def relax(u, v, adj, cost, dist):
    adj_u = adj[u]

    is_relaxed = False
    for i in range(len(adj_u)):
        if adj_u[i] == v:
            cost_u_v = cost[u][i]
            if dist[v] > dist[u] + cost_u_v:
                dist[v] = dist[u] + cost_u_v
                is_relaxed = True

            break

    return is_relaxed


def negative_cycle(adj, cost):
    # write your code here

    n = len(adj)
    visited = [False for _ in range(n)]
    dist = [max_weight for _ in range(len(adj))]

    for i in range(n):

        if not visited[i]:
            edges = []
            current_path = set()
            dfs(i, adj, visited, edges, current_path)

            V = len(current_path)
            dist[i] = 0

            # do (V-1) edge relaxations, starting node i
            for _ in range(V - 1):
                is_relaxed = False
                for e in edges:
                    if relax(e[0], e[1], adj, cost, dist):
                        is_relaxed = True

                if not is_relaxed:
                    break

            for e in edges:
                if relax(e[0], e[1], adj, cost, dist):
                    return 1

    return 0

# ------------------------


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


def negative_cycle_extra_node(adj, cost):
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

# ------------------------------------


def generate_graph(n, m):
    g = {}
    adj = [[] for i in range(n)]
    cost = [[] for i in range(n)]
    for i in range(n):
        g[i] = set()

    # So we have n nodes from 0 to (n-1)
    for i in range(m):
        u = random.randint(0, n-1)

        possibilities = [i for i in range(n) if i != u]
        if len(possibilities) == 0:
            continue

        v = random.choice(possibilities)
        # print(u, v)
        g[u].add(v)
        # g[v].add(u). commenting out because its a directed graph

    for i in g:
        adjs = list(g[i])
        adj[i].extend(adjs)
        for _ in range(len(adjs)):
            cost[i].append(random.randint(low_weight, high_weight))

    # print(g)
    # print(adj)
    # print(cost)
    return g, adj, cost


if __name__ == "__main__":

    # for i in range(10):
    while True:
        n = random.randint(1, N)  # 1 <= n <= 10**5
        m = random.randint(0, M)  # 0 <= m <= 10**5
        print("n:{0} m:{1}".format(n, m))

        g, adj, cost = generate_graph(n, m)
        # print(g)
        # print(adj)
        # print(cost)

        # adj = [[6], [], [4, 7], [5], [3], [0, 2], [7], [], []]
        # cost = [[235], [], [-278, -151], [-158], [-740], [422, -218], [-689], [], []]

        t1 = time.time()
        n1 = negative_cycle(adj, cost)
        t2 = time.time()
        n2, _ = negative_cycle_extra_node(adj, cost)
        t3 = time.time()

        print(n1, t2-t1)
        print(n2, t3-t2)
        assert n1 == n2, "results differ"
        assert abs((t2-t1) - (t3-t2)) < 0.5, "implementations differ by at least 0.5 sec"


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     # data = [4, 4, 1, 2, 5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
#     # data = [4, 3, 1, 2, -1, 2, 3, -2, 3, 4, -3]
#     # print(data)
#
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     data = data[3 * m:]
#     adj = [[] for _ in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#
#     n, dist = negative_cycle_extra_node(adj, cost)
#
#     print(n)
#     # print(dist)
