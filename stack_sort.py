def main():
    print("Enter [q] to quit")
    while True:
        print("Sort a stack in ascending order")
        i = input("Enter the values of the stack separated by space: ").split()
        if i[0] == "q":
            break
        stack = [int(x) for x in i]
        print("Before sort:")
        for e in stack:
            print(e)
        print("After sort:")
        stack = sort_stack(stack)
        for e in stack:
            print(e)

def sort_stack(stack):
    aux = []
    tmp = None
    while stack:
        tmp = stack.pop()
        while aux and aux[-1] < tmp:
                stack.append(aux.pop())
        aux.append(tmp)
    return aux


if __name__ == "__main__": main()
