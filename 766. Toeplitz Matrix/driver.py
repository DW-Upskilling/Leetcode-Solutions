from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(len(data)):
        matrix = []
        for row in data[i][2:-2].split("],["):
            matrix.append(list(map(int, row.split(","))))
        _output = Solution().isToeplitzMatrix(matrix)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()