# Find the optimal solution to the knapsack problem on a given set of values and weights


import sys


def main():
    data, W, n = _input()
    solution = knapsack(data, W, n)

    print(solution)


def knapsack(data, W, n):
    A = [[0] * (W+1) for _ in range(n)]

    for i in range(1, n):
        for x in range(W+1):
            value, weight = data[i]
            if weight > x:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-weight] + value)

    return A[-1][-1]


def _input():
    filepath = sys.argv[1]

    with open(filepath) as f:
        W, n = map(int, f.readline().strip().split())
        data = []

        for line in f.readlines():
            v, w = map(int, line.strip().split())
            data.append((v, w))

        return data, W, n


if __name__ == '__main__':
    main()
