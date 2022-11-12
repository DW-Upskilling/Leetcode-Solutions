class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        k = 1
        i = 1
        prev = nums[0]
        
        while i < len(nums):
            
            if nums[i] == prev:
                if i < len(nums) - 1:
                    j = i+1
                    while nums[j] == nums[i] and j < len(nums) - 1:
                        j += 1
                    
                    for n in range(i, j+1):
                        if nums[j] == prev:
                            nums[n] = '_'
                        else:
                            nums[n] = nums[j]
                else:
                    nums[i] = '_'
                continue
            elif nums[i] != '_':
                prev = nums[i]
                k += 1
            
            i += 1
        # print(k)
        return k
            