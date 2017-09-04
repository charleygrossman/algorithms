def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a list of numbers, separated by spaces: ")
            .split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        merge_sort(arr)
        print(arr)

def merge_sort(arr):
    n = len(arr)
    if n < 2: return

    a = arr[:n//2]
    b = arr[n//2:]

    merge_sort(a)
    merge_sort(b)
    merge(arr, a, b)

def merge(arr, a, b):
    i = j = 0
    while i + j < len(arr):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            arr[i+j] = a[i]
            i += 1
        else:
            arr[i+j] = b[j]
            j+= 1

if __name__ == "__main__":
    main()
