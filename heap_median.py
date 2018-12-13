# An application of median maintenance with two heaps:
# Successively compute the median of a list from the first int to current one,
# incrementing current by 1 to the end. Sum these medians and mod 10^5


import sys
import os
from heapq import heappush, heappop, heapify


def main():
    arr = []
    with open('heap.txt') as file:
        for line in file.readlines():
            arr.append(int(line.strip()))
    medians = get_medians(arr)
    print(sum(medians) % (len(arr)))


# After every new iteration, the median from x_1 to x_i is the root of one of
# the heaps
def get_medians(arr):
    medians = []
    # lo is a maxheap; smaller numbers here
    # NOTE: Negate number before inserting into a minheap to make it a
    # maxheap. Remember to negate again before using it
    lo = []
    # hi is a minheap; larger numbers here
    hi = []
    for i in range(len(arr)):
        x = arr[i]
        heap_insert(x, lo, hi)
        if abs(len(lo) - len(hi)) > 1:
            heaps_balance(lo, hi)
        if i % 2 == 0:
            if len(lo) > len(hi):
                medians.append(-lo[0])
            else:
                medians.append(hi[0])
        else:
            medians.append(-lo[0])
    return medians


def heap_insert(x, lo, hi):
    if not lo and not hi:
        heappush(lo, -x)
        heapify(lo)
    elif lo and not hi:
        if x <= -lo[0]:
            heappush(lo, -x)
            heapify(lo)
        else:
            heappush(hi, x)
            heapify(hi)
    elif not lo and hi:
        if x >= hi[0]:
            heappush(hi, x)
            heapify(hi)
        else:
            heappush(lo, -x)
            heapify(lo)
    else:
        if x < -lo[0]:
            heappush(lo, -x)
            heapify(lo)
        elif x > hi[0]:
            heappush(hi, x)
            heapify(hi)
        else:
            if len(lo) <= len(hi):
                heappush(lo, -x)
                heapify(lo)
            else:
                heappush(hi, x)
                heapify(hi)


# If a heap has more than one element above another, rebalance the heaps to
# maintain the two-heap median invariant
def heaps_balance(lo, hi):
    lo_len = len(lo)
    hi_len = len(hi)
    if lo_len > hi_len:
        heappush(hi, -heappop(lo))
    else:
        heappush(lo, -heappop(hi))
    heapify(lo)
    heapify(hi)


if __name__ == '__main__':
    main()
