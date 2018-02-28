import re
import random as rand

best_cut = 0

def main():
    print("Compute the minimum cut of a given graph")
    G = {}
    with open('min_cut_test.txt') as f:
        for line in f:
            line = line.rstrip()
            tmp = re.split(r"[\D']+", line)
            row = [int(x) for x in tmp]
            G[row[0]] = row[1:]
    test_min_cut(G, 250)
    global best_cut
    print(best_cut)

def test_min_cut(G, N):
    global best_cut
    for i in range(N):
        new_cut = compute_min_cut(G)
        if new_cut < best_cut:
            best_cut = new_cut

def compute_min_cut(G):
    while len(G) > 2:
        # Choose edge unif at random
        e = choose_edge(G)
        # Contract e.u, e.v into a single vertex, and remove self-loops
        contract(G, e)

    # return cut represented by final 2 (number of edges between them)

def choose_edge(G):
    while True:
        u = rand.randint(1, 200)
        try:
            v = rand.randrange(len(G[u]))
            return (u, G[u][v])
        except:
            KeyError

def contract(G, e):
    v, w = e
    G[v].remove(w)
    G[w].remove(v)
    
    # Remove self-loops
    if v in G[v]: G[v].remove(v)
    if w in G[w]: G[w].remove(w)


if __name__ == "__main__": main()
