def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a list of numbers, separated by spaces: ").split(" ")
        if i[0] == "q": break

        arr = [int(x) for x in i]
        quick_sort(arr, 0, len(arr)-1)
        print(arr)

def quick_sort(arr, lo, hi):
    if lo >= hi: return

    p = partition(arr, lo, hi)
    quick_sort(arr, lo, p-1)
    quick_sort(arr, p+1, hi)

# i := separates <p and >p
# j := separates seen from unseen
# pivot is arr[hi]
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo-1

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
    tmp = arr[i+1]
    arr[i+1] = arr[hi]
    arr[hi] = tmp
    return i + 1

if __name__ == "__main__":
    main()
