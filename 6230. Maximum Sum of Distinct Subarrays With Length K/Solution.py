class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        output = 0
        
        s = ""
        d = dict()
        
        i = 0
        skip = 0
        while i < len(nums) - (k - 1):
            flg = True
            if s == "":
                s = sum(nums[i:i+k])
                for j in range(i, i+k):
                    if nums[j] in d.keys():
                        flg = False
                    d[nums[j]] = j
            else:
                # print(nums[i:i+k], nums[i-1], i)
                s += nums[i+k-1] - nums[i-1]
                if nums[i+k-1] in d.keys() and d[nums[i+k-1]] > i-1:
                    flg = False
                d[nums[i+k-1]] = i+k-1
                
            if flg and output < s and not skip:
                output = s
            elif not flg:
                skip = i+k-1
            # print(s, d)
            
            i += 1
            if skip:
                skip -= 1
        
        
        return output