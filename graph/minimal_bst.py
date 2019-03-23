def main():
    print("Enter [q] to quit")
    while True:
        print("Turn an increasing, unique-valued array into a minimal bst")
        i = input("Enter increasing, unique values separated by space: ").split(" ")
        if i[0] == "q": break
        A = [int(x) for x in i]
        T = minimal_bst(A)
        print(T)

def minimal_bst(A):
    if not A: return
    center = len(A)//2
    new_node = Node(A[center])
    # If len(A) == 1 we're at leafs, so don't recurse
    if len(A) > 1:
        new_node.set_left(minimal_bst(A[:center]))
        new_node.set_right(minimal_bst(A[center+1:]))
    return new_node

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.children = set()

    def set_left(self, node):
        self.left = node
        self.children.add(node)

    def set_right(self, node):
        self.right = node
        self.children.add(node)

    def __str__(self):
        # ret = "\t"*level+repr(self.val)+"\n"
        ret = repr(self.val) + '\n'
        for child in self.children:
            if child: ret += child.__str__()
        return ret

    def __repr__(self):
        return '<tree node representation>'


# This code constructs a preordered list
#         return minimal_bst(A)
#
#
# def minimal_bst(A):
#     if len(A) == 0: return None
#     fill_tree(A)
#
#
# def fill_tree(A):
#     hi = len(A)-1
#     if hi == 0:
#         print(A[hi])
#         return
#     elif hi > 0:
#         mid = hi // 2
#         print(A[mid])
#         fill_tree(A[:mid])
#         fill_tree(A[mid+1:])
#     else:
#         return


if __name__ == "__main__": main()
