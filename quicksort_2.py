# cnt = 0

def main():
    A = [1, 6, 2, 4, 3, 0, 9, 7, 8]
    # with open('quicksort_test.txt') as f:
    #     A = []
    #     for line in f:
    #         A.append([int(x) for x in line.split()])
    quicksort(A, "first")
    print(A)
        # global cnt
        # print(cnt)
        # cnt = 0

def quicksort(A, mode):
    if len(A) <= 1: return
    p = choose_pivot(A, mode)
    A_part = partition(A, p)
    quicksort(A_part[:A_part.index(p)], mode)
    quicksort(A_part[A_part.index(p)+1:], mode)

def partition(A, p):
    hi = len(A)
    i = 0
    for j in range(i, hi):
        # global cnt
        # cnt += 1
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
        p, A[i-1] = A[i-1], p
    return A

def choose_pivot(A, mode):
    if mode == "first":
        return A[0]
    elif mode == "last":
        return A[len(A) - 1]
    elif mode == "median":
        tmp = sorted(A[0], A[len(A)//2], A[len(A)-1])
        return tmp[1]
    else:
        raise ValueError("Wrong mode")

if __name__ == "__main__": main()
