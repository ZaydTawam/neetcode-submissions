class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        areas = [0]*n
        l = 0
        for r in range(1, n):
            if height[r] >= height[l]:
                bar_height = min(height[r], height[l])
                while l < r:
                    l += 1
                    areas[l] = max(bar_height - height[l], 0)
        
        r = n - 1
        for l in range(n-2, -1, -1):
            if height[l] >= height[r]:
                bar_height = min(height[r], height[l])
                while l < r:
                    r -= 1
                    areas[r] = max(areas[r], bar_height - height[r], 0)
        
        return sum(areas)


# [0,2,0,3,1,0,1,3,2,1]
#    ^
#        ^

# [0,0,0,0,0,0,0,0,0,0]
