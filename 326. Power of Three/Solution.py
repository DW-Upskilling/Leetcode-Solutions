class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True
        
        # if n is even or divisble by 2 its false
        if (n & 1) == 0:
            return False
        
        x = 1
        while x < n:
            x *= 3
        
        return x == n

    def isPowerOfThree2(self, n: int) -> bool:
        # Because 3^19(1,162,261,467) is the largest power of three under 2^31 - 1
        max_possible_power = 3 ** 19
        # So we just neet to check if n > 0 and whether3^19 % n is 0
        return n > 0 and max_possible_power % n == 0