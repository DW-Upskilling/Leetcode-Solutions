class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n should be greater than 0 for the power
        if n <= 0: return False

        # checks if n divisible by 2, if n & (n-1) == 0 then its div by 2
        _out = (n & (n-1)) == 0
        # print(n, n-1, (n & (n-1)), _out)
        if not _out: return _out

        result = 1
        i = 0
        while result < n:
            result *= 4
            # print(result)

        return result == n