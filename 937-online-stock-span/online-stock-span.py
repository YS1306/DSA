class StockSpanner:

    def __init__(self):
        self.stack =[]
        self.i = 1

    def next(self, price: int) -> int:
        cnt = 0
        while self.stack and self.stack[-1][0] <= price:
            # cnt += self.i-self.stack[-1][1]-1
            self.stack.pop()
        
        if self.stack:
            cnt = self.i-self.stack[-1][1]
        else:
            cnt = self.i
            
        self.stack.append((price, self.i))  
        self.i += 1      
        return cnt
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)