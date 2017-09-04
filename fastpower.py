def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a base and its exponent: ").split()
        if i[0] == "q": break

        i = [int(x) for x in i]
        o = fast_power(i[0], i[1])
        print(o)

def fast_power(a, b):
    if b == 1: return a

    c = a * a
    ans = fast_power(c, b//2)
    if b % 2 != 0: return a * ans
    else: return ans

if __name__ == "__main__":
    main()
