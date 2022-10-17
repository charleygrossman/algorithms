from typing import *


def main():
    valid = TreeNode(
        data=8,
        left=TreeNode(data=3, left=TreeNode(data=1), right=TreeNode(data=6, left=TreeNode(data=4), right=TreeNode(data=7))),
        right=TreeNode(data=10, right=TreeNode(data=14, left=TreeNode(data=13))),
    )
    print("is a BST" if is_bst(valid) else "is not a BST")

    invalid = TreeNode(
        data=8,
        left=TreeNode(data=3, left=TreeNode(data=1), right=TreeNode(data=6, left=TreeNode(data=4), right=TreeNode(data=7))),
        right=TreeNode(data=10, right=TreeNode(data=14, left=TreeNode(data=16))),
    )
    print("is a BST" if is_bst(invalid) else "is not a BST")


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