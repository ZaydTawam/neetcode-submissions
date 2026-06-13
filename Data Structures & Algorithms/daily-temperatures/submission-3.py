class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            if not stk or temperatures[stk[-1]] >= temperatures[i]:
                stk.append(i)
            else:
                while stk and temperatures[stk[-1]] < temperatures[i]:
                    result[stk[-1]] = i - stk[-1]
                    stk.pop()
                stk.append(i)
        
        return result
                


        
