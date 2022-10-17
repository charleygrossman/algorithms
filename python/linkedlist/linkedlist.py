from typing import *
import copy

def main():
    head = ListNode(data=1, next=ListNode(data=2, next=ListNode(data=3, next=ListNode(data=4))))
    print(f"traversal: {traverse(head)}")
    print(f"reversal: {reverse(head)}")
    print(f"last: {k_from_last(head, 1)}")
    print(f"second from last: {k_from_last(head, 2)}")
    print(f"third from last: {k_from_last(head, 3)}")
    print(f"first: {k_from_last(head, 4)}")

class ListNode:
    def __init__(self, data: Optional[int]=None, next=None):
        self.data = data
        self.next = next

def traverse(head: ListNode) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

def reverse(head: ListNode) -> List[int]:
    curr, prev = copy.deepcopy(head), None
    while curr:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
    return traverse(prev)

def k_from_last(head: ListNode, k: int) -> int:
    fast, slow = head, head
    for i in range(k):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.data

if __name__ == "__main__":
    main()