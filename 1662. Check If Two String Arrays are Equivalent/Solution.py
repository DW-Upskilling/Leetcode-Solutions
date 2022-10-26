class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        l1 = 0
        l2 = 0
        i = ""
        j = ""
        while l1 < len(word1) and l2 < len(word2):
            if not i:
                i = word1[l1]
                l1 += 1
            if not j:
                j = word2[l2]
                l2 += 1
                
            if i[0] != j[0]:
                return False
            
            i = i[1:]
            j = j[1:]
            
        # print(l1, l2, i, j)
        while l1 < len(word1) and j:
            if not i:
                i = word1[l1]
                l1 += 1
                
            if i[0] != j[0]:
                return False
            
            i = i[1:]
            j = j[1:]
        
        # print(l1, l2, i, j)
        while l2 < len(word2) and i:
            if not j:
                j = word2[l2]
                l2 += 1
                
            if i[0] != j[0]:
                return False
            
            i = i[1:]
            j = j[1:]
        
        
        while i and j:
            if i[0] != j[0]:
                return False
            
            i = i[1:]
            j = j[1:]
        
        if i or j or l1 != len(word1) or l2 != len(word2):
            return False
        
        return True
        