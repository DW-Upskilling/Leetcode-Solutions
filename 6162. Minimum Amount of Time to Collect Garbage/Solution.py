class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        
        minutes = 0
        for truck in ['P', 'G', 'M']:
            # print("truck:", truck)
            
            dist = 0
            for i, g in enumerate(garbage):
                
                # print("h:", i, "g:", g)
                
                waits = g.count(truck)
                if truck in g:
                    minutes += waits
                
                if waits != 0:
                    minutes += dist
                    dist = 0
                
                if i < len(travel):
                    dist += travel[i]
                
                # print(minutes)
            if waits != 0 and dist != 0:
                minutes += dist
        return minutes
            
            