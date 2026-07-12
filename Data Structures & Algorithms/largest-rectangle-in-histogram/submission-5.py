class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            to_append = [i, height]
            while stk and stk[-1][1] > height:
                starting_index, prev_height = stk[-1]
                area = prev_height * (i - starting_index)
                max_area = max(max_area, area)
                to_append[0] = starting_index
                stk.pop()
            
            stk.append(to_append)
        
        for starting_index, height in stk:
            area = height * (len(heights) - starting_index)
            max_area = max(max_area, area)
        
        return max_area