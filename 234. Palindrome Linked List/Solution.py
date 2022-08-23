# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:

        # Two pointers -> 1 jump, 2 jumps
        p1 = head
        p2 = head

        left = []

        # by the end of the loop p1 will be in the middle
        while p1 and p2 and p2.next:
            left.append(p1.val)
            p1 = p1.next
            p2 = p2.next.next

        # if odd number of elements present p2 never become null
        if p2:
            p1 = p1.next

        # comparing remaining half of the linked list
        while p1:
            if p1.val != left[-1]:
                return False
            p1 = p1.next
            left.pop()

        return True
