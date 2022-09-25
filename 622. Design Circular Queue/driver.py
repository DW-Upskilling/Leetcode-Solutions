from Solution import MyCircularQueue
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        l1 = data[i][1:-1].split(",")
        l2 = data[i+1][1:-1].split(",")
        circularQueue = None
        _output = []
        for i, opt in enumerate(l1):
            value = l2[i][1:-1]
            _out = None
            if opt == "MyCircularQueue":
                circularQueue = MyCircularQueue(int(value))
            elif opt == "enQueue":
                _out = circularQueue.enQueue(int(value))
            elif opt == "deQueue":
                _out = circularQueue.deQueue()
            elif opt == "Front":
                _out = circularQueue.Front()
            elif opt == "Rear":
                _out = circularQueue.Rear()
            elif opt == "isEmpty":
                _out = circularQueue.isEmpty()
            elif opt == "isFull":
                _out = circularQueue.isFull()
            _output.append(_out)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()