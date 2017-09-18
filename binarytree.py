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
            binaryTree.min()

# A node with an initialized value, getters and setters for parent, left, and right
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def value(self):
        return self.value

    def left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def right(self):
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

    def insert(self, e):
        parent = self.root
        flag = True
        while flag:
            l = parent.left()
            r = parent.right()
            if l.value() is not None and l.value > e: parent = l
            elif l.value() is not None and l.value() < e: parent = r
            else: flag = False

        if parent.value() > e:
            parent.set_left(Node(e))
        if parent.value() < e:
            parent.set_right(Node(e))

    def get_size(self):
        print(self.size)

    def min(self):
        current = self.root
        min = None
        while current.value() is not None:
            min = current.value()
            current = current.left()

        print(min)

if __name__ == "__main__":
    main()
