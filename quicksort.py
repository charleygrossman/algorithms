cnt = 0

def main():
    # with open('quicksort_test.txt') as f:
    #     A = []
    #     for line in f:
    #         A.append([int(x) for x in line.split()])
    #     quicksort(A, 0, len(A)-1)
    #     print(A)
    #     print(cnt)
    arr = [1, 6, 2, 4, 3, 0, 9, 7, 2, 8]
    quicksort(arr, 0, len(arr)-1)
    print(arr)

def quicksort(arr, lo, hi):
    if lo >= hi: return
    p = partition(arr, lo, hi)
    quicksort(arr, lo, p-1)
    quicksort(arr, p+1, hi)

# i := separates <p and >p
# j := separates seen from unseen
# pivot is arr[hi]
def partition(arr, lo, hi):
    # pivot = arr[hi]
    # i = lo-1
    # for j in range(lo, hi):
    #     global cnt
    #     cnt += 1
    #     if arr[j] <= pivot:
    #         i += 1
    #         arr[i], arr[j] = arr[j], arr[i]
    # arr[i+1], arr[hi] = arr[hi], arr[i+1]
    # return i + 1
    pivot = arr[lo]
    i = lo+1
    for j in range(lo+1, hi):
        global cnt
        cnt += 1
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i-1], arr[lo] = arr[lo], arr[i-1]
    return i-1

# def choose_pivot(A, mode):
#     if mode == "first": return A[0]
#     elif mode == "last": return A[len(A) - 1]
#     elif mode == "median": return sorted(A[0], A[len(A)//2], A[len(A)-1])[1]
#     else: raise ValueError("Wrong mode")

if __name__ == "__main__":
    main()
