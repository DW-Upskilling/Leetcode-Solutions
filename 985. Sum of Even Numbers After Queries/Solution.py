class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
        output = []
        s = 0
        for n in nums:
            if n % 2 == 0:
                s += n
        
        for q in queries:
            
            index = q[1]
            value = q[0]
            prev = nums[index]
            
            if prev % 2 == 0:
                s -= prev
            
            nums[index] += value
            if nums[index] % 2 == 0:
                s += nums[index]
        
            output.append(s)
            
        return output                
            