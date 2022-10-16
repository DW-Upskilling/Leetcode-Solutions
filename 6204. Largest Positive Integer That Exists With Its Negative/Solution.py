class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        
        d = dict()
        
        for i in nums:
            
            if i not in d.keys():
                d[i] = 0
                
            d[i] += 1
            
        output = -1
        
        for i in d.keys():
            if i in d.keys() and -i in d.keys():
                if d[i] and d[-i] and output < i:
                    output = i
        
        return output
        