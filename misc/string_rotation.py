import random as rand

def main():
    print("Tell if one string is a rotation of another")
    test_is_rotation()

def test_is_rotation(trials=100, string_size=10):
    s1, s2 = "", ""
    for i in range(trials):
        for j in range(string_size):
            s1 += chr(rand.randint(97, 122))

        point = rand.randint(0, string_size)
        s2 = s1[point-1:] + s1[:point-1]

        if not is_rotation(s1, s2):
            print("Failed test at s1={}, s2={}".format(s1, s2))
            return

        s1, s2 = "", ""

    print("Passed tests")


def is_rotation(s1, s2):
    if s1 is None or s2 is None: return False
    else:
        tmp = s1 + s1
        if s2 in tmp: return True
        else: return False


if __name__ == "__main__": main()
