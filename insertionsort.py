def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a list of numbers, separated by spaces: ")
            .split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        insertion_sort(arr)
        print(arr)

# Every move forward, we look to see how far back we can push that element
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in reversed(range(i)):
            if arr[j+1] < arr[j]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp

if __name__ == "__main__":
    main()
