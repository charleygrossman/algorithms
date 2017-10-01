# Two methods to calculating a Goldbach number

from math import sqrt

def main():
    print("Press [q] to quit")

    while(True):
        i = input("Enter an even positive integer greater than 2 and receive " +
                 "all the pairs of two primes whose sum is equal to it: ")
        if i == "q": break
        i = int(i)
        goldbach(i)

# Generate a list of primes from 2 to n and then print the primes that compose n
def goldbach(n):
    if n == 4:
         print([2, 2])
         return
    primes = sieve_char(n)
    for i in range(len(primes)):
        if n - primes[i] in primes:
            print([primes[i], n-primes[i]])

# Method 1
def sieve_char(n):
    tmp = ['t'] * n
    for i in range(2, int(sqrt(n) + 1)):
        if tmp[i] == 't':
            for j in range(i*2, n, i):
                tmp[j] = 'f'
    return [x for x in range(2, n) if tmp[x] == 't']

# Method 2
def sieve_int(n):
    tmp = set([j for i in range(2, int(sqrt(n)) + 1) for j in range(i*2, n, i)])
    return [x for x in range(2, n) if x not in tmp]

if __name__ == "__main__": main()
