import re
import random as rand


best_cut = 0

def main():
    print("Compute the minimum cut of a given graph")
    G_prime = {}
    with open('min_cut_test.txt') as f:
        for line in f:
            line = line.rstrip()
            tmp = re.split(r"[\D']+", line)
            row = [int(x) for x in tmp]
            G_prime[row[0]] = row[1:]
    for i in range(1):
        print("In test #{}".format(i))
        G = G_prime.copy()
        test_min_cut(G)
    global best_cut
    print(best_cut)

def test_min_cut(G):
    global best_cut
    new_cut = compute_min_cut(G)
    print(new_cut)
    if new_cut < best_cut: best_cut = new_cut

def compute_min_cut(G):
    while len(G) > 2:
        e = choose_edge(G)
        contract(G, e)
    return min_cut_size(G)

# TODO: Fails more as graph size decreases
def choose_edge(G):
    print("Graph size: {}".format(len(G)))
    while True:
        u = rand.randint(1, 200)
        try:
            v = rand.randrange(len(G[u]))
            return (u, G[u][v])
        except: continue

def contract(G, e):
    v, w = e
    G[v].remove(w)
    if w in G:
        if v in G[w]: G[w].remove(v)
        G[v] += G[w]
        for val in G[w]:
            if val in G: G[val].append(v)
        if v != w: del G[w]
    if v in G[v]: G[v].remove(v)

def min_cut_size(G):
    count = 0
    G_iter = G.iterkeys()
    node_a = G_iter.next()
    node_b = G_iter.next()
    for e in G[node_a]:
        if e == node_b: count += 1
    return count


if __name__ == "__main__": main()
