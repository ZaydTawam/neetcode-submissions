class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = 1001
        while l <= r:
            if nums[l] <= nums[r]:
                minimum = min(nums[l], minimum)
                break
            mid = (l + r)//2
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                minimum = min(nums[mid], minimum)
                r = mid - 1
        
        return minimum