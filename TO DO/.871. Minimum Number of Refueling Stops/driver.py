from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(15, len(data), 3):
        target = int(data[i])
        startFuel = int(data[i+1])
        stations = []
        for i in data[i+2][1:-1].split("],["):
            _temp = "".join(i.split("["))
            _temp = "".join(_temp.split("]"))
            if not _temp: continue
            stations.append(list(map(int, _temp.split(","))))
        _output = Solution().minRefuelStops(target, startFuel, stations)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()