class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        
        output = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            grid[i].sort()
        
        for i in range(n):
            element = grid[0][i]
            for j in range(1, m):
                element = max(element, grid[j][i])
            output += element
        return output