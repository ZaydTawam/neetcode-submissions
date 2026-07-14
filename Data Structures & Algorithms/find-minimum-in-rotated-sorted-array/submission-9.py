class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        rotated = nums[0] > nums[-1]
        minimum = nums[0]
        while l <= r:
            if not rotated:
                return minimum

            mid = (l + r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                minimum = min(nums[mid], minimum)
                r = mid - 1
        
        return minimum