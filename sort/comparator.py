from typing import *
from collections import defaultdict
from functools import cmp_to_key


def main():
    s = "ccbbbaad"
    want = "b3,a2,c2,d1"
    got = freqsort(s)
    assert want == got, f"freqsort: want={want} got={got}"


def freqsort(s: str) -> str:
    """
    Map the characters of s to their frequencies (occurrences),
    sort by frequency descending, and lexicographically on ties.

    O(n+m) time, O(m) space, where n is the length of s,
    and m is the length of the alphabet of s.
    """
    m = defaultdict(int)
    for c in s:
        m[c] += 1
    return ",".join([f"{kv[0]}{kv[1]}" for kv in sorted(m.items(), key=cmp_to_key(_cmp))])

def _cmp(kv1: Tuple[str, int], kv2: Tuple[str, int]) -> int:
    if kv1[1] == kv2[1]:
        return -1 if kv1[0] < kv2[0] else 1
    else:
        return -1 if kv1[1] > kv2[1] else 1


if __name__ == "__main__":
    main()