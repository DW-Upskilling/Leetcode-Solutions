class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        
        m = len(heights)
        n = len(heights[0])
        
        d = dict()
        # self.trackWaterFlow(heights, 0, 4, d, 0)
        # self.trackWaterFlow(heights, 0, 4, d, 1)
        
        for i in range(m):
            self.trackWaterFlow(heights, i, 0, d, 0)
            self.trackWaterFlow(heights, i, n-1, d, 1)
            
        for i in range(n):
            self.trackWaterFlow(heights, 0, i, d, 0)
            self.trackWaterFlow(heights, m-1, i, d, 1)
        
        # print(d)
        output = []
        for i in d.keys():
            for j in d[i].keys():
                if d[i][j][0] and d[i][j][1]:
                    output.append([i, j])
                    
        return output
    
    def trackWaterFlow(self, heights, x, y, d, index):
        if x in d.keys() and y in d[x].keys() and d[x][y][index]: return None
        
        if x not in d.keys():
            d[x] = dict()
            d[x][y] = [0, 0]
        elif y not in d[x].keys():
            d[x][y] = [0, 0]
        
        # print(x, y)
        d[x][y][index] = 1
        
        h = heights[x][y]
        
        if x > 0 and heights[x-1][y] >= h:
            # print(h, heights[x-1][y], x-1, y, index)
            self.trackWaterFlow(heights, x-1, y, d, index)
        if y > 0 and heights[x][y-1] >= h:
            # print(h, heights[x][y-1], x, y-1, index)
            self.trackWaterFlow(heights, x, y-1, d, index)
            
        if x < len(heights)-1 and heights[x+1][y] >= h:
            # print(h, heights[x+1][y], x+1, y, index)
            self.trackWaterFlow(heights, x+1, y, d, index)
        if y < len(heights[x]) - 1 and heights[x][y+1] >= h:
            # print(h, heights[x][y+1], x, y+1, index)
            self.trackWaterFlow(heights, x, y+1, d, index)
        
        # print("----")
