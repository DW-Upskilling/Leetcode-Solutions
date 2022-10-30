class Solution:
    def averageValue(self, nums: list[int]) -> int:
        
        arr = []
        
        for i in nums:
            
            if i % 3 == 0 and i % 2 == 0:
                arr.append(i)
                
        return sum(arr)//len(arr) if len(arr) else 0