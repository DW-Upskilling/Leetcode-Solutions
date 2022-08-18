class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        l = 0
        hashMap = dict()
        for i in arr:
            if i not in hashMap.keys():
                hashMap[i] = 0
            hashMap[i] += 1
            l += 1
        target = l // 2
            
        counts = list(sorted(hashMap.values(), reverse=True))

        result = 0
        while target > 0:
            target -= counts[result]
            result += 1

        return result