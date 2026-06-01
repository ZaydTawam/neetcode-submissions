class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        for i in range(len(heights)):
            largest_area = max(heights[i], largest_area)
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(heights[j], min_height)
                largest_area = max(min_height*(j-i+1), largest_area)
        
        return largest_area