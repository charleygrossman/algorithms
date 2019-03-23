# A binary tree implementation with randomly chosen root and node positions.
# Favors being a full tree by always assigning left and right children if possible


from random import choice, randint


class BinaryTree(object):

    def __init__(self, nodes):
        if not self._validate(nodes):
            print('Takes a list of numbers as strings')
            raise ValueError
        try:
            # Not always good or even feasible memory-wise for large trees
            nodes = [Node(x) for x in nodes]
            self.root = choice(nodes)
            nodes.remove(self.root)
            _fill_tree(self.root, nodes)
        except ValueError:
            raise

    def __str__(self):
        print(self.root)
        for n in self.nodes:
            print(n)

    def root(self):
        return self.root

    def _validate(nodes):
        if not nodes.isinstance(list) or not nodes:
            return False
        for n in nodes:
            if not n.isnumeric():
                return False
        return True

    def _fill_tree(self, root, nodes):
        if not nodes: return retval
        r = randint(0, 1)
        # If current root doesn't have two children, grab a node and assign as
        # left or right child
        if not root.left or not root.right:
            n = choice(nodes)
            nodes.remove(n)
            n.parent = root
            # If r is 0, favor the left side. Else, favor the right
            if r == 0:
                if not root.left:
                    root.left = n
                else:
                    root.right = n
            else:
                if not root.right:
                    root.right = n
                else:
                    root.left = n
            _fill_tree(root, nodes)
        # Current root has two children; recurse on one of them
        else:
            curr = root.left if r == 0 else root.right
            _fill_tree(curr, nodes)


class Node(object):

    def __init__(self, val):
        if not self._validate(val):
            print('Use only numbers as node values')
            raise ValueError
        else:
            self.val, = int(val)
            self.left, self.right, self.parent = None, None, None

    def __str__(self):
        return 'value:{}, left:{}, right:{}, parent:{}\n'.format(
               self.val, self.left, self.right, self.parent)

    def _validate(self, val):
        if not val or not val.isnumeric():
            return False
        return True
