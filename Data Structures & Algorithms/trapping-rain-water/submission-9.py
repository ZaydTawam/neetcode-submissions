class Solution:
    def trap(self, height: List[int]) -> int:
        temp_areas = []
        areas_left = []
        tallest = 0
        for h in height:
            if h >= tallest:
                areas_left += temp_areas
                areas_left.append(0)
                temp_areas = []
                tallest = h
            else:
                temp_areas.append(tallest - h)
        
        areas_left += [0] * len(temp_areas)

        temp_areas = []
        areas_right = []
        tallest = 0
        for h in height[::-1]:
            if h >= tallest:
                areas_right += temp_areas
                areas_right.append(0)
                temp_areas = []
                tallest = h
            else:
                temp_areas.append(tallest - h)
        
        areas_right += [0] * len(temp_areas)

        areas_right = areas_right[::-1]
        max_area = 0
        print(areas_left, areas_right)
        for i in range(len(height)):
            max_area += max(areas_left[i], areas_right[i])

        return max_area