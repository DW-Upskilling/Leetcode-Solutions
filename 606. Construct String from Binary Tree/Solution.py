# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root) -> str:
        
        if not root: return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if left:
            left = "(" + left + ")"
        elif right:
            left = "()"
        else:
            left = ""
            
        if right:
            right = "(" + right + ")"
        else:
            right = ""
        
        return str(root.val) + left + right