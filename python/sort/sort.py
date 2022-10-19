from typing import *
import copy
import heapq


def main():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0]
    want = [0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    got = selection_sort(data)
    assert want == got, f"selection sort: want={want} got={got}"
    got = insertion_sort(data)
    assert want == got, f"insertion sort: want={want} got={got}"
    got = heapsort(data)
    assert want == got, f"heapsort: want={want} got={got}"
    got = mergesort(data)
    assert want == got, f"mergesort: want={want} got={got}"
    got = quicksort(data)
    assert want == got, f"quicksort: want={want} got={got}"
    got = counting_sort(data, 10)
    assert want == got, f"counting sort: want={want} got={got}"


def selection_sort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    for i in range(len(d)):
        min_i = i
        for j in range(i+1, len(d)):
            if d[j] < d[min_i]:
                min_i = j
        d[min_i], d[i] = d[i], d[min_i]
    return d

def insertion_sort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    for i in range(1, len(d)):
        j = i
        while j > 0 and d[j] < d[j-1]:
            d[j], d[j-1] = d[j-1], d[j]
            j -= 1
    return d

def heapsort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    result = []
    heapq.heapify(d)
    while d:
        result.append(heapq.heappop(d))
    return result

def mergesort(data: List[int]) -> List[int]:
    n = len(data)
    if n < 2:
        return data
    k = n // 2
    a = mergesort(data[:k])
    b = mergesort(data[k:])
    return _merge(a, b)

def _merge(a, b: List[int]) -> List[int]:
    n = len(a) + len(b)
    aux = [0] * n
    i, j, k = 0, 0, 0
    while k < n and i < len(a) and j < len(b):
        if a[i] <= b[j]:
            aux[k] = a[i]
            i += 1
        else:
            aux[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        aux[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        aux[k] = b[j]
        j += 1
        k += 1
    return aux

def quicksort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    _quicksort(d, 0, len(d)-1)
    return d

def _quicksort(d: List[int], l: int, h: int):
    if l >= h or l < 0:
        return
    p = _partition(d, l, h)
    _quicksort(d, l, p-1)
    _quicksort(d, p+1, h)

def _partition(d: List[int], l: int, h: int) -> int:
    pivot, i = d[h], l-1
    for j in range(l, h):
        if d[j] <= pivot:
            i += 1
            d[j], d[i] = d[i], d[j]
    i += 1
    d[h], d[i] = d[i], d[h]
    return i

def counting_sort(data: List[int], radix: int) -> List[int]:
    count = [0] * (radix + 1)
    for v in data:
        count[v+1] += 1
    for i in range(len(count)-1):
        count[i+1] += count[i]
    result = [None] * len(data)
    for v in data:
        result[count[v]] = v
        count[v] += 1
    return result


if __name__ == "__main__":
    main()