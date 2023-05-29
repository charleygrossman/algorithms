from typing import *


def main():
    graph = {
        2: [],
        3: [8, 10],
        5: [11],
        7: [8, 11],
        8: [9],
        9: [10],
        10: [3],
        11: [2, 9, 10]
    }
    result = "not a DAG" if cycle_detection(graph) else "you like DAGs?"
    print(result)


def cycle_detection(graph: Dict[int, List[int]]) -> bool:
    seen = set()
    for v in graph:
        if v in seen:
            continue
        source = v
        s = [source]
        while s:
            v = s.pop()
            seen.add(v)
            for u in graph[v]:
                if u == source:
                    return True
                if u not in seen:
                    s.append(u)
    return False            


if __name__ == "__main__":
    main()