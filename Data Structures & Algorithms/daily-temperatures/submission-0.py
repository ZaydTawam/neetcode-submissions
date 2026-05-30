class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            if not i:
                stk.append(i)
                continue
            
            while stk and temperatures[i] > temperatures[stk[-1]]:
                result[stk[-1]] = i - stk[-1]
                stk.pop()
            
            stk.append(i)
            
        return result