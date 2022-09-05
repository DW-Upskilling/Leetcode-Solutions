# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if not root: return []
        output = []
        stack = [root]
        
        while len(stack):
            _out = []
            _stack = []
            for n in stack:
                if n.children:
                    _stack.extend(n.children)
                    
                _out.append(n.val)
            
            output.append(_out)
            stack = _stack
        # print(output)
        return output
        