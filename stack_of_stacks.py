def main():
    print("Implement a stack that uses a list of resizable stacks")
    print("Enter [q] to quit")
    stack = Stack()
    while True:
        i = input("Enter push [element] or pop: ").split(" ")
        if i[0] == "q": break
        elif i[0] == "push": stack.push(i[1])
        elif i[0] == "pop": print(stack.pop())
        else: pass
        print("Current stack: {}".format(stack.stacklist))


class Stack(object):

    def __init__(self, maxsize=4):
        self.stacklist = []
        self.maxsize = maxsize

    def push(self, e):
        if len(self.stacklist) == 0: self.stacklist.append([e])
        else:
            last = self.stacklist[-1]
            if len(last) > 0 and len(last) < self.maxsize: last.append(e)
            else: self.stacklist.append([e])

    def pop(self):
        if len(self.stacklist) == 0: return None
        else:
            last = self.stacklist[-1]
            retval = last.pop()
            if len(last) == 0: self.stacklist = self.stacklist[:-1]
            return retval


if __name__ == "__main__": main()
