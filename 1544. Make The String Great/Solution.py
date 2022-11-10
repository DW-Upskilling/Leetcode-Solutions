class Solution:
    def makeGood(self, s: str) -> str:
        
        while True:
            
            toRemove = []
            for i in range(len(s) - 1):
                if (s[i] == s[i+1].lower() or s[i] == s[i+1].upper()) and s[i] != s[i+1]:
                    if i-1 not in toRemove:
                        toRemove.append(i)
                
            for i in toRemove[::-1]:
                s = s[:i] + s[i+2:]
            
            if not toRemove:
                break
        
        return s