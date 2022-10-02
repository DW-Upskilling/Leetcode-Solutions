class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = a if a < b else b
        c = 1
        for i in range(2, n+1):
            if a % i == 0 and b % i == 0:
                c += 1
                
        return c
                
        