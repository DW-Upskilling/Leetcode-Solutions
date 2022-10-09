# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        stack = [root]
        
        while stack:
            # level order over the give tree
            s = []
            for n in stack:
                # for every node check if there an node that statisfies the condition
                node = self.search(root, k-n.val)
                if node and node != n: return True
                
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)
                    
            stack = s
        
        return False
        
    # Binary search since tree is a binary tree
    def search(self, root, k):
        
        if not root: return None
        
        if k > root.val:
            return self.search(root.right, k)
        if k < root.val:
            return self.search(root.left, k)
        
        return root