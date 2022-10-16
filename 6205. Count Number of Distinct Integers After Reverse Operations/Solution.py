class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        d = dict()
        
        for i in nums:
            
            d[i] = 1
            
            temp = i
            rev = 0
            
            while temp:
                
                rev = rev * 10 + temp % 10
                temp //= 10
            
            d[rev] = 1
            # print(d)
        
        return len(d.keys())