# NOTE: This is not always returning a boolean value

def main():
    print("Press [q] to quit")

    while True:
        i = input("Please enter a list of numbers, separated by spaces, " +
                  "and end with the number you are searching for: ").split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        n = len(arr)
        o = binary_search(arr, arr[n-1], 0, n-1)
        print(o)

# Assumes the list is sorted
def binary_search(arr, e, lo, hi):
    if lo > hi: return false

    mid = lo + (hi - lo) // 2
    if e < arr[mid]:
        binary_search(arr, e, lo, mid-1)
    elif e > arr[mid]:
        binary_search(arr, e, mid+1, hi)
    else:
        return True

if __name__ == "__main__":
    main()
