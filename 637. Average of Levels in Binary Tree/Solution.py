# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root) -> list[float]:
        
        stack = [root]
        output = []
        while len(stack):
            nstack = []
            s = 0
            c = 0
            for node in stack:
                c += 1
                s += node.val
                if node.left: nstack.append(node.left)
                if node.right: nstack.append(node.right)
                    
            output.append(s/c)
            stack = nstack
        
        return output