class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        
        output = []
        zero = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                
            if nums[i] == 0:
                zero += 1
            else: output.append(nums[i])
        output.append(nums[-1])
        return output + [0]*zero
            