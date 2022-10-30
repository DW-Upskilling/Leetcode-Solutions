class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def sumOfDigits(a):
            s = 0
            while a:
                s += a%10
                a //= 10
            return s
        
        added = 0
        digit = 1
        while True:
            if sumOfDigits(n + added) <= target:
                return added
            added += (10**digit - ((n+added) % 10**digit))
            # print(n, added, digit)
            digit += 1