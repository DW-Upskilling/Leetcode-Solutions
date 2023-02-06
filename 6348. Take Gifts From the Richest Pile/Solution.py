import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        
        arr = []
        for i in range(k):
            # print(gifts, arr)
            if len(arr) < 1 or len(gifts) < 1 or arr[0] > gifts[-1]:
                gifts.extend(arr)
                arr = []
                gifts.sort()
            
            t = gifts[-1]
            gifts.pop()
            arr.append(int(math.sqrt(t)))
        
        gifts.extend(arr)
        # print(gifts)
        return sum(gifts)
            