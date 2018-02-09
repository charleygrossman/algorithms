import structs.linkedlist as ll


def main():
    print("Enter [q] to quit")
    while True:
        print("Partition values in a linkedlist by their comparative value to x")
        i = input("Enter the values of the linkedlist separated by space: ").split()
        if i[0] == "q":
            break
        arr = [int(x) for x in i]
        l = ll.LinkedList()
        for e in arr:
            l.insert(e)

        i = int(input("Now, enter a pivot value to sort around: "))
        if l.search(i) is False:
            print("Value not in list")
        else:
            newLL = partition(l, i)
            newLL.display()


def partition(l, x):
    smaller = ll.LinkedList()
    larger = ll.LinkedList()

    curr = l.head
    while curr:
        newNode = curr.get_next()
        curr.set_next(None)
        if curr.get_data() < x:
            if smaller.head is None:
                smaller.head = ll.Node(curr.get_data())
            else:
                n = ll.Node(curr.get_data())
                n.set_next(smaller.head)
                smaller.head = n
        if curr.get_data() > x:
            if larger.head is None:
                larger.head = ll.Node(curr.get_data())
            else:
                n = ll.Node(curr.get_data())
                n.set_next(larger.head)
                larger.head = n

        curr = newNode

    curr = smaller.head
    prev = None
    while curr:
        prev = curr
        curr = curr.get_next()
    prev.set_next(ll.Node(x))
    tmp = prev.get_next()
    tmp.set_next(larger.head)

    return smaller


if __name__ == "__main__": main()
