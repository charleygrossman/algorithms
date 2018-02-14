# Trying to get a computer to randomly generate hello world

import random as rand
from difflib import SequenceMatcher

def main():
    alphabet = [chr(x) for x in range(97, 123)]
    alphabet.append(' ')
    best = ("", 0.0)
    cnt = 0
    while True:
        tmp = generate(alphabet)
        if tmp[1] == 1.0:
            return tmp[0]
        else:
            if tmp[1] > best[1]:
                best = tmp
        cnt += 1
        if cnt % 1000 == 0:
            print("{} found at iteration #{}".format(best[0], cnt))

def generate(alphabet):
    s = ""
    for i in range(11):
        s += alphabet[rand.randrange(27)]
    simRatio = similarity_ratio(s, "hello world")
    return (s, simRatio)

def similarity_ratio(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == "__main__":
    main()
