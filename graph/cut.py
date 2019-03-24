# Compute the minimum cut of a given graph


import sys
import re
import copy
import random as rand


min_cut = sys.maxsize


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        data = {}
        n = 0

        for line in f.readlines():
            n += 1
            row = [int(x) for x in re.split(r"[\D']+", line.rstrip())]
            data[row[0]] = row[1:]

        return data, n


def main():
    G_prime, n = _input()

    # Compute nlogn min-cuts and output the lowest
    for i in range(n):
        G = copy.deepcopy(G_prime)
        candidate(G)

    global min_cut
    print(min_cut)


def candidate(G):
    global min_cut

    new_cut = compute_min_cut(G)
    if new_cut < min_cut:
        min_cut = new_cut


def compute_min_cut(G):
    while len(G) > 2:
        e = choose_edge(G)
        contract(G, e)
    return min_cut_size(G)


def choose_edge(G):
    while True:
        keys = list(G.keys())
        u = keys[rand.randrange(len(keys))]
        u_vals = G[u]
        v = u_vals[rand.randrange(len(u_vals))]
        if v in keys and u != v: return (u, v)


def contract(G, e):
    v, w = e
    # Remove contracted edge
    G[v].remove(w)
    G[w].remove(v)
    # Connect all edges incident upon w to v
    G[v] += G[w]
    for val in G[w]:
        if val in G: G[val].append(v)
    # Delete the actual w node, since it is now merged with v
    if v != w: del G[w]
    # Remove self-loops
    if v in G[v]: G[v].remove(v)


def min_cut_size(G):
    count = 0
    G_keys = list(G.keys())
    node_a = G_keys[0]
    node_b = G_keys[1]
    # Compute number of crossing edges between the last 2 nodes
    for e in G[node_b]:
        if e == node_a: count += 1
    return count


if __name__ == "__main__":
    main()

