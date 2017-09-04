# NOTE: WIP

def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a list of numbers, separated by spaces: ")
            .split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        global count
        count = 0
        merge_sort(arr)
        print(count)

def merge_sort(arr):
    n = len(arr)
    if n < 2: return

    a = arr[:n//2]
    b = arr[n//2:]

    merge_sort(a)
    merge_sort(b)
    merge(arr, a, b)
    # i = j = 0
    # while j < len(b):
    #     for i in range(len(a)):
    #         if a[i] > b[j]:
    #             global count
    #             count += (len(a) - i)
    #             break
    #     # After comparing first elements, what's next?

def merge(arr, a, b):
    i = j = 0
    while i + j < len(arr):
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            arr[i+j] = a[i]
            i += 1
        else:
            global count
            count += 1
            arr[i+j] = b[j]
            j+= 1

if __name__ == "__main__":
    main()
