def main():
    print("Enter [q] to quit")
    print("Implement a queue using two stacks")
    while True:
        i = input("Pop and push from your queue by typing pop or push value (can also peek): ").split(" ")
        q = my_queue()
        if i[0] == "q":
            break
        if i[0] == "pop":
            print(q.pop())
        elif i[0] == "push":
            q.push(i[1])
        elif i[0] == "peek":
            print(q.peek())
        else:
            raise ValueError("Wrong input")


class my_queue(object):
    
    def __init__(self):
        self.stk_old = []
        self.stk_new = []

    def push(self, val):
        self.stk_new.append(val)

    def pop(self):
        self.shift_stacks()
        return self.stk_old.pop()

    def peek(self):
        # stk_old may not always be nonempty, but when it is, it's guaranteed to have the next-up
        if self.stk_old:
            return self.stk_old[-1]
        else:
            return self.stk_new[0]

    def shift_stacks(self):
        if not self.stk_old:
            while self.stk_new:
                self.stk_old.append(self.stk_new.pop())


if __name__ == "__main__":
    main()
