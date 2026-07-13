class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        areas = [0]*n

        left_bar = 0
        for right_bar in range(n):
            if height[right_bar] < height[left_bar] or left_bar == right_bar:
                continue
            min_bar = min(height[left_bar], height[right_bar])
            if min_bar:
                for i in range(left_bar + 1, right_bar):
                    areas[i] = min_bar - height[i]
            left_bar = right_bar
        
        right_bar = n - 1
        for left_bar in range(n - 1, -1, -1):
            if height[left_bar] < height[right_bar] or right_bar == left_bar:
                continue
            min_bar = min(height[right_bar], height[left_bar])
            if min_bar:
                for i in range(right_bar - 1, left_bar, -1):
                    areas[i] = max(areas[i], min_bar - height[i])
            right_bar = left_bar

        return sum(areas)
        

