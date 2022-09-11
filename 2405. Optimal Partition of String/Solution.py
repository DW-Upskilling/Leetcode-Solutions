class Solution:
    def partitionString(self, s: str) -> int:
        
        out = 0
        d = dict()
        for c in s:
            
            if c not in d.keys():
                d[c] = 0
            
            if d[c] == 1:
                out += 1
                # print(d)
                for k in d.keys():
                    d[k] = 0
                
            d[c] = 1
        out += 1
        # print(d)
    
        return out