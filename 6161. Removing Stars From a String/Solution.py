class Solution:
    def removeStars(self, s: str) -> str:
        ns = ""
        
        for i in s:
            if i == '*':
                ns = ns[:-1]
            else:
                ns = ns + i
        
        return ns