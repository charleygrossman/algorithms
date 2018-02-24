def main():
    print("Enter [q] to quit")
    while True:
        i = input("Enter two strings to see if they're permutations: ").split(" ")
        if i[0] == "q": break
        print(is_permutation(i[0], i[1]))

def is_permutation(a, b):
    if len(a) != len(b): return False
    a_dict, b_dict = {}, {}
    fill_dict(a_dict, a)
    fill_dict(b_dict, b)
    for k,v in a_dict.items():
        if k not in b_dict: return False
        else:
            if b_dict[k] != v: return False
    return True

def fill_dict(d, s):
    for char in s:
        if char in d: d[char] += 1
        else: d[char] = 1


if __name__ == "__main__": main()
