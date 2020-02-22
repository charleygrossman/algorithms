from typing import List
import sys
from utils.profile import timer_decorator


def main():
    data: List[int] = _input()
    n = len(data)
    # want is data sorted by the Python builtin sort.
    want: List[int] = timer_decorator(sorted)(data)

    got: List[int] = mergesort(data)

    for i in range(n):
        if got[i] != want[i]:
            print('fail')
            return
    print('pass')


@timer_decorator
def mergesort(data: List[int]) -> List[int]:
    return _mergesort(data)


def _mergesort(data: List[int]) -> List[int]:
    """
    _mergesort is a recursive mergesort implementation
    with a running time much worse than O(nlg(n)).

    :param data: The list of integers to sort.
    :return: A sorted list from data.
    """
    n = len(data)
    if n < 2:
        return data

    k = n // 2
    a = _mergesort(data[:k])
    b = _mergesort(data[k:])
    return _merge(a, b)


def _merge(a, b: List[int]) ->  List[int]:
    """
    _merge populates and returns an auxiliary
    array of the elements from a and b in a
    stable, sorted order.

    :param a: A list of integers to sort.
    :param b: A list of integers to sort.
    :return: A sorted list from a and b.
    """
    m, n = len(a), len(b)
    aux = [0] * (m + n)
    i, j, k = 0, 0, 0

    while i < m and j < n:
        if a[i] <= b[j]:
            aux[k] = a[i]
            i += 1
        else:
            aux[k] = b[j]
            j += 1
        k += 1

    if i < m and not j < n:
        while i < m:
            aux[k] = a[i]
            i, k = i+1, k+1
    else:
        while j < n:
            aux[k] = b[j]
            j, k = j+1, k+1

    return aux


def _input():
    filepath = sys.argv[1]

    with open(filepath) as file:
        data = []
        for line in file.readlines()[1:]:
            data.append(int(line.strip()))

        return data


if __name__ == '__main__':
    main()