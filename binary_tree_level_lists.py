# import structs.linkedlist as llist
# import structs.searchtree as bin_tree

def main():
    print("Make a linkedlist for all nodes at every depth of a binary tree")


def depth_lists(tree):
    lists = {}
    #tree = Tree()
    _depth_lists(tree.root, 0, lists)
    return lists

def _depth_lists(node, depth, lists):
    if not node: return
    if depth not in lists: lists[depth] = llist.LinkedList()
    else: lists[depth].insert(node.val)
    if node.left: _depth_lists(node.left, depth+1, lists)
    if node.right: _depth_lists(node.right, depth+1, lists)


if __name__ == "__main__":
    main()
