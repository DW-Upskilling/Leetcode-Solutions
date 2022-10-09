class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = dict()
        
        for i in nums:
            if i in d.keys():
                return True
            
            d[i] = 0
            
        return False
        