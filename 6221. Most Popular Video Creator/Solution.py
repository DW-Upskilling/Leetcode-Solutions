class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        
        d = dict()
        
        top = ["", 0]
        
        for i in range(len(creators)):
            if creators[i] not in d.keys():
                d[creators[i]] = [creators[i], ids[i], views[i], views[i]]
            elif  views[i] > d[creators[i]][2] or views[i] == d[creators[i]][2] and ids[i] < d[creators[i]][1]:
                d[creators[i]] = [creators[i], ids[i], views[i], views[i] + d[creators[i]][3]]
            else:
                d[creators[i]][3] += views[i]
                
            if d[creators[i]][3] > top[1]:
                top = [creators[i], d[creators[i]][3]]
            
        # print(d, top, second)
        
        output = []
        for k in d.keys():
            if d[k][3] == top[1]:
                output.append([d[k][0], d[k][1]])
        
        return output