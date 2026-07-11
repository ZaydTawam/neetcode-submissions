class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk or val < self.min_stk[-1]:
            self.min_stk.append(val)
        else:
            self.min_stk.append(self.min_stk[-1])       

    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        

    def getMin(self) -> int:
        if self.min_stk:
            return self.min_stk[-1]
        
