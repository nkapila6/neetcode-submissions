class BrowserHistory:

    def __init__(self, homepage: str):
        self.lst = [homepage]
        self.idx = 0
        self.size = 0

    def visit(self, url: str) -> None:
        if self.idx == self.size:
            self.lst.append(url)
            self.idx += 1
            self.size += 1
            return
        
        # idx can only be lower than size
        self.lst = [self.lst[n] for n in range(len(self.lst)) if n<=self.idx] # forward history cleared
        self.lst.append(url)
        self.idx += 1
        self.size = self.idx

    def back(self, steps: int) -> str:
        if self.idx - steps < 0:
           self.idx = 0
           return self.lst[self.idx]
        
        self.idx -= steps
        return self.lst[self.idx]

    def forward(self, steps: int) -> str:
        if self.idx + steps > self.size:
            self.idx = self.size
            return self.lst[self.idx]
        
        self.idx += steps
        return self.lst[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)