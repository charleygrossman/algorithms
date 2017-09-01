def main():
    print("Press [q] to quit")

    while True:
        i = input("Enter a list of numbers separate by spaces: ").split()
        if i[0] == "q": break

        global count
        count = 0
        i = [int(x) for x in i]
        inversion_count(i)
        print(count)

def inversion_count(arr):
    n = len(arr)
    if n < 2: return

    a = arr[:n//2]
    b = arr[n//2:]

    inversion_count(a)
    inversion_count(b)
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
