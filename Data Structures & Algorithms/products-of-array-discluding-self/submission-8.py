class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1]*n
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        last_val = 1 
        for i in range(n - 2, -1, -1):
            val = last_val * nums[i + 1]
            res[i] *= val
            last_val = val
        
        return res