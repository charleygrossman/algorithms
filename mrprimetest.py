from random import randint

def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a number >= 2 to test if it is a prime, followed by " +
                  " a space and a number of 'witness' trials (Try on a " +
                  " Carmichael number! e.g. 561): ").split()
        if i[0] == "q": break

        arr = [int(x) for x in i]
        o = miller_rabin(arr[0], arr[1])
        if o: print("Prime")
        else: print("Composite")

# The higher the s, the more accurate the test
def miller_rabin(n, s):
    for i in range(1, s):
        a = randint(1, n - 1)
        if witness(a, n): return False
    return True

# a is a witness, n is the test number
def witness(a, n):
    t = 0
    u = n - 1
    while u % 2 == 0:
        u //= 2
        t += 1

    x = modexp(a, u, n)
    for i in range(t):
        tmp = (x ** 2) % n
        if tmp == 1 and x != 1 and x != n - 1: return True
        x = tmp
    if x != 1: return True
    return False

# For computing a^b (mod n)
def modexp(a, b, n):
    c = 0
    d = 1
    b = bin(b)[2:]

    for i in range(len(b)):
        c *= 2
        d = (d*d) % n
        if b[i] == "1":
            c += 1
            d = (d*a) % n
    return d

if __name__ == "__main__":
    main()
