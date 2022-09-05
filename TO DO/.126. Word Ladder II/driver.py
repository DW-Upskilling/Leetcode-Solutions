from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 3):
        _output = Solution().findLadders(data[i], data[i+1], data[i+2][1:-1].split(','))
        output.append(json.dumps(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()
    
    