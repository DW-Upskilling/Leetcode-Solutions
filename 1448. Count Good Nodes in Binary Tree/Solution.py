# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        
        if root:
            c = 1
            
            if root.left:
                c += self.trace(root.left, root.val)
                
            if root.right:
                c += self.trace(root.right, root.val)
                
            return c
                
        else:
            return 0
        
    def trace(self, root, val):
        c = 0
        # print(root.val, val)
        if root.val >= val:
            c += 1
            val = root.val
            
        if root.left:
            c += self.trace(root.left, val)

        if root.right:
            c += self.trace(root.right, val)
            
        return c
                
        