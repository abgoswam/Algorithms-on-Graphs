#Uses python3

import sys
import queue
import random

max_weight = 10**9
N = 10
M = 10

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist


class BinaryHeap:
    def __init__(self):
        self.data = [Node(-1, -1)]  #dummy node
        self.size = 0

    def get_min_element(self):
        assert self.size > 0

        if self.size == 1:
            self.size = 0
            return self.data[1]

        min_elem = self.data[1]
        self.data[1] = self.data[self.size]
        self.size -= 1
        self.siftdown(1)
        return min_elem

    def add(self, node):
        num_items_in_heap = self.size
        size_array = len(self.data) - 1
        assert num_items_in_heap <= size_array

        if num_items_in_heap == size_array:
            self.data.append(node)
        else:
            self.data[num_items_in_heap+1] = node

        self.size += 1
        self.siftup(self.size)

    def siftup(self, x):
        while x > 1:
            px = x // 2
            if self.data[px].dist < self.data[x].dist:
                break

            self.data[x], self.data[px] = self.data[px], self.data[x]
            x = px

    def siftdown(self, x):
        lx = 2*x
        rx = 2*x + 1

        if lx > self.size:
            return

        candidate = lx
        if rx <= self.size and self.data[rx].dist < self.data[candidate].dist:
            candidate = rx

        if self.data[candidate].dist < self.data[x].dist:
            self.data[x], self.data[candidate] = self.data[candidate], self.data[x]
            x = candidate
            return self.siftdown(x)


def distance_proper(adj, cost, s, t):
    # write your code here
    # print(adj)
    # print(cost)
    dist = [max_weight for _ in range(len(adj))]
    dist[s] = 0

    min_distances_found = set()
    binary_heap = BinaryHeap()

    for i in range(len(adj)):
        node = Node(i, dist[i])
        binary_heap.add(node)

    while binary_heap.size > 0:
        unode = binary_heap.get_min_element()
        u = unode.id
        if u in min_distances_found:
            continue

        min_distances_found.add(u)
        u_adj = adj[u]
        u_cost = cost[u]

        for v_idx, v in enumerate(u_adj):
            if dist[v] > dist[u] + u_cost[v_idx]:
                dist[v] = dist[u] + u_cost[v_idx]
                binary_heap.add(Node(v, dist[v]))

    return -1 if dist[t] == max_weight else dist[t]


def relax(u, u_adj, u_cost, dist):
    relaxed = False
    for v_idx, v in enumerate(u_adj):
        if dist[v] > dist[u] + u_cost[v_idx]:
            dist[v] = dist[u] + u_cost[v_idx]
            relaxed = True

    return relaxed


def distance_naive(adj, cost, s, t):
    #write your code here

    # print(adj)
    # print(cost)

    dist = [max_weight for _ in range(len(adj))]
    dist[s] = 0

    while True:
        is_relaxed = False
        for u in range(len(adj)):
            got_relaxed = relax(u, adj[u], cost[u], dist)
            if got_relaxed:
                is_relaxed = True

        if not is_relaxed:
            break

    return -1 if dist[t] == max_weight else dist[t]


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
            cost[i].append(random.randint(1, 10**3))

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
        print(adj)
        print(cost)

        s = random.randint(0, n-1)
        t = random.randint(0, n - 1)
        print("s:{0} t:{1}".format(s, t))

        dist_proper = distance_proper(adj, cost, s, t)
        dist_naive = distance_naive(adj, cost, s, t)

        print("dist_proper:{0}".format(dist_proper))
        print("dist_naive:{0}".format(dist_naive))

        assert dist_proper == dist_naive, "Aha. differ"

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     data = data[3 * m:]
#
#     adj = [[] for _ in range(n)]
#     cost = [[] for _ in range(n)]
#
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#
#     s, t = data[0] - 1, data[1] - 1
#     print(distance(adj, cost, s, t))
