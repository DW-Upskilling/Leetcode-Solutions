from Solution import Solution
import json

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(len(data)):
        head = None
        stack = []
        child = []
        index = -1
        for i in data[i][1:-1].split(","):
            if i == 'null': 
                if index == -1:
                    head = child[0]
                else:
                    stack[index].children = child
                child = []
                index += 1
                continue
            
            i = int(i)
            n = Node(i)
            child.append(n)
            stack.append(n)
        if child:
            stack[index].children = child
        _output = Solution().levelOrder(head)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()