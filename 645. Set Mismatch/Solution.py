class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        d = dict()
        duplicate = 0
        s = 0
        
        for i in nums:
            if i in d.keys():
                duplicate = i
                continue
            d[i] = 1
            s += i
        
        # Arthmetic progression sum and remove the sum of distinct numbers
        num = int(((len(nums)/2)*(1 + len(nums))) - s)
        
        return [duplicate, num]
        