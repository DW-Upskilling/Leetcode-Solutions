from Solution import Solution
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(len(data)):
        head = None
        stack = []
        child = 0
        for i in data[i][1:-1].split(","):
            if i == '': continue
            if i == 'null': i = None
            else: i = int(i)

            if not len(stack):
                head = TreeNode(i)
                stack.append(head)
            else:
                node = stack[0]
                n = TreeNode(i) if i != None else None
                if child == 0:
                    node.left = n
                    if n: stack.append(n)
                    child += 1
                else:
                    child = 0
                    node.right = n
                    if n: stack.append(n)
                    stack.pop(0)
        _output = Solution().tree2str(head)

        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()