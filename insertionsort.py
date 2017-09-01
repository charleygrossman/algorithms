def main():
    print("Enter [q] to quit")

    while True:
        i = input("Please enter a list of numbers, separated by spaces: ").split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        insertion_sort(arr)
        print(arr)

# Every move forward, we look to see how far back we can push that element
def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in reversed(range(1, i)):
            if arr[j] < arr[j-1]:
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp

if __name__ == "__main__":
    main()
