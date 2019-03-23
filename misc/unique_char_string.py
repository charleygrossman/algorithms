def main():
    print("Enter [q] to quit")
    while True:
        print("Tell whether every character in a string is unique or not")
        i = input("Enter a string: ")
        if i == "q": break
        print(is_unique(i))

def is_unique(s):
    seen = {}
    for c in s:
        if c not in seen: seen[c] = True
        else: return False
    return True

if __name__ == "__main__": main()
