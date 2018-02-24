# NOTE: This in_order function is a fantastic way to sort a bst

import structs.bst as bst

def main():
    print("Press [q] to quit")
    while True:
        print("Find the in-order successor (i.e. sorted-next) of a bst node: ")
        i = input("Enter integers to make a tree, separated by spaces: ").split(" ")
        N = int(input("Now, enter a node that's in the tree: "))
        if i[0] == "q":
            break
        vals = [int(x) for x in i]
        T = bst.BinarySearchTree()
        for val in vals:
            T.put(val, val)

        print(next_node(T, N))

def next_node(T, N):
    if T.length() < 2: return None
    arr_in_order = in_order(T)
    if N not in arr_in_order:
        return None
    else:
        try:
            return arr_in_order[arr_in_order.index(N)+1]
        except:
            print("N has no successor")

def in_order(T):
    arr = []
    _in_order(T.root, arr)
    return arr

def _in_order(root, arr):
    if root is None: return
    _in_order(root.leftChild, arr)
    arr.append(root.key)
    _in_order(root.rightChild, arr)


if __name__ == "__main__": main()
