from typing import *
from sys import maxsize
from bisect import bisect_right


def main():
    sequence = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    expected = [
        [0, 2, 6, 9, 11, 15],
        [0, 4, 6, 9, 11, 15],
        [0, 2, 6, 9, 13, 15],
        [0, 4, 6, 9, 13, 15]
    ]
    print(f"LIS length: {lis_optimal(sequence)}")


def lis_optimal(s: List[int]) -> int:
    l = [maxsize for _ in range(len(s)+1)]
    l[0] *= -1
    for i in range(len(s)):
        v = s[i]
        j = bisect_right(l, v)
        if l[j-1] < v and v < l[j]:
            l[j] = v
    result = 1
    for i in range(len(s), 0, -1):
        if l[i] < maxsize:
            result = i
            break
    return result

def lis_basic(s: List[int]) -> List[int]:
    l = [[s[i]] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i):
            if s[i] > s[j] and len(l[i]) < len(l[j]) + 1:
                l[i] = l[j] + [s[i]]
    l.sort(key=lambda x: len(x), reverse=True)
    return l[0]

def lis_basic_reconstructed(s: List[int]) -> List[int]:
    l = [0 for i in range(len(s)+1)]
    p = [None for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i):
            if s[i] > s[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
                p[i] = j
    return _reconstructed(s, l, p)

def _reconstructed(s: List[int], l: List[int], p: List[int]) -> List[int]:
    m, j = 0, None
    for i in range(len(s)):
        if l[i] > m:
            m = l[i]
            j = i
    result = []
    while j != None:
        result.append(s[j])
        j = p[j]
    result.reverse()
    return result


if __name__ == "__main__":
    main()