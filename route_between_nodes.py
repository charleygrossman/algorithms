import re
import structs.graph as graph

def main():
    print("Enter [q] to quit")
    print("Determine if there is a route between two nodes in a directed graph")
    # while True:
    print("First, create a graph")
    graph_type = input("Is this graph directed (enter 1), or undirected (enter 2)?: ")
    vertices_tmp = input("Now, enter a list of vertices, separate by space: ").split(" ")
    vertices = [int(x) for x in vertices_tmp]
    edges_tmp = input("Finally, enter ordered pairs of edges (e.g. '(1,2)' with no spaces), separated by space: ").split(" ")
    edges = []
    # Breaks user ordered-pair input into integer tuple
    for e in edges_tmp:
        e = re.sub('[()]', '', e)
        e = re.sub('[,]', ' ', e)
        edges.append((int(e[0]), int(e[2])))
    G = graph.Graph(vertices, edges, graph_type)


# 1. Call DFS(G) to compute finishing times for each vertex
# 2. Compute the reverse of G
# 3. Call DFS(G_reverse), but in the main loop of DFS, consider the vertices
# in order of decreasing finishing times
# 4. Output the vertices of each tree in the depth-first forest formed by 3.
# as a separate strongly connected component
def strongly_connected_components(self, G):


def dfs()

if __name__ == "__main__": main()
