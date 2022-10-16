from Solution import Solution
import json

if __name__ == '__main__':
    data = []
    with open('input', 'r') as fd:
        data = "".join(fd.read().split('"')).split('\n')
    output = []
    for i in range(0, len(data), 3):

        nums = data[i]
        minK = int(data[i+1])
        maxK = int(data[i+2])

        _output = Solution().countSubarrays(
            list(map(int, nums[1:-1].split(","))),
            minK,
            maxK
        )
        output.append(str(_output))
        
    with open('output', 'w') as fd:
        fd.write("\n".join(output))
        fd.close()