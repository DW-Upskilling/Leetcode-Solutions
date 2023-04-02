class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        
        d = dict()
        output = []
        
        for i in nums:
            index = 0
            if i in d.keys():
                index = d[i] + 1
            d[i] = index
            
            if len(output) <= index:
                output.append([])
            # print(output, d, index, i)
            
            output[index].append(i)
            
        return output
        