from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        l1 = list(map(int, data[i][1:-1].split(",")))
        l2 = list(map(lambda l: list(map(int, l.split(','))), data[i+1][2:-2].split("],[")))
        _output = Solution().sumEvenAfterQueries(l1, l2)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()