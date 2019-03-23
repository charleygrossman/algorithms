# Compute the largest value of k such that there is a k-clustering with spacing at least 3
# (or any other valid spacing)
#
#
# Each line of the file represents a corresponding node in a graph labeled by line number,
# the data of each node being the bitstring of the line itself. The distance of
# two nodes is then the hamming distance between their bitstrings.
# Starting with all nodes as separate clusters, what is the maximum number of
# clusters k that can be had while ensuring the max spacing is 3? That is,
# every cluster should have nodes with hamming distance between 0 and 2 of each other.


import networkx as nx
from itertools import combinations


def main():
    try:
        with open('clustering_big.txt') as file:
            node_count, bit_count = map(int, file.readline().strip().split())
            data = dict_from_data(file)
    except:
        raise
    G = nx.Graph()
    G.add_nodes_from([i for i in range(1, node_count+1)])
    print(max_k_clustering(G, data, node_count, bit_count))


# Union all nodes of hamming distance less than 3, then return the number of clusters
def max_k_clustering(G, data, node_count, bit_count):
    dist_1_mask = [1 << i for i in range(bit_count)]
    dist_2_mask = []
    for c in combinations([i for i in range(bit_count)], 2):
        x = (1 << c[0]) ^ (1 << c[1])
        dist_2_mask.append(x)
    distances = set([0] + dist_1_mask + dist_2_mask)
    for dist in distances:
        for k in data:
            x = k ^ dist
            if x in data:
                for pair in combinations(data[k].union(data[x]), 2):
                    G.add_edge(pair[0], pair[1])
    return nx.number_connected_components(G)


def dict_from_data(file):
    data = {}
    node = 1
    for line in file.readlines():
        bits = int(''.join(line.strip().split()), 2)
        if bits not in data:
            data[bits] = {node}
        else:
            data[bits].add(node)
        node += 1
    return data


if __name__ == '__main__':
    main()
