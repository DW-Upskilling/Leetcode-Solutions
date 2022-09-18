# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        
        stack = [root]
        level = 0
        
        
        while len(stack):
            
            _s = []
            for n in stack:
                
                if n.left:
                    _s.append(n.left)
                if n.right:
                    _s.append(n.right)
                
                pass
            
            if (level+1) % 2 != 0:
                _s = self.ReverseNodes(stack, _s[::-1])
            
            stack = _s
            level += 1
            
        return root
    
    def ReverseNodes(self, parents, childs):
        
        for i in range(len(childs) // 2):
            # print(childs[i].val, childs[len(childs)-i-1].val)
            t1 = childs[i].left
            t2 = childs[i].right
            
            childs[i].left = childs[len(childs)-i-1].left
            childs[i].right = childs[len(childs)-i-1].right
            childs[len(childs)-i-1].left = t1
            childs[len(childs)-i-1].right = t2
        
        i = 0
        for p in parents:
            
            if p.left:
                # print(p.left.val, childs[i].val)
                p.left = childs[i]
                i+=1
                pass
            
            if p.right:
                # print(p.right.val, childs[i].val)
                p.right = childs[i]
                i+=1
                pass
            
        return childs
        
        
        