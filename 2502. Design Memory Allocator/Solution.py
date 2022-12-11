class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.size = n
        

    def allocate(self, size: int, mID: int) -> int:
        if size > self.size:
            return -1
        
        curr = size
        index = -1
        for i in range(self.size):
            if self.memory[i] > 0:
                curr = size
                continue
            curr -= 1
            if curr == 0:
                index = i
                break
        # print(curr, index, self.memory)
        if curr != 0: return -1
        
        for i in range(index, index-size, -1):
            self.memory[i] = mID
        # print(self.memory)
        return (index+1)-size

    def free(self, mID: int) -> int:
        unit = 0
        for i in range(self.size):
            if self.memory[i] == mID:
                unit += 1
                self.memory[i] = 0
        return unit
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)