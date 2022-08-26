class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = dict()
        
        for ch in magazine:
            if ch not in d.keys():
                d[ch] = 0
            d[ch] += 1
        
        for ch in ransomNote:
            if ch not in d.keys():
                return False
            
            if d[ch] < 1:
                return False
            
            d[ch] -= 1
            
        return True