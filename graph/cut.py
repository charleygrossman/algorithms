import re
import random as rand
import sys
import copy
import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

best_cut = sys.maxsize


def main():
    print("Compute the minimum cut of a given graph")
    # Create a master graph from the list
    G_prime = {}
    with open(os.path.join(BASE_DIR, 'test/cut.txt')) as f:
        for line in f:
            line = line.rstrip()
            tmp = re.split(r"[\D']+", line)
            row = [int(x) for x in tmp]
            G_prime[row[0]] = row[1:]

    # Run roughly nlogn (where n is number of nodes) min-cuts, taking the best
    for i in range(225):
        print("In test #{}".format(i))
        G = copy.deepcopy(G_prime)
        test_min_cut(G)
    global best_cut
    print(best_cut)


def test_min_cut(G):
    global best_cut
    new_cut = compute_min_cut(G)
    if new_cut < best_cut: best_cut = new_cut


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


if __name__ == "__main__": main()
