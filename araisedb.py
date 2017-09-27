# Given a positive integer n, find if integers a,b such that a^b = n exist.
# Assume that n > b > 1

def main():
    print("Enter [q] to quit")

    while True:
        i = input("Enter a positive integer: ")
        if i == "q": break

        i = int(i)
        o = a_raised_b(i)
        if o: print("Yes")
        else: print("No")

def a_raised_b(n):
    pFacts = p_factors(n)
    if n == 1 or n in pFacts: return False
    pfDistinct = list(set(pFacts))
    if len(pfDistinct) == 1: return True

    maxDegree = 1
    for i in range(len(pfDistinct)-1):
        if pFacts.count(pfDistinct[i]) != pFacts.count(pfDistinct[i+1]):
            return False
        maxDegree = max(maxDegree, pFacts.count(pfDistinct[i]))

    if maxDegree == 1: return False
    return True

# NOTE: Doesn't include 1 in list of factors
def p_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
       factors.append(n)
    return factors

if __name__ == "__main__": main()
