class Solution:
    def intToRoman(self, num: int) -> str:
        
        ROMANS = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',  50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        
        output = ""
        for _v_ in list(ROMANS.keys())[::-1]:
            
            while num >= _v_:
                output += ROMANS[_v_]
                num -= _v_
            
        return output