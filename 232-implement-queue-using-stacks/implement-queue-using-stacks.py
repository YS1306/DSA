class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.front = -1
        self.rear = -1

    def push(self, x: int) -> None:
        if self.front == self.rear == -1:
            self.front = self.rear = 0
            self.s1.append(x)
        else:
            self.rear += 1
            self.s1.append(x)
            

    def pop(self) -> int:
        print("Before",self.s1, self.front, self.rear)
        while(self.rear - self.front > 0):
            print(self.rear)
            self.s2.append(self.s1.pop(self.rear))
            self.rear -= 1
        temp = self.s1[self.rear]
        self.front += 1
        while(len(self.s2) > 0):
            self.s1.append(self.s2.pop(-1))
            self.rear += 1
        print("After",self.s1, self.front, self.rear)
        
        return temp

    def peek(self) -> int:
        while(self.rear - self.front > 0):
            self.s2.append(self.s1.pop(self.rear))
            self.rear -= 1

        temp = self.s1[self.rear]

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop(-1))
            self.rear += 1
        return temp
        

    def empty(self) -> bool:
        print(self.front, self.rear)
        return self.front == self.rear+1 or (self.front, self.rear) == (-1, -1)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()