class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = dict()
        
        def helper(index = 0):
            if index == len(s):
                return 1;

            if s[index] == '0':
                return 0
            
            if index in dp.keys():
                return dp[index]
            
            ans = helper(index + 1)
            
            if s[index] == '1' and index+1 < len(s):
                ans += helper(index + 2)
            elif s[index] == '2' and index+1 < len(s) and int(s[index+1]) <= 6:
                ans += helper(index + 2)
                
            dp[index] = ans
            
            return ans
        
        return helper()