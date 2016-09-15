import networkx as nx
import numpy as np


def match(s1, s2):
    isMatch = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if isMatch:
                return False
            else:
                isMatch = True
    return isMatch

def genAdjMatrix(words):
    size = len(words)
    M = [[0 for _ in range(len(words))] for _ in range(len(words))]
    for y in range(len(words)):
        for x in range(y, len(words)):
            if match(words[x], words[y]):
                M[y][x] += 1
                M[x][y] += 1
    return M

nodes = ["abc", "bbb", "aab", "acc", "ccc"]
d = dict(zip(nodes, range(len(nodes))))
A = np.array(genAdjMatrix(nodes))
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())
try:
    print(len(nx.dijkstra_path(G, d['abc'], d['ccc'])) - 1)
except:
    print(-1)
