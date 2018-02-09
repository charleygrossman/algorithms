import structs.linkedlist as ll


def main():
    print("Enter [q] to quit")
    while True:
        print("Deduplicate a linkedlist")
        i = input("Enter the values of the linkedlist separated by space: ").split()
        if i[0] == "q":
            break
        arr = [int(x) for x in i]
        l = ll.LinkedList()
        for e in arr:
            l.insert(e)

        print("Before de-duplicating: ")
        l.display()
        print("After de-duplicating: ")
        retval = dedup(l)
        retval.display()

def dedup(l):
    table = set()
    curr = l.head
    prev = None
    while curr:
        nextNode = curr.get_next()
        if curr.get_data() in table:
            curr.set_next(None)
            prev.set_next(nextNode)
        else:
            table.add(curr.get_data())
            prev = curr
        curr = nextNode
    return l

if __name__ == "__main__": main()
