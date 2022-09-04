class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        
        d = dict()
        
        for i, ch in enumerate(s):
            
            k = ord(ch) - 97
            
            if k not in d.keys():
                d[k] = i
                
            else:
                d[k] = (i - 1) - d[k]
        
        for k in d.keys():
            if distance[k] != d[k]: return False
            
        return True