class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        if len(skill)%2 != 0:
            return -1
        
        skill.sort()
        output = 0
        V = 0
        for i in range(len(skill)//2):
            
            output += skill[i] * skill[(len(skill)-1)-i]
            v = skill[i] + skill[(len(skill)-1)-i]
            if i != 0 and V != v:
                return -1
            V = v
        
        return output
            
            