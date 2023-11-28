from typing import Any, Optional

graph = {
    1: [2],
    2: [3],
    3: [],
    4: [3, 6],
    5: [3],
    6: [5],
}


def iterative_dfs(g, start):
    s = []
    s.append(start)
    vizited = set()
    while s:
        vertex = s.pop()
        for i in graph[vertex]:
            if i not in vizited:
                vizited.add(i)
                s.append(i)
        print(vertex)


def bfs(g, start):
    queue = [start]
    vizited = set([start])
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for i in g[vertex]:
            if i not in vizited:
                queue.append(i)
                vizited.add(vertex)


def kruskal_algo(graph):
    components_set = set()


class DisjointSet:

    def __init__(self):
        self.parent = dict()
        self.rank = dict()

    # создает новое множество
    def make_set(self, x):
        self.parent[x] = x  # В данном случае p(x) = x то есть он замкнут сам на себя
        self.rank[x] = 0

    def i_get(self, x):  # итеративная реализация эвристики сжаия путей
        root = x
        prev_p = self.parent[x]
        if prev_p != x:
            while self.parent[root] != root:
                root = self.parent[root]
            while prev_p != x:
                self.parent[x] = root
                x = prev_p
                prev_p = self.parent[x]
        return self.parent[x]

    def r_get(self, x):  # рекурсивное получение с эвристикой сжатия путей
        if x != self.parent[x]:
            self.parent[x] = self.r_get(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.i_get(x)
        y = self.i_get(y)
        if x != y:
            if self.rank[y] > self.rank[x]:
                x, y = y, x
            self.parent[y] = x
            if self.rank[y] == self.rank[x]:
                self.rank[x] += 1

    def __str__(self):
        return str(self.parent)


def parse_graph(file: str):
    with open(file, 'r') as file:
        data = file.read()
    data = data.split('\n')
    d = []
    for i in data:
        d += [i.split()]
    print(d)

    vertexes = d[0]
    graph = dict()
    edges = []

    for row in range(1, len(d)):
        graph[vertexes[row - 1]] = []
        for col in range(len(d[row])):
            weight = int(d[row][col])
            if weight > 0:
                graph[vertexes[row - 1]] += [(vertexes[col], weight)]
                if col > row - 1:
                    edges += [(weight, vertexes[row - 1], vertexes[col])]

    print(edges)
    kruskal_with_edges_list(edges)


def kruskal_with_dict(graph):
    s = DisjointSet()
    tree = dict()
    for i in graph:
        s.make_set(i)
        graph[i] = sorted(graph[i], key=lambda x: x[1])
    for i in graph:
        for g in graph[i]:
            if s.i_get(i) != s.i_get(g[0]):
                tree[i] = g
                s.union(i, g[0])
                break
    print(graph)
    print(tree)


def kruskal_with_edges_list(edges):
    s = DisjointSet()
    tree_edges = []
    edges = sorted(edges, key=lambda x: x[0])
    for i in edges:
        s.make_set(i[1])
        s.make_set(i[2])
    for i in edges:
        if s.i_get(i[1]) != s.i_get(i[2]):
            tree_edges.append(i)
            s.union(i[1], i[2])
    print(tree_edges)

    # right_shift = 1
    # edge_set = set()
    # graph = dict()
    # vertexes = data[0]
    # for g in range(len(vertexes)):
    #     graph[vertexes[g]] = []
    #     for i in range(len(data[g+1]):
    #         if data[i]


parse_graph("example.txt")

# a = DSElement(1)
# b = DSElement(2)
# c = DSElement(3)
# d = DSElement(4)
#
# DisjointSet.union(a, b)
#
# DisjointSet.get(a)
#
# DisjointSet.union(a, c)
