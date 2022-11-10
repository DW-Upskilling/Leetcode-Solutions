class StockSpanner:

    def __init__(self):
        
        self.arr = []
        self.map = dict()
        

    def next(self, price: int) -> int:
        
        output = 1
        if not self.arr:
            self.map[price] = {0: 1}
            
        elif price >= self.arr[-1]:
            index = len(self.arr) - 1
            value = 1
            while self.arr[index] <= price and index > -1:
                _temp = self.map[self.arr[index]]
                # print(_temp, index)
                value += _temp[index]
                index -= _temp[index]
                # break
            if price in self.map.keys():
                self.map[price][len(self.arr)] = value
            else:
                self.map[price] = {len(self.arr): value}
            output = value
        else:
            if price in self.map.keys():
                self.map[price][len(self.arr)] = 1
            else:
                self.map[price] = {len(self.arr): 1}
        self.arr.append(price)
        
        # print(self.map, self.arr)
        
        return output


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)