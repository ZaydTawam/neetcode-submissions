class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        stk = []

        for i, height in enumerate(heights):
            to_push = [i, height]
            while stk and stk[-1][1] > height:
                to_push[0] = stk[-1][0]
                area = stk[-1][1] * (i - stk[-1][0])
                largest_area = max(area, largest_area)
                stk.pop()
            stk.append(to_push)
        
        while stk:
            area = stk[-1][1] * (len(heights) - stk[-1][0])
            largest_area = max(area, largest_area)
            stk.pop()
        
        return largest_area