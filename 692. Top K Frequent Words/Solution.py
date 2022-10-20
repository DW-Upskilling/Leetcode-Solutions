class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        counts = dict()
        for i in words:
            if i not in counts.keys():
                counts[i] = 0
            counts[i] += 1
            
        
        values = dict()
        for i in counts.keys():
            if counts[i] not in values.keys():
                values[counts[i]] = []
            
            values[counts[i]].append(i)
            
        counts = values
        # print(counts)
        output = []
        for i in sorted(counts.keys(), reverse=True):
            counts[i].sort()
            for s in counts[i]:
                output.append(s)
                k -= 1
                if k <= 0:
                    break
            if k <= 0:
                break
        
        # output.sort()
        return output
 