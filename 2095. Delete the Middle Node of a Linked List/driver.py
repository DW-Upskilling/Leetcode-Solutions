from Solution import Solution
import json

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(len(data)):
        head = None
        curr = None
        for i in map(int, data[i][1:-1].split(",")):
            if not head:
                head = ListNode(i)
                curr = head
            else:
                n = ListNode(i)
                curr.next = n
                curr = curr.next

        head = Solution().deleteMiddle(head)
        _output = []
        while head:
            _output.append(head.val)
            head = head.next
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()