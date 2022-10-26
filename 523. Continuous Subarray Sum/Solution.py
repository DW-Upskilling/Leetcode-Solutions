class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        hashMap = dict()
        remainder = nums[0] % k
        hashMap[remainder] = 0

        for i in range(1, len(nums)):
            remainder = (remainder + nums[i]) % k

            if remainder == 0:
                return True

            if remainder in hashMap.keys():
                if i - hashMap[remainder] > 1:
                    return True
            else:
                hashMap[remainder] = i

        return False