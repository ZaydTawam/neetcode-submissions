class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        if not self.arr or val < self.min_arr[-1]:
            self.min_arr.append(val)
        else:
            self.min_arr.append(self.min_arr[-1])
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1]
        
