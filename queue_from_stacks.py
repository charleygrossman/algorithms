def main():
    print("Enter [q] to quit")
    print("Implement a queue using two stacks")
    while True:
        i = input("Pop and push from your queue by typing pop or push value: ").split(" ")
        q = my_queue()
        if i[0] == "q":
            break
        if i[0] == "pop":
            print(q.pop())
        elif i[0] == "push":
            q.push(i[1])
        else:
            raise ValueError("Wrong input")


class my_queue(object):
    def __init__(self):
        self.stack_oldest = []
        self.stack_newest = []

    def push(self, val):
        self.stack_newest.append(val)

    def pop(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def shift_stacks(self):
        if not self.stack_oldest:
            while self.stack_newest:
                self.stack_oldest.append(self.stack_newest.pop())


if __name__ == "__main__":
    main()
