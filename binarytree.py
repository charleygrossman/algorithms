def main():
    print("Enter [q] to quit")
    print("Welcome to the binary tree interface! Here are the methods: " +
          "insert, size")

    binaryTree = BinaryTree()

    while True:
        i = input("Enter a command (insert, size): " )
        if i == "q": break

        if i == "insert":
            e = input("Name the element you want to insert: ")
            binaryTree.insert(e)

        if i == "size":
            binaryTree.get_size()

class Node(object):

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

class BinaryTree(object):

    def __init__(self):
        self.root = Node(None)
        self.parent = None
        self.left = None
        self.right = None
        self.size = 0

    def insert(self, child, parent=None, parent_lr=None):
        child = int(child)
        if parent is None:
            parent = self.root

        # Don't insert new and increase size if identical
        if parent.get_value() is None:
            new_node = Node(child)
            parent = new_node
            self.size += 1
        else:
            if child < parent.get_value():
                print("child < parent")
                self.insert(self, child, parent.get_left())
            if child > parent.get_value():
                print("child > parent")
                self.insert(self, child, parent.get_right())

    def get_size(self):
        print(self.size)

if __name__ == "__main__":
    main()
