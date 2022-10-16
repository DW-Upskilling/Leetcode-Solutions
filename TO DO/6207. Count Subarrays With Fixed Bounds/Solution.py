class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        
        dp = dict()
        output = 0
        
        def helper(i, j):
            # print(i, j)
            if i not in dp.keys():
                dp[i] = dict()
            elif j in dp[i].keys():
                return dp[i][j]

            curr = [nums[i], nums[i]]
            dp[i][i] = curr
            if curr[0] == minK and curr[1] == maxK:
                # output = output + 1
                print("1")

            for _i in range(i+1, j):
                dp[i][_i] = helper(i, _i)
                curr = [min(curr[0], dp[i][_i][0]), max(curr[1], dp[i][_i][1])]

                dp[_i][j] = helper(_i, j)
                curr = [min(curr[0], dp[_i][j][0]), max(curr[1], dp[_i][j][1])]
                
            dp[i][j] = curr

            if curr[0] == minK and curr[1] == maxK:
                # output = output + 1
                print("1")

            # print(i, j, curr)

            return curr
            
        
        helper(0, len(nums)-1)
        print("_____")
        return output