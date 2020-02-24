from typing import List
import sys
from utils.profile import timer_decorator


def main():
    data: List[int] = _input()
    n = len(data)
    # want is data sorted by the Python builtin sort.
    want: List[int] = timer_decorator(sorted)(data)

    heapsort(data)

    for i in range(n):
        if data[i] != want[i]:
            print('fail')
            return
    print('pass')


@timer_decorator
def heapsort(data: List[int]):
    """
    heapsort is an in-place, recursive heapsort implementation
    with performance much worse than O(nlg(n)).

    :param data: The list of integers to sort.
    :return:
    """
    heap = Minheap(data)
    for i in range(len(data)):
        data[i] = heap.extract_min()


class Minheap(list):
    """
    Minheap is a list representation of a minheap
    that maintains the following invariants:
        - The first element is the minimum.
        - The parent of an element at position k
          is at the floor of k/2, if it exists.
        - The children of an element at position k
          are at positions 2k and 2k+1, if they exist.
        - The parent element is smaller than its children.

    The length of the heap does not change after initialization;
    extracting the minimum does not truncate the heap.
    """
    def __init__(self, data: List[int]):
        super().__init__()
        # self.n represents the length of the heap.
        self.n = 0
        # This is similar to the insert operation of a true heap.
        for i in range(len(data)):
            self.append(data[i])
            self.n += 1
            self._bubble_up(i)

    def __len__(self):
        return self.n

    def extract_min(self) -> int:
        """
        extract_min returns the minimum element of the heap,
        which is the first element, and overwrites the first
        element to the last one, bubbling-down the new first
        element until the heap invariants are satisfied.

        The length of the heap is decremented to simulate
        the returned element being deleted from the heap.

        :return: The minimum element of the heap.
        """
        minimum = self[0]

        self[0] = self[len(self)-1]
        self.n -= 1
        self._bubble_down(0)

        return minimum

    def _bubble_up(self, i: int):
        """
        _bubble_up recursively swaps the element at initial position
        i of the heap with its parent, until the invariant that the
        parent is smaller than its children is satisfied.

        :param i: The initial position of the element to bubble-up.
        :return:
        """
        j = self._parent_index(i)
        if j == -1:
            return

        if self[i] < self[j]:
            self._swap(i, j)
            self._bubble_up(j)

    def _bubble_down(self, i: int):
        """
        _bubble_down recursively swaps the element at initial
        position i of the heap with the smallest of its children,
        until the invariant that the parent is smaller than its
        children is satisfied.

        :param i: The initial position of the element to bubble-down.
        :return:
        """
        child_index = self._left_child_index(i)
        min_index = i

        for k in range(2):
            j = child_index + k
            if j < len(self) and self[j] < self[min_index]:
                min_index = j

        if min_index != i:
            self._swap(i, min_index)
            self._bubble_down(min_index)

    def _parent_index(self, i: int) -> int:
        return -1 if i == 0 else (i+1) // 2 - 1

    def _left_child_index(self, i: int) -> int:
        return 2 * (i+1) - 1

    def _swap(self, i: int, j: int):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp


def _input():
    filepath = sys.argv[1]

    with open(filepath) as file:
        data = []
        for line in file.readlines()[1:]:
            data.append(int(line.strip()))

        return data


if __name__ == '__main__':
    main()