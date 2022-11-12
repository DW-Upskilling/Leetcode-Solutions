from Solution import MedianFinder
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        cases = data[i][1:-1].split(",")
        values = data[i+1][1:-1].split(",")
        medianFinder = None
        _output = []
        for i, case in enumerate(cases):
            __output = None
            if case == "MedianFinder":
                medianFinder = MedianFinder()
            elif case == "addNum":
                __output = medianFinder.addNum(int(values[i][1:-1]))
            elif case == "findMedian":
                __output = medianFinder.findMedian()
            _output.append(str(__output))
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()