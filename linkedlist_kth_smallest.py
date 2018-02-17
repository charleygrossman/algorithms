import structs.linkedlist as ll

def main():
    print("Enter [q] to quit")
    print("Return the kth last item of a linkedlist")
    L = ll.LinkedList()
    vals = [int(x) for x in input("Enter the values of the list, separated by space: ").split(" ")]
    for val in vals:
        # TODO: ll.LinkedList creates a list reverse of insert!
        L.insert(val)
    L.display()
    while True:
        k = int(input("Enter the k value (0 for the largest item): "))
        print(kth_to_last(L, k))

# NOTE: You're popping, so more than one call will cause issues
def kth_to_last(L, k):
    if L.head is None or k < 0: return None
    cnt = 0
    S = []
    curr = L.head
    while curr:
        S.append(curr)
        curr = curr.get_next()
    if cnt == k: return S.pop().get_data()
    while cnt < k:
        tmp = S.pop().get_data()
        cnt += 1
        if cnt == k: return tmp
    return None


if __name__ == "__main__": main()
