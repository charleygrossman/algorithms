from typing import *


def main():
    graph = {
        2: [],
        3: [8, 10],
        5: [11],
        7: [8, 11],
        8: [9],
        9: [],
        10: [],
        11: [2, 9, 10]
    }
    print(f"kaaahn!: {topological_sort_kahn(graph)}")
    print(f"dfs: {topological_sort_dfs(graph)}")


def topological_sort_kahn(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    result = []
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for u in graph[v]:
            in_degree[u] += 1
    sources = [kv[0] for kv in in_degree.items() if kv[1] == 0]
    while sources:
        v = sources.pop()
        result.append(v)
        for u in graph[v]:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                sources.append(u)
    return result if len(result) == len(graph) else None

def topological_sort_dfs(graph: Dict[int, List[int]]) -> List[int]:
    visited, time = [], [0]
    seen = set()
    for v in graph:
        if v not in seen:
            _topological_sort_dfs(graph, v, seen, visited, time)
    visited.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in visited]    

def _topological_sort_dfs(g: Dict[int, List[int]], v: int, seen: Set[int], visited: List[Tuple[int, int]], time: List[int]):
    seen.add(v)
    for u in g[v]:
        if u not in seen:
            _topological_sort_dfs(g, u, seen, visited, time)
    visited.append((v, time[0]))
    time[0] += 1


if __name__ == "__main__":
    main()