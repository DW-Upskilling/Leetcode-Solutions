class Solution:
    # Time Limit Issue for larger sets
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        csum = [nums[0]]
        for i in nums[1:]:
            csum.append(csum[-1] + i)
            if csum[-1] % k == 0:
                return True
        
        for i in range(1, len(nums)-1):

            if csum[-1] - csum[i-1] < k and not (nums[i] == 0 and nums[i+1] == 0):
                # print(csum[-1] - csum[i-1] < k, csum[-1] - csum[i-1] != 0, i)
                continue
            # print(csum[-1] - csum[i-1], k)
            for j in range(i+1, len(nums)):
                
                if csum[j] - csum[i-1] % k == 0:
                    # print(i, j, nums[i:j+1])
                    return True
        
        return False