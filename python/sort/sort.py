from typing import *
import copy
import heapq


def main():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0]
    want = [0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print("insertion sort:")
    print ("pass" if insertion_sort(data) == want else "fail")
    print("selection sort:")
    print ("pass" if selection_sort(data) == want else "fail")
    print("heapsort:")
    print ("pass" if heapsort(data) == want else "fail")
    print("mergesort:")
    print ("pass" if mergesort(data) == want else "fail")
    print("count sort:")
    print ("pass" if count_sort(data, 10) == want else "fail")


def insertion_sort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    for i in range(1, len(d)):
        j = i
        while j > 0 and d[j] < d[j-1]:
            d[j], d[j-1] = d[j-1], d[j]
            j -= 1
    return d

def selection_sort(data: List[int]) -> List[int]:
    d = copy.copy(data)
    for i in range(len(d)):
        min_i = i
        for j in range(i+1, len(d)):
            if d[j] < d[min_i]:
                min_i = j
        d[min_i], d[i] = d[i], d[min_i]
    return d

def heapsort(data: List[int]) -> List[int]:
    l = copy.copy(data)
    result = []
    heapq.heapify(l)
    while l:
        result.append(heapq.heappop(l))
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

def count_sort(data: List[int], radix: int) -> List[int]:
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