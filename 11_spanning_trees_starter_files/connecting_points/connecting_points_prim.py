#Uses python3

import sys
import math


class DistNode:
    def __init__(self, dist, end_node1, end_node2):
        self.dist = dist
        self.end_node1 = end_node1
        self.end_node2 = end_node2


class BinaryHeapDistNodes:
    def __init__(self):
        self.data = [DistNode(-1, -1, -1)]  #dummy node
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

    def add(self, dnode):
        num_items_in_heap = self.size
        size_array = len(self.data) - 1
        assert num_items_in_heap <= size_array

        if num_items_in_heap == size_array:
            self.data.append(dnode)
        else:
            self.data[num_items_in_heap+1] = dnode

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


tree_vertices_so_far = set()


def minimum_distance(x, y):
    # print("x:{0}".format(x))
    # print("y:{0}".format(y))
    result = 0.
    # write your code here

    bh = BinaryHeapDistNodes()
    bh.add(DistNode(0, 0, 0))

    while bh.size > 0:
        min_dnode = bh.get_min_element()

        if min_dnode.end_node2 in tree_vertices_so_far:
            continue

        tree_vertices_so_far.add(min_dnode.end_node2)
        result += min_dnode.dist

        for i in range(len(x)):
            if i == min_dnode.end_node2:
                continue

            dist = math.sqrt(math.pow((x[min_dnode.end_node2] - x[i]), 2) + math.pow((y[min_dnode.end_node2] - y[i]), 2))
            bh.add(DistNode(dist, min_dnode.end_node2, i))

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    # x = [0, 0, 1, 1]
    # y = [0, 1, 0, 1]
    print("{0:.9f}".format(minimum_distance(x, y)))
