import random

def main():

    # There is a probability p that there is an edge between any two nodes
    # For each p from 1 to 100 (discrete), generate a random graph of size 100
    # Then, run dfs and count the number of connected components
    # There should be a critical p when the graph breaks from a single component
    for p in range(1,101):
        print(p)
        graph = Graph(100)


class Graph(dict):

    def __init__(self, size):
        for i in range(1, size+1):
            self.add_vertex(str(i))

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v, w = e
        self[v][w] = e
        self[w][v] = e

class Vertex(object):
    def __init__(self, val=None):
        self.val = val

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__


if __name__ == "__main__":
    main()
