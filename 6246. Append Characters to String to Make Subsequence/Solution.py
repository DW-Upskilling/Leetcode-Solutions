class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        output = 0
        
        i,j = 0,0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                i+=1

        return 0 if len(t) == j else len(t) - j