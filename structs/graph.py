# Graph interfaces Vertex, not the user
class Graph(dict):

    # vertices is a list, edges a list of tuples
    def __init__(self, vertices, edges, graph_type="directed"):
        for v in vertices:
            self.add_vertex(v)
        for e in edges:
            self.add_edge(e, graph_type)

    # TODO: Using a Vertex object as a dictionary key is not the way to go
    def add_vertex(self, val, color="white", time_disc=0, time_exhaust=0, dist=0):
        v = Vertex(val, color, time_disc, time_exhaust, dist)
        self[v] = {}

    def add_edge(self, e, graph_type):
        v, w = e
        if graph_type == "directed":
            self[v][w] = e
        elif graph_type == "undirected":
            self[v][w] = e
            self[w][v] = e
        else:
            raise ValueError("Create a graph with type parameter 'directed' or 'undirected'")

    # TODO: def __str__(self):

    def __repr__(self):
        return "<graph representation>"

    # TODO: Assumes legal vertices was entered
    def has_edge(self, e):
        v,w = e
        if self[v][w] == e: return True
        else: return False

    # Reverse(): create a copy, reverse it, and return it

class Vertex(object):

    def __init__(self, val, color, time_disc, time_exhaust, dist):
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
