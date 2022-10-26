from Solution import Solution
import json
import time

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    with open('output', 'r') as fd:
        actual_output = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 2):
        k = int(data[i+1])
        nums = list(map(int, data[i][1:-1].split(",")))
        t1 = time.time()*1000
        _output = Solution().checkSubarraySum(nums, k)
        t2 = time.time()*1000
        output.append(str(_output))
        print(i//2, "{0} ms".format(round(t2 - t1)), "P" if actual_output[i//2] == str(_output) else "F")
    with open('.output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()