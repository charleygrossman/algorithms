# NOTE: WIP: Pick primes for Goldbach number while generating primes list

from math import sqrt

# Generate a list of primes from 2 to n
# and then print the primes that compose
# the Goldbach number n
def main():
    n = 28
    if n == 4: print([2, 2])
    primesChar = sieve_char(n)
    primesInt = sieve_int(n)
    # print(primes)
    # for i in range(len(primes)):
    #     if n - primes[i] in primes:
    #         print([primes[i], n-primes[i]])

def sieve_char(n):
    tmp = ['t'] * n
    for i in range(2, int(sqrt(n) + 1)):
        if tmp[i] == 't':
            for j in range(i*2, n, i):
                tmp[j] = 'f'
    return [x for x in range(2, n) if tmp[x] == 't']

def sieve_int(n):
    tmp = set([j for i in range(2, int(sqrt(n)) + 1) for j in range(i*2, n, i)])
    return [x for x in range(2, n) if x not in tmp]

if __name__ == "__main__": main()
