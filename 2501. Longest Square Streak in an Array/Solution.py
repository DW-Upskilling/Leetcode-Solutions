class Solution:
    def longestSquareStreak(self, nums: list[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        d = dict()
        
        output = -1
        for i in range(len(nums)):
            
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            curr = d[nums[i]]
            
            sq = nums[i] ** 2
            if sq not in d.keys():
                d[sq] = 1
            d[sq] += curr
            
            # print(nums[i], d)
            
        # print(d)
        for i in range(len(nums)):
            if d[nums[i]] > 1:
                output = max(output, d[nums[i]])
        # print(d)
        return output