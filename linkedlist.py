
# WIP: Provide a full and interactive interface to play with a visual linked-list

def main():
    print("Enter [q] to quit")
    print("Welcome to the linked-list interface! Here are the methods: " +
          "insert, delete, search, size, display")

    linkedList = LinkedList()

    while True:
        i = input("Enter a command (insert, delete, search, size, display): " )
        if i == "q": break

        if i == "insert":
            e = input("Name the element you want to insert: ")
            linkedList.insert(e)
        if i == "delete":
            e = input("Name the element you want to delete: ")
            linkedList.delete(e)
        if i == "search":
            e = input("Name the element you're searching for: ")
            o = linkedList.search(e)
            print(o)
        if i == "size":
            s = linkedList.size()
            print(s)
        if i == "display":
            linkedList.display()

class Node(object):

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# LinkedList interfaces Node, user interfaces LinkedList
# Handle raised value errors?
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    # Insert into front of list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
                print("Element not in list")
                # raise ValueError("Data not in list")
        return found

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Element not in list")
            # raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def display(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

if __name__ == "__main__":
    main()
