cnt = 0

def main():
    with open('quicksort_test.txt') as f:
        A = []
        for line in f:
            A.append([int(x) for x in line.split()])
        quicksort(A, 0, len(A)-1)
        print(A)
        print(cnt)

def quicksort(arr, lo, hi):
    if lo >= hi: return

    p = partition(arr, lo, hi)
    quicksort(arr, lo, p-1)
    quicksort(arr, p+1, hi)

# i := separates <p and >p
# j := separates seen from unseen
# pivot is arr[hi]
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo-1

    for j in range(lo, hi):
        global cnt
        cnt += 1
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[i+1]
    arr[i+1] = arr[hi]
    arr[hi] = tmp
    return i + 1

# def choose_pivot(A, mode):
#     if mode == "first": return A[0]
#     elif mode == "last": return A[len(A) - 1]
#     elif mode == "median": return sorted(A[0], A[len(A)//2], A[len(A)-1])[1]
#     else: raise ValueError("Wrong mode")

if __name__ == "__main__":
    main()
