#Uses python3

import sys
import queue
import random

N = 10**2
M = 10**2


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


def bipartite_DFS(adj):
    #write your code here
    #print(adj)

    n = len(adj)
    indicator = [-1 for _ in range(n)]

    for v in range(n):
        if indicator[v] == -1:
            ret = dfs(adj, v, indicator, 0)
            if ret == 0:
                return 0

    return 1


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


def generate_graph(n, m):
    g = {}
    adj = [[] for i in range(n)]
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
        g[v].add(u)

    for i in g:
        adj[i].extend(list(g[i]))

    # print(g)
    # print(adj)
    return g, adj


if __name__ == "__main__":

    # for i in range(10):
    while True:
        n = random.randint(1, N)  # 1 <= n <= 10**5
        m = random.randint(0, M)  # 0 <= m <= 10**5
        print("n:{0} m:{1}".format(n, m))

        g, adj = generate_graph(n, m)
        # print(g)
        print(adj)

        bipartite_dfs = bipartite_DFS(adj)
        bipartite_bfs = bipartite_BFS(adj)

        print("bipartite DFS:{0}".format(bipartite_dfs))
        print("bipartite BFS:{0}".format(bipartite_bfs))

        assert bipartite_dfs == bipartite_bfs, "Aha. differ"



