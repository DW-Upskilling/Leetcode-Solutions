# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        
        if not head: return None
        one = head
        if not head.next: return None
        two = head.next
        
        while two and two.next and two.next.next:
            
            one = one.next
            two = two.next.next
            
        one.next = one.next.next
        
        return head
        