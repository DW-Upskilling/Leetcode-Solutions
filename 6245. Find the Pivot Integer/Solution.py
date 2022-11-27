class Solution:
    def pivotInteger(self, n: int) -> int:
        
        nums = []
        s = 0
        for i in range(1, n+1):
            nums.append(i)
            s += i
        
        cs = 0
        for i in range(n-1,-1, -1):
            cs += nums[i]
            # print(nums[i], s, cs)
            if s == cs:
                return nums[i]
            s -= nums[i]
            # print(nums[i])
        
        return -1