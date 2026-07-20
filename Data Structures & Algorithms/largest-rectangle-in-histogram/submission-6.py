class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            to_append = [i, height]
            while stk and height < stk[-1][1]:
                area = (i - stk[-1][0]) * stk[-1][1]
                max_area = max(max_area, area)
                to_append[0] = stk[-1][0]
                stk.pop()
            stk.append(to_append)
        
        for i, height in stk:
            area = (len(heights) - i) * height
            max_area = max(max_area, area)

        return max_area