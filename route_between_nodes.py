import structs.graph as graph

def main():
    print("Enter [q] to quit")
    print("Determine if there is a route between two nodes in a directed graph")
    while True:
        print("First, create a graph")
        graph_type = input("Is this graph directed (enter 'directed'), or undirected (enter 'undirected')?: ")
        vertices = input("Now, enter a list of vertices, separate by space: ").split(" ")
        edges = input("Finally, enter ordered pairs of edges, separated by space: ").split(" ")
        G = graph.Graph(vertices, edges, graph_type)



if __name__ == "__main__": main()
