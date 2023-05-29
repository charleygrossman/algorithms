from typing import *


def main():
    found, not_found = "found", "not found"

    keys = ["she", "sells", "down", "by", "seashore"]
    print(f"initial keys: {keys}")
    t = Trie(keys)
    for key in ["she", "sells", "seashells", "down", "by", "the", "seashore"]:
        print(f"{key}: {found if t.search(key) else not_found}")

    key = "seashells"
    t.insert(key)
    print(f"inserted: {key}")
    print(f"{key}: {found if t.search(key) else not_found}")


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}

class Trie:
    def __init__(self, keys: Sequence[str]):
        self.root = TrieNode()
        for k in keys:
            self.insert(k)

    def insert(self, key: str):
        curr = self.root
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

    def search(self, key: str):
        curr = self.root
        for c in key:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


if __name__ == '__main__':
    main()
