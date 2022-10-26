from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        word1 = [w.strip() for w in data[i][1:-1].split(",")]
        word2 = [w.strip() for w in data[i+1][1:-1].split(",")]
        _output = Solution().arrayStringsAreEqual(word1, word2)
        output.append(str(_output))
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()