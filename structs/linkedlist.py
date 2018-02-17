class Node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next(self):
        return self.nextNode

    def set_next(self, newNext):
        self.nextNode = newNext

# LinkedList interfaces Node, user interfaces LinkedList
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    # TODO: Inserts in reverse order
    def insert(self, data):
        newNode = Node(data)
        newNode.set_next(self.head)
        self.head = newNode

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def search(self, data):
        curr = self.head
        found = False
        while curr and found is False:
            if curr.get_data() == data:
                found = True
            else:
                curr = curr.get_next()
        if curr is None:
            raise ValueError("Data not in list")
        return found

    def delete(self, data):
        curr = self.head
        previous = None
        found = False
        while curr and found is False:
            if curr.get_data() == data:
                found = True
            else:
                previous = curr
                curr = curr.get_next()
        if curr is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = curr.get_next()
        else:
            previous.set_next(curr.get_next())

    def display(self):
        curr = self.head
        while curr:
            print(curr.get_data())
            curr = curr.get_next()
