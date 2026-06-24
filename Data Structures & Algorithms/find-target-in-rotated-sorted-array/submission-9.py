class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid  = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[r]:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] >= nums[l]:
                if nums[l] > target or nums[mid] < target: 
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1



# rotated if: nums[0] > nums[-1]

# in left part if: nums[i] > nums[0]

# in right part if: nums[i] < nums[-1]

# [5,1,2,3,4]
#    ^
#    ^
#    ^