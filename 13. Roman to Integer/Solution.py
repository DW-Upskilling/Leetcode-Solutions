class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        values = []
        for ch in s:
            values.append(hashMap[ch])
            
        value = 0
        for i, v in enumerate(values[:-1]):
            if v < values[i+1]:
                value -= v
            else:
                value += v
        value += values[-1]
            
        # print(values, value)
        
        return value