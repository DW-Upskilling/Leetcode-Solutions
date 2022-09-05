from Solution import Solution
import json
import time
import math

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        n = int(data[i])
        matrix = []
        for row in data[i+1][2:-2].split("],["):
            matrix.append(list(map(int, row.split(","))))
        t1 = time.time() * 1000
        _output = Solution().mostBooked(n, matrix)
        t2 = time.time() * 1000
        t = math.ceil(t2 - t1)
        if t > 1000: t = str(t // 1000) + "s"
        else: t = str(t) + "ms"
        print("Test Case-{0}: {1}".format(i//2, t))
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()