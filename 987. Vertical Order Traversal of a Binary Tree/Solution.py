# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root) -> list[list[int]]:
        
        stack = [[root, 0, 0]]
        
        d = dict()

        while len(stack):
            
            s = []
            for e in stack:
                
                if e[2] not in d.keys():
                    d[e[2]] = dict()
                if e[1] not in d[e[2]].keys():
                    d[e[2]][e[1]] = []
                
                node = e[0]
                d[e[2]][e[1]].append(node.val)
                if node.left:
                    s.append([node.left, e[1] + 1, e[2] - 1])
                    
                if node.right:
                    s.append([node.right, e[1] + 1, e[2] + 1])
                    
            stack = s
        
        output = []
        # print(d)
        for i in sorted(d.keys()):
            v = []
            for j in sorted(d[i].keys()):
                d[i][j].sort()
                v.extend(d[i][j])
            output.append(v)
        
        return output