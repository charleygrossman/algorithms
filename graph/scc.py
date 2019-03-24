import struct.graph as gph
import traceback
import sys
import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# For node finishing times and scc membership
global t, scc, scc_counts
t, scc = 0, 1
scc_counts = {}

def main():
    with open(os.path.join(BASE_DIR, 'test/scc.txt')) as file:
        try:
            nodes = set()
            edges = []
            for line in file.readlines():
                v, w = map(int, line.strip().split())
                nodes.add(v)
                nodes.add(w)
                edges.append((v,w))
            nodes = sorted(nodes)
            G = gph.Graph(nodes, edges, directed=True)
            G_rev = G.reversed()
            dfs_post_iter(G_rev)
            G = G_rev.reversed()
            dfs_scc_iter(G)
            print(five_largest(G))


        except Exception as e:
            print(traceback.format_exception(*sys.exc_info()))
            raise


def dfs_post_iter(G):
    global t
    for v in G:
        G.node_info[v].visited = False
    for v in G:
        if G.node_info[v].visited == False:
            stk = [v]
            while stk:
                v = stk.pop()
                G.node_info[v].visited = True
                # print("dfs on " + str(v))
                for w in G[v]:
                    if G.node_info[w].visited == False:
                        stk.append(w)
                t += 1
                G.node_info[v].post = t


def dfs_scc_iter(G):
    global scc, scc_counts
    for v in G:
        G.node_info[v].visited = False
    for v in post_sort(G):
        if G.node_info[v].visited == False:
            stk = [v]
            while stk:
                v = stk.pop()
                if scc not in scc_counts:
                    scc_counts[scc] = 1
                else:
                    scc_counts[scc] += 1
                G.node_info[v].scc = scc
                G.node_info[v].visited = True
                # print("dfs on " + str(v))
                for w in G[v]:
                    if G.node_info[w].visited == False:
                        stk.append(w)
            scc += 1


def dfs_post(G):
    for v in G:
        G.node_info[v].visited = False
    for v in G:
        if G.node_info[v].visited == False:
            _dfs_post(G, v)

def _dfs_post(G, v):
    # print("dfs on " + str(v))
    global t
    G.node_info[v].visited = True
    for w in G[v]:
        if G.node_info[w].visited == False:
            _dfs_post(G, w)
    t += 1
    G.node_info[v].post = t


def dfs_scc(G):
    global scc, scc_counts
    for v in G:
        G.node_info[v].visited = False
    # dfs by descending order of node post-visit
    for v in post_sort(G):
        if G.node_info[v].visited == False:
            _dfs_scc(G, v, scc)
            scc += 1

def _dfs_scc(G, v, scc):
    global scc_counts
    if scc not in scc_counts:
        scc_counts[scc] = 1
    else:
        scc_counts[scc] += 1
    G.node_info[v].visited = True
    G.node_info[v].scc = scc
    for w in G[v]:
        if G.node_info[w].visited == False:
            _dfs_scc(G, w, scc)


# Sort and return graph's keys by its descending order node_info.post
def post_sort(G):
    desc_post = sorted(list(G.node_info.values()), key=lambda node: node.post, reverse=True)
    return [n.value for n in desc_post]


def five_largest(G):
    scc = [0 for i in range(1, 341510)]
    for value, node in G.node_info.items():
        scc[node.scc] += 1
    return sorted(scc, reverse=True)[:5]


if __name__ == '__main__':
    main()
