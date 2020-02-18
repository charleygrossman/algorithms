# Use the Miller-Rabin primality test to determine if a number is prime or composite


import sys
from random import randint


def main():
    datum = _input()
    solution = miller_rabin(datum)

    if solution:
        print('Prime')
    else:
        print('Composite')


def miller_rabin(n):
    for i in range(20):
        a = randint(1, n-1)
        if witness(a, n):
            return False

    return True


def witness(a, n):
    t = 0
    u = n - 1
    while u % 2 == 0:
        u //= 2
        t += 1

    x = modexp(a, u, n)

    for i in range(t):
        tmp = x**2 % n
        if tmp == 1 and x != 1 and x != n - 1:
            return True
        x = tmp

    return True if x != 1 else False


def modexp(a, b, n):
    c = 0
    d = 1
    b = bin(b)[2:]

    for i in range(len(b)):
        c *= 2
        d = d*d % n
        if b[i] == "1":
            c += 1
            d = d*a % n

    return d


def _input():
    datum = int(sys.argv[1].strip())
    return datum


if __name__ == "__main__":
    main()
