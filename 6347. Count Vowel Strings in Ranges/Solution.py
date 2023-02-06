class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        arr = [0]
        for i in range(len(words)):
            w = words[i]
            if w[0] in ('a', 'e', 'i', 'o', 'u') and w[-1] in ('a', 'e', 'i', 'o', 'u'):
                arr.append(1+arr[-1])
            else:
                arr.append(arr[-1])
        output = []
        arr.pop(0)
        # print(arr)
        for q in queries:
            diff = 0
            if q[0] > 0:
                diff = arr[q[0]-1]
            # print(q[0], q[1], diff)
            res = arr[q[1]] - diff
            # res = arr[q[1]] - arr[q[0]-1]
            output.append(res)
            
        return output
                