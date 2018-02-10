import re
import structs.graph as graph

def main():
    print("Enter [q] to quit")
    print("Determine if there is a route between two nodes in a directed graph")
    # while True:
    print("First, create a graph")
    graph_type = input("Is this graph directed (enter 'directed'), or undirected (enter 'undirected')?: ")
    vertices_tmp = input("Now, enter a list of vertices, separate by space: ").split(" ")
    vertices = [int(x) for x in vertices_tmp]
    edges_tmp = input("Finally, enter ordered pairs of edges (e.g. '(vertexA,vertexB)' with no spaces), separated by space: ").split(" ")
    edges = []
    for e in edges_tmp:
        e = re.sub('[()]', '', e)
        e = re.sub('[,]', ' ', e)
        edges.append((int(e[0]), int(e[2])))
    G = graph.Graph(vertices, edges, graph_type)

    # 1. Split the graph into strongly connected components (using dfs and graph reversal)
    # 2. Determine if the two vertices are in the same component


if __name__ == "__main__": main()
