class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_left = [1]*n
        for i in range(1, n):
            prefix_left[i] = prefix_left[i - 1] * nums[i - 1] 
        
        prefix_right = [1]*n
        for i in range(n - 2, -1, -1):
            prefix_right[i] = prefix_right[i + 1] * nums[i + 1]
        
        output = []
        for i in range(n):
            output.append(prefix_left[i] * prefix_right[i])
        
        return output