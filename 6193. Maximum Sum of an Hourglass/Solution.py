class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        
        mx = 0
        m = len(grid)
        for i in range(m):
            if i > m - 3:
                break
            
            n = len(grid[i])
            for j in range(n):
                if j > n - 3:
                    break
                
                s = self.getSum(grid, i, j)
                if s > mx:
                    mx = s
                    
        return mx
                
                
    def getSum(self, grid, x, y):
        
        s = sum(grid[x][y:y+3])
        s += grid[x+1][y+1]
        s += sum(grid[x+2][y:y+3])
        
        return s