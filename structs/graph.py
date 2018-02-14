class Graph(dict):

    # vertices is a list, edges a list of tuples
    def __init__(self, vertices, edges, graph_type="1"):
        self.vertices = vertices
        self.edges = edges
        self.graph_type = graph_type

        for v in vertices:
            self.add_vertex(v)
        for e in edges:
            self.add_edge(e, graph_type)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e, graph_type):
        v, w = e
        if graph_type == "1":
            self[v][w] = e
        elif graph_type == "2":
            self[v][w] = e
            self[w][v] = e
        else:
            raise ValueError("Create a graph with type parameter '1' or '2'")

    # Assumes legal vertices was entered
    def has_edge(self, e):
        v, w = e
        if self[v][w] == e: return True
        else: return False

    def reverse(self):
        edges_rev = [x[::-1] for x in self.edges]
        return Graph(self.vertices, edges_rev, self.graph_type)

    def __str__(self):
        retval = ""
        for k, v in self.items():
            retval += str(k) + " -> " + str(v) + "\n"
        return retval

    def __repr__(self):
        return "<graph representation>"


class Vertex(object):

    def __init__(self, val=None, color=None, time_disc=None, time_exhaust=None, dist=None):
        self.val = val
        self.color = color
        self.time_disc = time_disc
        self.time_exhaust = time_exhaust
        self.dist = dist

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return(hash(str(self.val)))

    def __str__(self):
        return "Vertex " + str(self.val) + "\n"

    def __repr__(self):
        return "<graph vertex representation>"
