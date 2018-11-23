import random


def generate_graph(n, m):
    g = {}
    adj = [[] for i in range(n)]
    for i in range(n):
        g[i] = set()

    # So we have n nodes from 0 to (n-1)
    for i in range(m):
        u = random.randint(0, n-1)
        v = random.choice([i for i in range(n) if i != u])
        print(u, v)
        g[u].add(v)
        g[v].add(u)

    for i in g:
        adj[i].extend(list(g[i]))

    # print(g)
    # print(adj)
    return g, adj


# N, M = map(lambda x: int(x), input().split())
# g, adj = generate_graph(N, M)
# print(g)
# print(adj)

N = 10
M = 10

for i in range(10):
    n = random.randint(2, N)  # 2 <= n <= 10**5
    m = random.randint(0, M)  # 0 <= m <= 10**5
    print("n:{0} m:{1}".format(n, m))

    g, adj = generate_graph(n, m)
    print(g)
    print(adj)

