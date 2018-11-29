#Uses python3

import sys

max_weight = 10**9


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

    print(negative_cycle(adj, cost))
