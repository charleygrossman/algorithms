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
    _quicksort is an in-place, deterministic, recursive quicksort
    implementation with a running time much worse than O(nlg(n)).

    :param data: The list of integers to sort.
    :param l: The first index of the list.
    :param h: The last index of the list.
    :return:
    """
    if l >= h:
        return

    p = _partition(data, l, h)
    _quicksort(data, l, p-1)
    _quicksort(data, p+1, h)


def _partition(data: List[int], l: int, h: int) -> int:
    """
    _partition chooses a pivot element p as the last element
    of the list and performs a linear scan, maintaining
    a boundary at position i of the elements less than
    the pivot, finally placing the pivot in the position
    of the list where all elements to its left are smaller,
    and all elements to its right are greater or equal.
    This final position is then returned.

    :param data: The list of integers to sort.
    :param l: The first index of the list.
    :param h: The last index of the list.
    :return: The position of the pivot in its relative-sorted order.
    """
    p = data[h]
    i = l

    for j in range(l, h):
        if p > data[j]:
            _swap(data, j, i)
            i += 1
    _swap(data, h, i)

    return i


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