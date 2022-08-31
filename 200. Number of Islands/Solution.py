class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    island += 1
                    self.scoutIsland(grid, i, j)
            # print(grid)
        return island
    
    def scoutIsland(self, grid, x, y):
        # print(x, y)
        grid[x][y] = -1
        
        if x > 0 and grid[x-1][y] == '1':
            self.scoutIsland(grid, x-1, y)
        if y > 0 and grid[x][y-1] == '1':
            self.scoutIsland(grid, x, y-1)
        if x < len(grid) - 1 and grid[x+1][y] == '1': 
            self.scoutIsland(grid, x+1, y)
        if y < len(grid[x]) - 1 and grid[x][y+1] == '1': 
            self.scoutIsland(grid, x, y+1)