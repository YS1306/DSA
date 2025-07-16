class MinStack:

    def __init__(self):
        self.stack = []
        self.topo = -1
        self.min = 0

    def push(self, val: int) -> None:
        self.topo += 1
        self.stack.append(val)
        if self.stack[self.min] >= val:
            self.min = self.topo
        

    def pop(self) -> None:
        if self.min == self.topo:
            temp = self.topo-1
            self.min = temp
            while temp >= 0:
                if self.stack[self.min] >= self.stack[temp]:
                    self.min = temp
                temp -= 1
                
        self.stack.pop()
        self.topo -= 1

    def top(self) -> int:
        return self.stack[self.topo]

    def getMin(self) -> int:
        return self.stack[self.min]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()