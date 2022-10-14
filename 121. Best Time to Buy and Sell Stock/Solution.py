class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sm = prices[0]
        
        profit = 0
        
        for i in prices[1:]:
            _p = i - sm
            if i < sm:
                sm = i
            if _p > profit:
                profit = _p
            
                
        return profit