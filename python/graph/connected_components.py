from typing import *


def main():
    undirected_graph = {
        2: [11],
        3: [8, 10],
        5: [11],
        7: [8, 11],
        8: [3, 7, 9],
        9: [8, 11],
        10: [3, 11],
        11: [2, 5, 7, 9, 10],
        12: [13],
        13: [12],
        14: []
    }
    print(f"connected components (undirected): {connected_components(undirected_graph)}")


def connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    result = []
    seen = set()
    for source in graph:
        if source in seen:
            continue
        cc = []
        s = [source]
        while s:
            v = s.pop()
            seen.add(v)
            cc.append(v)
            for u in graph[v]:
                if u not in seen:
                    s.append(u)
        result.append(cc)
    return result


if __name__ == "__main__":
    main()