class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        
        h = num // 2
        
        if h == num: return True
        
        reverse = lambda x: int(str(x)[::-1])
        for i in range(h, num):
            
            if i + reverse(i) == num:
                return True
            
        return False 