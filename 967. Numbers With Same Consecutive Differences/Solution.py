class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        
        pairs = dict()
        
        for i in range(9, k-1, -1):
            
            j = str(i - k)
            i = str(i)
            
            if i not in pairs.keys():
                pairs[i] = []
            if j not in pairs.keys():
                pairs[j] = []
            
            pairs[i].append(j)
            pairs[j].append(i)
            
        # print(pairs)
        
        output = []
        for k in pairs.keys():
            if k == '0': continue
            output.extend(self.concatNextDigit(pairs, n, k))
            
        output = list(set(output))
        output.sort()
        return output
    
    def concatNextDigit(self, pairs, n, s):
        if len(s) == n: return [s]
        
        narr = []
        for i in pairs[s[-1]]:
            
            narr.extend(self.concatNextDigit(pairs, n, s + i))
            
        return narr