from typing import *


def main():
    valid = TreeNode(
        data=8,
        left=TreeNode(data=3, left=TreeNode(data=1), right=TreeNode(data=6, left=TreeNode(data=4), right=TreeNode(data=7))),
        right=TreeNode(data=10, right=TreeNode(data=14, left=TreeNode(data=13))),
    )
    want = True
    got = is_bst(valid)
    assert want == got, f"valid BST: want={want} got={got}"

    invalid = TreeNode(
        data=8,
        left=TreeNode(data=3, left=TreeNode(data=1), right=TreeNode(data=6, left=TreeNode(data=4), right=TreeNode(data=7))),
        right=TreeNode(data=10, right=TreeNode(data=14, left=TreeNode(data=16))),
    )
    want = False
    got = is_bst(invalid)
    assert want == got, f"invalid BST: want={want} got={got}"


class TreeNode:
    def __init__(self, data: Optional[int]=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_bst(root: Optional[TreeNode]) -> bool:
    return _is_bst(root)

def _is_bst(root: Optional[TreeNode], low: Optional[TreeNode]=None, high: Optional[TreeNode]=None) -> bool:
    if not root:
        return True
    if low and low.data >= root.data:
        return False
    if high and high.data <= root.data:
        return False
    return _is_bst(root.left, low, root) and _is_bst(root.right, root, high)


if __name__ == "__main__":
    main()