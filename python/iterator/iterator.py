from typing import *


def main():
    iter = CompositeIterator([
        Iterator(["a1", "a2"]),
        Iterator(["b1"]),
        Iterator(["c1", "c2", "c3", "c4"]),
    ])
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())
    print(iter.has_next())
    print(iter.next())


class Iterator:
    def __init__(self, iter: Sequence[Any]):
        self.iter = iter
        self.i = 0
        self.n = len(self.iter)
    
    def has_next(self) -> bool:
        return self.i < self.n

    def next(self) -> Any:
        if not self.has_next():
            return None
        result = self.iter[self.i]
        self.i += 1
        return result


class CompositeIterator:
    class IteratorNode:
        def __init__(self, iter: Iterator, prev=None, next=None):
            self.iter = iter
            self.prev = prev
            self.next = next

    def __init__(self, iters: Sequence[Iterator]):
        self.curr = None
        if len(iters) == 0:
            return
        self.curr = self.IteratorNode(iters[0])
        prev = self.curr
        for i in range(1, len(iters)):
            n = self.IteratorNode(iters[i], prev=prev)
            prev.next = n
            prev = n
        self.curr.prev = prev
        prev.next = self.curr

    def has_next(self) -> bool:
        return self.curr != None

    def next(self) -> Any:
        if not self.has_next():
            return None
        result, found, curr = None, False, self.curr
        while curr:
            n = curr.next
            if curr.iter.has_next():
                result = curr.iter.next()
                found = True
            if not curr.iter.has_next():
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr = n if curr != n else None
            else:
                curr = n
            if found:
                break
        self.curr = curr
        return result


if __name__ == "__main__":
    main()