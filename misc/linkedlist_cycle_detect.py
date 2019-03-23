# NOTE: This is broken not because of the algorithm, but because of the faulty
# linkedlist implementation

import struct.linkedlist as ll


def main():
    print("Enter [q] to quit")
    while True:
        print("Dedect if a linkedlist contains a cycle")
        i = input("Enter the values of the linkedlist separated by space: ").split(" ")
        if i[0] == "q":
            break
        arr = [int(x) for x in i]
        l = ll.LinkedList()
        for e in arr:
            l.insert(e)
        answer = is_cyclical(l)
        if answer == False: print("No cycle")
        else: print("Cylce detected at node {}".format(answer))

def is_cyclical(l):
    slow = l.head
    fast = l.head
    while fast and fast.get_next():
        slow = slow.get_next()
        fast = fast.get_next().get_next()
        if slow == fast: break
    if fast is None or fast.get_next() is None: return False
    slow = l.head
    while slow != fast:
        slow = slow.get_next()
        fast = fast.get_next()
    return fast.get_data()


if __name__ == "__main__": main()
