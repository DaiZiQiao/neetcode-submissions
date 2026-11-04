class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        if i < self.length:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.capacity:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            val = self.arr[self.length-1]
            self.arr[self.length-1] = 0
            self.length -= 1
        return val

    def resize(self) -> None:
        self.capacity *= 2
        tmp_arr = [0] * self.capacity
        tmp_arr[:self.length] = self.arr[:self.length]
        self.arr = tmp_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
