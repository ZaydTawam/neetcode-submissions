class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            print(l, mid, r)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[l] > target and nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] < target:
                if nums[mid] < nums[l]:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1
        return -1
