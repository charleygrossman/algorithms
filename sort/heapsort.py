# Heapsort implementation.


import sys
from typing import List


def main():
    data = _input()
    want = sorted(data)
    heapsort(data)
    for i in range(len(data)):
        if data[i] != want[i]:
            print('fail')
            return
    print('pass')


def heapsort(data: List[int]):
    h = Minheap(data)
    for i in range(len(data)):
        data[i] = h.extract_min()

class Minheap(list):
    def __init__(self, data: List[int]):
        super().__init__()
        self.n = 0
        for i in range(len(data)):
            self.append(data[i])
            self.n += 1
            self._bubble_up(i)

    def __len__(self):
        return self.n

    def extract_min(self) -> int:
        x = self[0]
        self[0] = self[self.n-1]
        self.n -= 1
        self._bubble_down(0)

        return x

    def _parent_index(self, i: int) -> int:
        if i == 0:
            return -1
        return (i+1) // 2 - 1

    def _left_child_index(self, i: int) -> int:
        return 2 * (i+1) - 1

    def _bubble_up(self, i: int):
        j = self._parent_index(i)
        if j == -1:
            return
        if self[j] > self[i]:
            self._swap(i, j)
            return self._bubble_up(j)

    def _bubble_down(self, i: int):
        child_index = self._left_child_index(i)
        min_index = i
        for k in range(2):
            j = child_index + k
            if j < self.n and self[min_index] > self[j]:
                min_index = j
        if min_index != i:
            self._swap(i, min_index)
            return self._bubble_down(min_index)

    def _swap(self, i: int, j: int):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        data = []
        for line in f.readlines()[1:]:
            data.append(int(line.strip()))
        return data


if __name__ == '__main__':
    main()