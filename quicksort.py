def main():
    print("Enter [q] to quit")

    while True:
        i = input("Please enter a list of numbers, separated by spaces: ").split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        #-1
        quick_sort(arr, 0, len(arr))
        print(arr)

def quick_sort(arr, lo, hi):
    if lo >= hi: return

    p = partition(arr, lo, hi)
    quick_sort(arr, lo, p-1)
    quick_sort(arr, p+1, hi)

# i := separates <p and >p
# j := separates seen from unseen
# Pivot is arr[hi]
def partition(arr, lo, hi):
    i = lo-1
    for j in range(lo, hi-1):
        if arr[j] <= arr[hi]:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    i += 1
    tmp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = tmp

    return i

if __name__ == "__main__":
    main()
