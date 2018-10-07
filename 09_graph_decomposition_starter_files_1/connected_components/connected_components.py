#Uses python3

import sys


class Group:
    def __init__(self, n):
        self.cells = n
        self.parent = [-1 for _ in range(n)]
        self.group_count = n

    def find(self, v):
        while self.parent[v] != -1:
            v = self.parent[v]
        return v

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.group_count -= 1

    def get_group_count(self):
        return self.group_count


def number_of_components(adj):
    # write your code here

    group = Group(len(adj))
    for v in range(len(adj)):
        for n in adj[v]:
            group.union(v, n)

    return group.get_group_count()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
