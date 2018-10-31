# Adjacency list representation
# Inherits from dictionary, has 2-tuple graph edge values
class Graph(dict):

    # nodes: list , edges: list of tuples
    def __init__(self, nodes, edges, directed=True, node_info=None):
        self.nodes = nodes
        self.edges = edges
        self.directed = directed
        for v in nodes:
            self[v] = {}
        for e in edges:
            self.add_edge(e)
        # If a graph has already been constructed before,
        # hold onto all of the node objects and their attributes.
        # Otherwise, construct new node objects
        if node_info:
            self.node_info = node_info
        else:
            self.node_info = {}
            for v in nodes:
                self.node_info[v] = Node(v)

    def add_node(self, v):
        self[v] = {}
        self.node_info[v] = Node(v)

    def add_edge(self, e):
        v, w = e
        if self.directed:
            self[v][w] = e
        else:
            self[v][w] = e
            self[w][v] = e

    def has_edge(self, e):
        v, w = e
        if v in self and w in self[v] and self[v][w] == e:
            return True
        return False

    def reversed(self):
        edges_rev = [e[::-1] for e in self.edges]
        return Graph(self.nodes, edges_rev, self.directed, self.node_info)

    def __str__(self):
        retval = []
        for k, v in self.items():
            retval.append("{} => {}\n".format(str(k), str(v)))
        return "".join(retval)

    def __repr__(self):
        return "<graph representation>"


# Stored as key in Graph's node_info dictionary attribute
class Node(object):

    def __init__(self, value, visited=False, pre=None, post=None, dist=None, scc=None):
        self.value = value
        self.visited = visited
        self.pre = pre
        self.post = post
        self.dist = dist
        self.scc = scc

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return(hash(str(self.val)))

    def __str__(self):
        return str(val)

    def __repr__(self):
        return "<graph node representation>"
