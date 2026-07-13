class Solution:
    def trap(self, height: List[int]) -> int:
        areas = [0]*len(height)

        l = 0
        for r in range(len(height)):
            if height[r] < height[l] or l == r:
                continue
            min_bar = min(height[l], height[r])
            while min_bar and l < r - 1:
                l += 1
                areas[l] = min_bar - height[l]
            l = r
        
        l = len(height) - 1
        for r in range(len(height) - 1, -1, -1):
            if height[r] < height[l] or l == r:
                continue
            min_bar = min(height[l], height[r])
            while min_bar and l > r + 1:
                l -= 1
                areas[l] = max(areas[l], min_bar - height[l])
            l = r

        return sum(areas)
        

