class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i, height in enumerate(heights):
            to_push = [i, height]
            
            while stk and stk[-1][1] >= height:
                top_index, top_height = stk.pop()
                area = top_height * (i - top_index)
                print(i, top_index, top_height, area)
                max_area = max(max_area, area)
                to_push[0] = top_index
            
            stk.append(to_push)
        
        for i, height in stk:
            area = height * (len(heights) - i)
            max_area = max(max_area, area)
        
        return max_area