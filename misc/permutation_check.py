def main():
    print("Enter [q] to quit")
    while True:
        i = input("Enter two strings to see if they're permutations: ").split(" ")
        if i[0] == "q": break
        print(is_permutation(i[0], i[1]))

def is_permutation(a, b):
    if len(a) != len(b): return False
    d = {}
    for i in range(len(a)):
        if a[i] in d: d[a[i]] += 1
        else: d[a[i]] = 1
        if b[i] in d: d[b[i]] -= 1
        else: d[b[i]] = -1
    for v in d.values():
        if v != 0: return False
    return True


if __name__ == "__main__": main()
