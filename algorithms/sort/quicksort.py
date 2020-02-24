from typing import List
import sys
from utils.profile import timer_decorator


def main():
    data: List[int] = _input()
    n = len(data)
    # want is data sorted by the Python builtin sort.
    want: List[int] = timer_decorator(sorted)(data)

    quicksort(data)

    for i in range(n):
        if data[i] != want[i]:
            print('fail')
            return
    print('pass')


@timer_decorator
def quicksort(data: List[int]):
    _quicksort(data, 0, len(data)-1)


def _quicksort(data: List[int], l: int, h: int):
    """
    _quicksort is an in-place, recursive quicksort implementation
    with a running time much worse than O(nlg(n)).

    :param data: The list of integers to sort.
    :return:
    """
    if l >= h:
        return

    p = _partition(data, l, h)
    _quicksort(data, l, p-1)
    _quicksort(data, p+1, h)


def _partition(data: List[int], l: int, h: int) -> int:
    p = h
    j = l

    for i in range(l, h):
        if data[p] > data[i]:
            _swap(data, i, j)
            j += 1
    _swap(data, p, j)

    return j


def _swap(data: List[int], i: int, j: int):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def _input():
    filepath = sys.argv[1]

    with open(filepath) as file:
        data = []
        for line in file.readlines()[1:]:
            data.append(int(line.strip()))

        return data


if __name__ == '__main__':
    main()