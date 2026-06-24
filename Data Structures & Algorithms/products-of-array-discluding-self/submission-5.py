class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        for i in range(1, n):
            l[i] = nums[i - 1] * l[i - 1]
        r = [1] * n
        for i in range(n - 2, -1, -1):
            r[i] = nums[i + 1] * r[i + 1]
        
        res = []
        for i in range(n):
            res.append(l[i]*r[i])
        
        return res