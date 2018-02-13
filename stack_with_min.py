def main():
    print("A stack that knows its minimum value")
    i = input("Enter the initial values of the stack separated by space: ").split(" ")
    tmp = [int(x) for x in i]
    stack = Min_Stack(tmp)
    print("Enter [q] to quit")
    while True:
        i = input("Enter a command (push, pop, min, show): " )
        if i == "q": break
        if i == "push":
            e = input("Name the element you want to push: ")
            stack.push(int(e))
        if i == "pop":
            print(stack.pop())
        if i == "min":
            print(stack.min())
        if i == "show":
            print(stack)
        else:
            print("This stack only supports push, pop and min functionality")

class Min_Stack(object):

    def __init__(self, vals=[]):
        self.stack, self.min_stack = [], []
        for v in vals:
            self.push(v)

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            if val <= self.min_stack[-1]: self.min_stack.append(val)
        else:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            retval = self.stack.pop()
            if retval == self.min_stack[-1]: self.min_stack.pop()
            return retval
        else:
            print("The stack is empty")

    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("The stack is empty")

    def __str__(self):
        return str(self.stack)

if __name__ == "__main__": main()
