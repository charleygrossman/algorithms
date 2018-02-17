# cnt = 0

def main():
    print("Enter [q] to quit")
    A = [1, 6, 2, 4, 3, 0, 9, 7, 2, 8]
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
    partition(A, p)
    quicksort(A[:A.index(p)], mode)
    quicksort(A[A.index(p)+1:], mode)

def partition(A, p):
    hi = len(A)
    i = 1
    for j in range(1, hi):
        # global cnt
        # cnt += 1
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[A.index(p)], A[i-1] = A[i-1], A[A.index(p)]

def choose_pivot(A, mode):
    if mode == "first": return A[0]
    elif mode == "last": return A[len(A) - 1]
    elif mode == "median": return sorted(A[0], A[len(A)//2], A[len(A)-1])[1]
    else: raise ValueError("Wrong mode")

if __name__ == "__main__": main()
