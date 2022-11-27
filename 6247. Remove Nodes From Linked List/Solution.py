# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head):
        
        stack = [head]
        curr = head
        
        while curr and curr.next:
            
            curr = curr.next

            while len(stack):
                if curr.val > stack[-1].val:
                    stack.pop()
                    if len(stack):
                        stack[-1].next = curr
                else:
                    break
            stack.append(curr)
                
            # print(stack)

        return stack[0]