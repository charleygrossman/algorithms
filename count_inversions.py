full_cnt = 0

def main():
    print("Enter [q] to quit")
    print("Count the number of inversions in a given array")
    with open('count_inversions_test.txt') as f:
        A = []
        for line in f:
            A.append([int(x) for x in line.split()])
        count_inversions(A)
        global full_cnt
        print(full_cnt)
        full_cnt = 0

def count_inversions(A):
    n = len(A)
    if n < 2: return A
    # x and y are 2-tuples of type (list, integer)
    x = sort_count(A[:n//2])
    y = sort_count(A[n//2:])
    count_splits(A, x, y)


# TODO: Fix sorting and count problem
def sort_count(A):
    n = len(A)
    if n < 2: return(A)
    a = A[:n//2]
    b = A[n//2:]
    sort_count(a)
    sort_count(b)
    merge(A, a, b)
    # TODO: Probably shouldn't return here
    return (A)

def count_splits(A, a,b):
    merge(A, a, b)

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
            global full_cnt
            full_cnt += len(a) - i
    # return cnt

if __name__ == "__main__":
    main()
