import structs.searchtree as bst
from collections import deque

def main():
    print("Press [q] to quit")
    while True:
        print("Check if a binary tree is balanced")
        i = input("Enter integers to make a tree, separated by spaces: ").split(" ")
        if i[0] == "q":
            break
        vals = [int(x) for x in i]
        T = bst.BinarySearchTree()
        for val in vals:
            T.put(val, val)

        depths = leaf_depths(T)
        print("Depths: {}".format(depths))
        if (max(depths) - min(depths)) > 1:
            print("Not balanced")
        else:
            print("Balanced")

def leaf_depths(T):
    depths = set()
    root = T.root
    root.color == "gray"
    root.depth = 0
    q = deque()
    q.append(root)
    while q:
        u = q.popleft()
        l = None
        r = None
        if u.isLeaf():
            depths.add(u.depth)
        if u.hasLeftChild():
            l = u.leftChild
        if u.hasRightChild():
            r = u.rightChild
        if l:
            if l.color == "white":
                l.color = "gray"
                l.depth = u.depth+1
                q.append(l)
        if r:
            if r.color == "white":
                r.color = "gray"
                r.depth = u.depth+1
                q.append(l)
        u.color = "black"
    return depths


if __name__ == "__main__":
    main()
