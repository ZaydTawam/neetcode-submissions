class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            while stk and stk[-1][1] < temperatures[i]:
                result[stk[-1][0]] = i - stk[-1][0]
                stk.pop() 
            stk.append([i, temperatures[i]])
        
        return result