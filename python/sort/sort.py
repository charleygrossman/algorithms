from typing import *
import copy
import heapq


def main():
    l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 0]
    expected = [0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print("========")
    print("insertion sort:")
    print ("pass" if insertion_sort(l) == expected else "fail")
    print("========")
    print("selection sort:")
    print ("pass" if selection_sort(l) == expected else "fail")
    print("========")
    print("heapsort:")
    print ("pass" if heapsort(l) == expected else "fail")
    print("========")
    print("mergesort:")
    print ("pass" if mergesort(l) == expected else "fail")
    print("========")
    print("count sort:")
    print ("pass" if count_sort(l) == expected else "fail")


def insertion_sort(lst: List[int]) -> List[int]:
    l = copy.copy(lst)
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l

def selection_sort(lst: List[int]) -> List[int]:
    l = copy.copy(lst)
    for i in range(len(l)):
        min_i = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_i]:
                min_i = j
        l[min_i], l[i] = l[i], l[min_i]
    return l

def heapsort(lst: List[int]) -> List[int]:
    l = copy.copy(lst)
    result = []
    heapq.heapify(l)
    while l:
        result.append(heapq.heappop(l))
    return result

def mergesort(lst: List[int]) -> List[int]:
    l = copy.copy(lst)
    n = len(l)
    if n < 2:
        return l
    k = n // 2
    a = mergesort(l[:k])
    b = mergesort(l[k:])
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

def count_sort(lst: List[int]) -> List[int]:
    l = copy.copy(lst)
    radix = 10
    count = [0] * (radix + 1)
    for v in l:
        count[v+1] += 1
    for i in range(len(count)-1):
        count[i+1] += count[i]
    result = [None] * len(l)
    for v in l:
        result[count[v]] = v
        count[v] += 1
    return result


if __name__ == "__main__":
    main()