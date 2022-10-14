class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        for i in nums1:
            if i not in d1.keys():
                d1[i] = 0
            d1[i] += 1
        
        d2 = dict()
        for i in nums2:
            if i not in d2.keys():
                d2[i] = 0
            d2[i] += 1
            
        output = []
        for i in d1.keys():
            if i in d2.keys():
                repeat = d1[i]
                if d1[i] > d2[i]:
                    repeat = d2[i]
                
                output += [i] * repeat
        return output