import structs.linkedlist as ll


def main():
    print("Enter [q] to quit")
    while True:
        print("Add two numbers using linkedlists")
        i = input("Enter the two numbers to add, separated by space: ").split()
        if i[0] == "q":
            break
        val1 = [int(x) for x in str(i[0])]
        val2 = [int(x) for x in str(i[1])]
        a = ll.LinkedList()
        b = ll.LinkedList()
        for e in val1:
            a.insert(e)
        for e in val2:
            b.insert(e)

        retval = add_ll(a,b)
        retval.display()


def add_ll(a,b):
    acurr = a.head
    bcurr = b.head
    c = ll.LinkedList()
    co = None

    while acurr and bcurr:
        val = acurr.get_data() + bcurr.get_data()
        if val > 9:
            if co is None:
                co = 1
            c.insert(val%10)
        else:
            c.insert(val)
        acurr = acurr.get_next()
        bcurr = bcurr.get_next()

    if co: c.insert(co)

    if acurr and not bcurr:
        while acurr:
            c.insert(acurr.get_data())
            acurr = acurr.get_next()

    elif bcurr and not acurr:
        while bcurr:
            c.insert(bcurr.get_data())
            bcurr = bcurr.get_next()
    else:
        return c


if __name__ == "__main__": main()
