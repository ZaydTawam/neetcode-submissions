class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stk = []

        for i, height in enumerate(heights):
            if not stk or stk[-1][0] < height:
                stk.append((height, i))
            elif stk[-1][0] > height:
                index = i
                while stk and stk[-1][0] > height:
                    top = stk.pop()
                    area = top[0] * (i - top[1])
                    max_area = max(max_area, area)
                    index = top[1]
                
                stk.append((height, index))
        
        while stk:
            top = stk.pop()
            area = top[0] * (len(heights) - top[1])
            max_area = max(max_area, area)

        return max_area