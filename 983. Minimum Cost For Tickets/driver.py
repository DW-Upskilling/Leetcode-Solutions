from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        days = list(map(int, data[i][1:-1].split(',')))
        costs = list(map(int, data[i+1][1:-1].split(',')))
        _output = Solution().mincostTickets(days, costs)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()