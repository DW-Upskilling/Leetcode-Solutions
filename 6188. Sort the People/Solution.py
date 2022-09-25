class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        d = dict()
        
        for i, h in enumerate(heights):
            d[h] = i
            
        output = []
        for k in sorted(d.keys(), reverse=True):
            output.append(names[d[k]])
            
        return output