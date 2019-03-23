cnt = 0

def main():
    with open('quicksort_test.txt') as f:
        A = []
        for line in f:
            A.append([int(x) for x in line.split()])
    quicksort(A, 0, len(A)-1)
    print(A)
    global cnt
    print(cnt)
    cnt = 0

def quicksort(A, l, r):
    if l >= r: return
    p = partition(A, l, r)
    quicksort(A, l, p-1)
    quicksort(A, p+1, r)

# TODO all start at l+1
def partition(A, l, r):
    tmp = choose_pivot(A, l, r, "median")
    A[l], A[tmp] = A[tmp], A[l]
    p = A[l]
    i = l+1
    global cnt
    cnt += r-l
    for j in range(l+1, r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1


def choose_pivot(A, l, r, mode):
    if mode == "first": return l
    elif mode == "last": return r
    elif mode == "median":
        tmp = sorted([A[l], A[l + ((r-l)//2)], A[r]])
        return A.index(tmp[1])
    else: raise ValueError("Wrong mode")

if __name__ == "__main__": main()
