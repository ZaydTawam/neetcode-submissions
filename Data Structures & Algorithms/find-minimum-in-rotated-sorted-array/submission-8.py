class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_element = float('inf')
        while l <= r:
            mid = (l + r)//2
            if nums[0] > nums[-1] and nums[mid] >= nums[0]:
                l = mid + 1
            else:
                min_element = min(nums[mid], min_element)
                r = mid - 1
        
        return min_element