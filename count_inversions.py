def main():
    print("Enter [q] to quit")
    while True:
        print("Count the number of inversions in a given array")
        i = input("Enter a list of numbers, separated by spaces: ").split(" ")
        if i[0] == "q": break
        A = [int(x) for x in i]
        print(count_inversions(A))

def count_inversions(A):
    n = len(A)
    if n < 2: return 0
    # x and y are 2-tuples of type (list, integer)
    x = sort_count(A[:n//2], 0)
    y = sort_count(A[n//2:], 0)
    z = count_splits(A, x[0], y[0])
    return x[1] + y[1] + z

def sort_count(A, cnt):
    n = len(A)
    if n < 2: return (A, cnt)
    a = A[:n//2]
    b = A[n//2:]
    sort_count(a, cnt)
    sort_count(b, cnt)
    cnt += merge(A, a, b)
    return (A, cnt)

def count_splits(A, a,b):
    return merge(A, a, b)

def merge(A, a, b):
    i = j = cnt = 0
    while i + j < len(A):
        # b is exhausted or it's not and a element is less than b
        if j == len(b) or (i < len(a) and a[i] < b[j]):
            A[i+j] = a[i]
            i += 1
        # a is exhausted or it's not and b element is less than a
        else:
            A[i+j] = b[j]
            j+= 1
            cnt += len(a) - i
    return cnt

if __name__ == "__main__":
    main()
