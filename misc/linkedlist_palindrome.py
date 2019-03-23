# Room for improvement:
# 1.) A queue is not needed here- just use a stack for the first half,
# and pop that while comparing current node for the second first_half
# 2.) If size is not known, use the slow/fast runner technique

import struct.linkedlist as ll
from collections import deque

def main():
    print("Enter [q] to quit")
    while True:
        print("Check if a (linkedlist) word is a palindrome")
        i = input("Enter a word: ")
        if i == "q":
            break
        ll_word = ll.LinkedList()
        for letter in i:
            ll_word.insert(letter)

        answer = is_palindrome(ll_word)
        if answer:
            print("Yes")
        else:
            print("No")

def is_palindrome(ll_word):
    size = ll_word.size()
    if size == 0 or size == 1:
        return True
    if size % 2 == 0:
        center_index = (size / 2) - 1
    else:
        center_index = size // 2
    # Stack (append, pop)
    first_half = []
    # Queue (append, popleft)
    second_half = deque()

    i = 0
    curr = ll_word.head
    while curr:
        if i < center_index:
            first_half.append(curr.get_data())
        elif i > center_index:
            second_half.append(curr.get_data())
        else:
            if size % 2 == 0:
                first_half.append(curr.get_data())
        curr = curr.get_next()
        i += 1

    print(first_half)
    print(second_half)

    if len(first_half) != len(second_half):
        return False
    else:
        while first_half:
            if first_half.pop() != second_half.popleft():
                return False
        return True

if __name__ == "__main__":
    main()
