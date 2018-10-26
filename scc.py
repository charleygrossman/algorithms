# Compute and return the vertex counts of the five largest SCCs of a given graph
# NOTE: Recommended DFS
from collections import deque
import traceback
import sys

def main():
    with open('scc.txt') as file:
        try:
            adj_list = data_as_adj_list(file)
            scc_sizes = scc(adj_list)
            top_five = five_largest(scc_sizes)
            print(top_five)
        except Exception as e:
            print(traceback.format_exception(*sys.exc_info()))
            raise


# return an adjacency-list representation as a dictionary of Vertex objects
def data_as_adj_list(file):
    d = {}
    for line in file.readlines()[:10]:
        v, w = map(int, line.strip().split())
        # TODO: These are new objects, hence unique when they shouldn't be
        # Tuple fix
        v = (v, False, None)
        w = (w, False, None)
        if v not in d:
            d[v] = [w]
        else:
            if w not in d[v]:
                d[v].append(w)
    return d


# Compute all SCCs, and return a dictionary with the vertex count of each
def scc(G):
    scc_number = 1
    scc_sizes = {scc_number: 0}
    for v in G:
        if not v[1]:
            scc_sizes[scc_number] = bfs(G, v, scc_number)
            scc_number += 1
    return scc_sizes


def bfs(G, s, scc_number):
    # s[1] = True
    # s[2] = scc_number
    tmp = G[s]
    G[s] = (tmp[0], True, scc_number)
    scc_count = 1
    Q = deque([s])
    while Q:
        v = Q.popleft()
        for w in G[v]:
            # If value in ytup
            # if not w[1]:
                # w[1] = True
                # w[2] = scc_number
                tmp = G[w]
                G[w] = (tmp[0], True, scc_number)
                scc_count += 1
                Q.append(w)
    return scc_count


# Compute the five SCCs with the most vertices and return their sizes
# NOTE: Output example: "500,400,300,200,100"
def five_largest(scc_sizes):
    retval = []
    sizes = sorted(scc_sizes.values(), reverse=True)
    i = 0
    while len(retval) < 5 and i < len(sizes):
        if sizes[i] not in retval:
            retval.append(sizes[i])
        i += 1
    return ",".join(map(str, retval))


class Vertex(object):

    def __init__(self, value, visited=False, scc=None):
        self.value = value
        self.visited = visited
        self.scc = scc

    def __str__(self):
        return "Value: {}, Visited: {}, SCC #: {}".format(self.value, self.visited, self.scc)


if __name__ == "__main__":
    main()
