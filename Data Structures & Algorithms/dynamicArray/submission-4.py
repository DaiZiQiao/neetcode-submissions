class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.length:
            self.arr[i] = n            

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1
            
    def popback(self) -> int:
        val = self.arr[self.length - 1]
        self.arr[self.length  -1] = None
        self.length -=1
        return val

    def resize(self) -> None:
        self.capacity = self.capacity*2
        tmp_arr = [0] * self.capacity
        for i in range(self.length):
            tmp_arr[i] = self.arr[i]
        self.arr = tmp_arr

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
