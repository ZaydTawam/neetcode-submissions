class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i != 0:
                if nums[i - 1] == nums[i]:
                    continue
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while True:
                if l >= r:
                    break
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[l], nums[r], nums[i]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    continue
                if total > target:
                    r -= 1
                else:
                    l += 1

        return res