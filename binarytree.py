def main():
    print("Enter [q] to quit")
    print("Welcome to the binary tree interface! Here are the methods: " +
          "insert, size, min")

    init = int(input("Please initialize your tree with a value here: "))
    binaryTree = BinaryTree(init)

    while True:
        i = input("Enter a command (insert, size, min): " )
        if i == "q": break

        if i == "insert":
            e = input("Name the element you want to insert: ")
            binaryTree.insert(int(e))

        if i == "size":
            binaryTree.get_size()

        if i == "min":
            binaryTree.get_min()

# A node with an initialized value, getters and setters for parent, left, and right
class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def get_left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def get_right(self):
        return self.right

    def set_right(self, new_right):
        self.right = new_right

class BinaryTree(object):

    # Initialize by constructing a non-null root
    def __init__(self, init):
        self.root = Node(init)
        self.root.set_left(Node(None))
        self.root.set_right(Node(None))
        self.size = 1

    # Default parameters are for internal recursive call (Refactor w/ helper?)
    def insert(self, child, parent_t=None, parent=None):
        if parent is None:
            # We start at the root
            parent = self.root

        # Occurs when a null leaf is hit
        if parent.get_value() is None:
            new_node = Node(child)
            tmp = parent.get_parent()
            parent = new_node
            parent.set_parent(tmp)
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

    def get_min(self):
        current = self.root.get_left()
        min = current.get_value()

        while current.get_value():
            min = current.get_value()
            current = current.get_left()

        print(min)

if __name__ == "__main__":
    main()
