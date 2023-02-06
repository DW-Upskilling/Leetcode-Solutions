from Solution import Solution

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        _output = Solution().vowelStrings(
            data[i][1:-1].split(","),
            list(map(lambda e: tuple(map(int, e.split(','))), data[i+1][2:-2].split("],["))),
        )
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()