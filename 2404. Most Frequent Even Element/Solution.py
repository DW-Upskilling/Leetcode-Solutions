class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        
        d = dict()
        mx = 0
        for i in nums:
            
            if i % 2 == 0:
                if i not in d.keys():
                    d[i] = 0
                d[i] += 1
                if d[i] > mx:
                    mx = d[i]
        
        for k in sorted(d.keys()):
            if d[k] == mx:
                return k
        
        return -1