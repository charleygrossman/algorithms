from typing import *


def main():
    root = TreeNode(
        data=8,
        left=TreeNode(data=3, left=TreeNode(data=1), right=TreeNode(data=6, left=TreeNode(data=4), right=TreeNode(data=7))),
        right=TreeNode(data=10, right=TreeNode(data=14, left=TreeNode(data=13))),
    )
    print(f"inorder iterative: {inorder_iterative(root)}")
    print(f"inorder recursive: {inorder_recursive(root)}")
    print(f"preorder recursive: {preorder_recursive(root)}")
    print(f"postorder recursive: {postorder_recursive(root)}")


class TreeNode:
    def __init__(self, data: Optional[int]=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder_iterative(root: TreeNode) -> List[int]:
    result = []
    curr = root
    s = []
    while curr or s:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            v = s.pop()
            result.append(v.data)
            curr = v.right
    return result

def inorder_recursive(root: TreeNode) -> List[int]:
    result = []
    _inorder_recursive(root, result)
    return result

def _inorder_recursive(node: Optional[TreeNode], result: List[int]):
    if not node:
        return
    _inorder_recursive(node.left, result)
    result.append(node.data)
    _inorder_recursive(node.right, result)
 
def preorder_recursive(root: TreeNode) -> List[int]:
    result = []
    _preorder_recursive(root, result)
    return result

def _preorder_recursive(node: Optional[TreeNode], result: List[int]):
    if not node:
        return
    result.append(node.data)
    _preorder_recursive(node.left, result)
    _preorder_recursive(node.right, result)

def postorder_recursive(root: TreeNode) -> List[int]:
    result = []
    _postorder_recursive(root, result)
    return result

def _postorder_recursive(node: Optional[TreeNode], result: List[int]):
    if not node:
        return
    _postorder_recursive(node.left, result)
    _postorder_recursive(node.right, result)
    result.append(node.data)


if __name__ == "__main__":
    main()