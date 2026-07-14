class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(combination, curr_sum, index):
            if curr_sum == target:
                combinations.append(combination.copy())

            for i in range(index, len(nums)):
                if curr_sum + nums[i] > target:
                    continue
                combination.append(nums[i])
                backtrack(combination, curr_sum + nums[i], i)
                combination.pop()
        
        backtrack([], 0, 0)
        return combinations