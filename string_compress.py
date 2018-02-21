import os
import random as rand

def main():
    print("Compess a string by consecutive same characters")
    print("Generating a 10-million character string.")
    i = generate()
    start = etime()
    compress_with_str(i)
    end = etime()
    elapsed = end - start
    print("String concatenation took {}".format(elapsed))

    start = etime()
    compress_with_arr(i)
    end = etime()
    elapsed = end - start
    print("Array append and join took {}".format(elapsed))

# Quadratic in time?
def compress_with_str(S):
    if len(S) < 2: return S
    retval = ""
    curr = S[0]
    cnt = 1
    for i in range(1, len(S)):
        if S[i] != curr:
            if cnt == 1: retval += curr
            else: retval += curr + str(cnt)
            curr = S[i]
            cnt = 1
        else:
            cnt += 1
    if cnt == 1: retval += curr
    else: retval += curr + str(cnt)
    return retval

# Linear in time?
def compress_with_arr(S):
    if len(S) < 2: return S
    aux = []
    curr = S[0]
    cnt = 1
    for i in range(1, len(S)):
        if S[i] != curr:
            if cnt == 1: aux.append(curr)
            else: aux.append(curr + str(cnt))
            curr = S[i]
            cnt = 1
        else:
            cnt += 1
    if cnt == 1: aux.append(curr)
    else: aux.append(curr + str(cnt))
    return "".join(aux)

def generate():
    alphabet = [chr(x) for x in range(97, 123)]
    s = []
    for i in range(10000000):
        s.append(alphabet[rand.randrange(26)])
    return "".join(s)

def etime():
    user, sys, chuser, chsys, real = os.times()
    return user+sys

if __name__ == "__main__": main()
