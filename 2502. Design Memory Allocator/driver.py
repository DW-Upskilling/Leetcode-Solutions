from Solution import Allocator
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        l1 = data[i][1:-1].split(",")
        l2 = data[i+1][2:-2].split("],[")
        allocator = None
        _output = []
        for i, opt in enumerate(l1):
            value = l2[i].split(',')
            _out = None
            if opt == "Allocator":
                allocator = Allocator(int(value[0]))
            elif opt == "allocate":
                _out = allocator.allocate(int(value[0]), int(value[1]))
            elif opt == "free":
                _out = allocator.free(int(value[0]))
            _output.append(_out)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()