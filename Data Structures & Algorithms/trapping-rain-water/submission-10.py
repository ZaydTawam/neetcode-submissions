class Solution:
    def trap(self, height: List[int]) -> int:
        areas_left = [0 for _ in range(len(height))]
        areas_right = [0 for _ in range(len(height))]
        
        slow, fast = 0, 0
        while fast < len(height) - 1:
            fast += 1
            if height[fast] >= height[slow]:
                min_height = min(height[fast], height[slow])
                if not fast - slow - 1:
                    slow = fast
                    continue
                else:
                    while True:
                        slow += 1
                        if slow == fast:
                            break
                        areas_left[slow] = min_height - height[slow]

        height = height[::-1]

        slow, fast = 0, 0
        while fast < len(height) - 1:
            fast += 1
            if height[fast] >= height[slow]:
                min_height = min(height[fast], height[slow])
                if not fast - slow - 1:
                    slow = fast
                    continue
                else:
                    while True:
                        slow += 1
                        if slow == fast:
                            break
                        areas_right[slow] = min_height - height[slow]
        
        areas_right = areas_right[::-1]
        total_area = 0
        for i in range(len(height)):
            total_area += max(areas_left[i], areas_right[i])
        
        return total_area
        

                
        


        
# [0,2,0,3,1,0,1,3,2,1]
#  ^ ^ 
# 1 - 0 - 1 = 0
# min(0, 2) = 0
# area = 0*0 = 0

# [0,2,0,3,1,0,1,3,2,1]
#    ^   ^ 
# 3 - 1 - 1 = 1
# min(2, 3) = 2
# area = 1*2 = 2

# [0,2,0,3,1,0,1,3,2,1]
#        ^       ^ 
# 7 - 3 - 1 = 3
# min(3, 3) = 3
# area = 3*3 - 2 = 7

# [0,2,0,3,1,0,1,3,2,1]
#                ^
