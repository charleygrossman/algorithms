import re
import struct.graph as graph

def main():
    print("Enter [q] to quit")
    print("Determine if there is a route between two nodes in a directed graph")
    graph_type = input("Is this graph directed or undirected?: ")
    vertices = [int(x) for x in input("Enter a list of vertices, separate by space: ").split(" ")]
    tmp = input("Finally, enter ordered pairs of edges (e.g. '(1,2)' with no spaces), separated by space: ").split(" ")
    edges = []
    for e in tmp:
        e = re.sub('[()]', '', e)
        e = re.sub('[,]', ' ', e)
        edges.append((int(e[0]), int(e[2])))
    G = graph.Graph(vertices, edges, graph_type)
    strongly_connected_components(G)


# 1. Call DFS(G) to compute finishing times for each vertex
# 2. Reverse the edges of G
# 3. Call DFS(G_reverse), but in the main loop of DFS, consider the vertices
# in order of decreasing finishing times
# 4. Output the vertices of each tree in the depth-first forest formed by 3.
# as a separate strongly connected component


def strongly_connected_components(G):
    dfs(G)
    for v in G:
        print("Vertex {} discovered in step {}, and exhausted by step {}".format(v, G.vertex_info[v].time_disc, G.vertex_info[v].time_exhaust))

clock = None
def dfs(G, state="original"):
    global clock
    clock = 0
    for v in G:
        G.vertex_info[v].color = "white"
    for v in G:
        if G.vertex_info[v].color == "white":
            dfs_visit(G, v)

def dfs_visit(G, v):
    pre_visit(G, v)
    # TODO
    for w in G[v]:
        if G.vertex_info[w].color == "white": dfs_visit(G, w)
        post_visit(G, w)

def pre_visit(G, v):
    global clock
    G.vertex_info[v].time_disc = clock
    clock += 1
    G.vertex_info[v].color == "gray"

def post_visit(G, v):
    global clock
    G.vertex_info[v].time_exhaust == clock
    clock += 1
    G.vertex_info[v].color == "black"

if __name__ == "__main__": main()
