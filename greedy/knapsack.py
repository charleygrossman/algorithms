# Find the optimal solution to the knapsack problem on a given set of values and weights


def main():
    with open('knapsack.txt') as file:
        W, n = map(int, file.readline().strip().split())
        # [(value, weight)]
        data = []
        for line in file.readlines():
            v, w = map(int, line.strip().split())
            data.append((v, w))
        print(knapsack(data, W, n))


def knapsack(data, W, n):
    A = [[0]*(W+1) for i in range(n)]
    for i in range(1, n):
        for x in range(W+1):
            value, weight = data[i]
            if weight > x:
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-weight] + value)
    return A[-1][-1]


if __name__ == '__main__':
    main()
