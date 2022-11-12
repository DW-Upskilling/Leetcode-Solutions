class MedianFinder:

    def __init__(self):
        
        self.arr = []
        self.isEven = True
        

    def addNum(self, num: int) -> None:
        
        def binarySearch(i, j, v):
            
            if i >= j:
                return i
            
            mid = (i + j) // 2
            
            if self.arr[mid] == v:
                return mid
            
            if self.arr[mid] > v:
                return binarySearch(i, mid, v)
            return binarySearch(mid+1, j, v)
        
        index = binarySearch(0, len(self.arr), num)
        # print(num, index)
        
        if index == len(self.arr):
            self.arr.append(num)
        else:
            self.arr.insert(index, num)
        self.isEven = not self.isEven
        

    def findMedian(self) -> float:
        
        mid = len(self.arr) // 2
        
        if self.isEven:
            return sum([self.arr[mid] + self.arr[mid-1]]) / 2
        
        return self.arr[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()