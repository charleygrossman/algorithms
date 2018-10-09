# Compute and return the node counts of the five largest SCCs of a given graph
from collections import deque
import structs.graph


def main():
    with open('scc.txt') as file:
        try:
            # An adjacency-list representation as a dictionary of Vertex objects
            adj_list = data_as_dict(file)
            scc_sizes = scc(adj_list)
            top_five = five_largest(scc_sizes)
            print(top_five)
        except:
            print("Error handling strongly-connected components data")


def data_as_dict(file):
    d = {}
    for line in file.readlines():
        v, w = map(int, line.strip().split())
        v = Vertex(v)
        w = Vertex(w)
        if v not in adj_list:
            d[v] = [w]
        else:
            if w not in adj_list[v]:
                d[v].append(w)
    return d


def scc(G):
    scc_number = 1
    scc_sizes = {scc_number: 0}
    for v in G.keys():
        if !v.visited:
            scc_sizes[scc_number] = bfs(G, v, scc_number)
            scc_number += 1
    return scc_sizes

def bfs(G, s, scc_number):
    s.visited = True
    s.scc = scc_number
    scc_count = 1
    Q = deque([s])
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if !w.visted():
                w.visited = True
                w.scc = scc_number
                Q.append(w)


# NOTE: Output example: "500,400,300,200,100"
def five_largest(scc_sizes):
    retval = []
    for k,v in scc_sizes.items():
        v.sort(key=lambda x: x, reverse=True)
    i = 0
    sizes = scc_sizes.values()
    while len(retval) < 5 and i < len(sizes):
        if sizes[i] not in retval:
            retval.append(sizes[i])
        i += 1
    return ",".join(retval)


if __name__ == "__main__":
    main()


class Vertex(object):

    def __init__(self, value, visited=False, scc=None):
        self.value = value
        self.visited = visited
        self.scc = scc

    def __str__():
        return "Value: {}, Visited: {}, SCC #: {}".format(value, visited, scc)

    def __repr__():
        return "<Vertex object representation>"
