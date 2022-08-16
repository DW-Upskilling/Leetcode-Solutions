class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = dict()
        for i, ch in enumerate(s):
            if ch in d.keys():
                d[ch] = -1
                continue
            d[ch] = i
        
        for k in d.keys():
            if d[k] != -1:
                return d[k]
        
        return -1