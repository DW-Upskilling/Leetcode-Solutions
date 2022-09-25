class MyCircularQueue:

    def __init__(self, k: int):
        self.__size = k
        self.queue = [None] * self.__size
        
        self.__i = 0
        self.__j = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        self.__j = (self.__j + 1) % self.__size
        self.queue[self.__j] = value
        
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.queue[self.__i] = None
        self.__i = (self.__i + 1) % self.__size
        
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        
        return self.queue[self.__i]
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        
        return self.queue[self.__j]
        

    def isEmpty(self) -> bool:
        return True if self.queue[self.__i] == None else False
        

    def isFull(self) -> bool:
        return True if self.queue[(self.__j + 1) % self.__size] != None else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()