from typing import *
from collections import deque


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
    print(f"dfs: method=iterative, source=2: {dfs_iterative(graph, 2)}")
    print(f"dfs: method=recursive, source=2: {dfs_recursive(graph, 2)}")
    print(f"dfs: method=iterative, source=3: {dfs_iterative(graph, 3)}")
    print(f"dfs: method=recursive, source=3: {dfs_recursive(graph, 3)}")
    print(f"dfs: method=iterative, source=5: {dfs_iterative(graph, 5)}")
    print(f"dfs: method=recursive, source=5: {dfs_recursive(graph, 5)}")
    print(f"dfs: method=iterative, source=7: {dfs_iterative(graph, 7)}")
    print(f"dfs: method=recursive, source=7: {dfs_recursive(graph, 7)}")
    print("========")
    print(f"bfs: method=iterative, source=2: {bfs_iterative(graph, 2)}")
    print(f"bfs: method=iterative, source=3: {bfs_iterative(graph, 3)}")
    print(f"bfs: method=iterative, source=5: {bfs_iterative(graph, 5)}")
    print(f"bfs: method=iterative, source=7: {bfs_iterative(graph, 7)}")


def dfs_iterative(graph: Dict[int, List[int]], source:int) -> List[int]:
    result = []
    seen = set()
    s = [source]
    while s:
        v = s.pop()
        seen.add(v)
        result.append(v)
        for u in graph[v]:
            if u not in seen:
                s.append(u)
    return result

def dfs_recursive(graph: Dict[int, List[int]], source:int) -> List[int]:
    result = []
    _dfs_recursive(graph, source, set(), result)
    return result

def _dfs_recursive(graph: Dict[int, List[int]], node: int, seen: Set[int], result: List[int]):
    if node in seen:
        return
    seen.add(node)
    result.append(node)
    for u in graph[node]:
        if u not in seen:
            _dfs_recursive(graph, u, seen, result)

def bfs_iterative(graph: Dict[int, List[int]], source:int) -> List[int]:
    result = []
    seen = set([source])
    q = deque([source])
    while q:
        v = q.popleft()
        result.append(v)
        for u in graph[v]:
            if u not in seen:
                seen.add(u)
                q.append(u)
    return result


if __name__ == "__main__":
    main()