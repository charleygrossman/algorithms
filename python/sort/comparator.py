from typing import *
from collections import defaultdict
from functools import cmp_to_key


def main():
    s = "ccbbbaad"
    expected = "b3,a2,c2,d1"
    print("pass" if char_count(s) == expected else "fail")


def char_count(s: str) -> str:
    """
    map ascii lowercase chars to count of occurrences,
    sort by occurrences descending and format the kv
    pair as a comma-separated string.

    Note that sorting is a combination of occurrence count decreasing
    and lexicographical char increasing.

    O(n) time, O(1) space, where n is the length of the string.
    """
    m = defaultdict(int)
    for c in s.lower():
        m[c] += 1
    result = []
    for pair in sorted(m.items(), key=cmp_to_key(cmp)):
        result.append(f"{pair[0]}{pair[1]}")
    return result

def cmp(kv1: Tuple[str, int], kv2: Tuple[str, int]) -> int:
    if kv1[1] == kv2[1]:
        return -1 if kv1[0] < kv2[0] else 1
    else:
        return -1 if kv1[1] > kv2[1] else 1


if __name__ == "__main__":
    main()